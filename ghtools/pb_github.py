from typing import NamedTuple

from github import Github, GithubException
from github.Issue import Issue

from .constants import GH_TOKEN, GH_USER, OPEN_STATUS


class Message(NamedTuple):
    success: bool
    msg: str


class PybitesGithub:
    def __init__(
        self,
        source_repo_name,
        destination_repo_name,
        token=GH_TOKEN,
        user=GH_USER,
    ):
        self.destination_repo_name = destination_repo_name
        self.gh = Github(token)
        self.source_repo = self.gh.get_repo(f"{user}/{source_repo_name}")
        self.destination_repo = self.gh.get_repo(f"{user}/{destination_repo_name}")

    def copy_milestones(self) -> list[Message]:
        milestones = self.source_repo.get_milestones(state=OPEN_STATUS)
        output = []
        for milestone in milestones:
            try:
                self.destination_repo.create_milestone(
                    title=milestone.title,
                    state=milestone.state,
                    description=milestone.description,
                )
            except GithubException as exc:
                output.append(
                    Message(
                        success=False, msg=f"Cannot create milestone, exception: {exc}"
                    )
                )
            else:
                output.append(
                    Message(success=True, msg=f"Copied milestone {milestone.title}")
                )
        return output

    def _should_skip_issue(self, issue: Issue, issue_filter: str | None = None) -> bool:
        if issue_filter is None:
            return False
        return issue_filter.lower() not in issue.title.lower()

    def copy_issues(self, issue_filter: str | None = None) -> list[Message]:
        issues = self.source_repo.get_issues(state=OPEN_STATUS)
        issue_titles_already_copied = {
            issue.title for issue in self.destination_repo.get_issues()
        }
        output = []
        for issue in issues:
            if issue.title in issue_titles_already_copied:
                output.append(Message(success=False, msg="Issue already created, skip"))
                continue

            if self._should_skip_issue(issue, issue_filter):
                output.append(
                    Message(
                        success=False,
                        msg=f"Issue does not match '{issue_filter}', skip",
                    )
                )
                continue

            params = {"title": issue.title}

            if issue.body is not None:
                params.update({"body": issue.body})

            if issue.milestone is not None:
                params.update({"milestone": issue.milestone})

            if issue.labels:
                labels = [label.name for label in issue.labels]
                params.update({"labels": labels})

            try:
                self.destination_repo.create_issue(**params)
            except GithubException as exc:
                output.append(
                    Message(success=False, msg=f"Cannot create issue, exception: {exc}")
                )
            else:
                output.append(Message(success=True, msg=f"Copied issue {issue.title}"))
        return output
