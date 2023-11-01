import typer
from rich.console import Console
from rich.table import Table

from .constants import DESTINATION_REPO, SOURCE_REPO
from .pb_github import Message, PybitesGithub

app = typer.Typer()
console = Console()
err_console = Console(stderr=True)


def _show_results(output: list[Message], *, col_name) -> None:
    table = Table("Status", col_name)
    if output:
        for line in output:
            icon = "✅" if line.success else "❌"
            table.add_row(icon, line.msg)
        console.print(table)
    else:
        err_console.print(f"[red]No {col_name.lower()}s to copy[/red]")


@app.command()
def main(
    source: str = typer.Option(SOURCE_REPO),
    destination: str = typer.Option(DESTINATION_REPO),
    copy_milestones: bool = True,
    copy_issues: bool = True,
    issue_filter: str = typer.Option(None, help="Only copy issues matching filter."),
):
    """Copy milestones and issues from source to destination repo"""
    if source is None or destination is None:
        err_console.print(
            "[bold red]Need to know both source and " "destination repos[/bold red]"
        )
        raise typer.Exit(code=1)

    pb_gh = PybitesGithub(source, destination)

    if copy_milestones:
        console.print("[green]Copying milestones ...[/green]")
        output = pb_gh.copy_milestones()
        _show_results(output, col_name="Milestone")

    if copy_issues:
        console.print("[green]Copying issues ...[/green]")
        output = pb_gh.copy_issues(issue_filter)
        _show_results(output, col_name="Issue")


if __name__ == "__main__":
    app()
