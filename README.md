# GitHub Tools

Using the GitHub API to automate certain tasks.

## Copying issues

Issues were not being copied over from a template repo we have. So that's the first task we fixed:

### Example:

```
$ python -m ghtools --destination some_repo
Copying milestones ...
Result:
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Status ┃ Milestone                                                                  ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ✅     │ Copied milestone Some milestone                                            │
│ ✅     │ Copied milestone Some other milestone                                      │
│ ✅     │ Copied milestone A third milestone                                         │
└────────┴────────────────────────────────────────────────────────────────────────────┘
Copying issues ...
Result:
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Status ┃ Issue                                                    ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ✅     │ Copied issue Issue Feature 1                             │
│ ✅     │ Copied issue Some other issue                            │
│ ✅     │ Copied issue Yet another issue                           │
└────────┴──────────────────────────────────────────────────────────┘
```

### Config

You can set the following environment variables:

```
$ more .env-template
GITHUB_REPO_TOKEN=
REPO_OWNER=
SOURCE_REPO=
DESTINATION_REPO=
```

`GITHUB_REPO_TOKEN` and `REPO_OWNER` are required. We only support the same owner for source and destination repos at this point.

Source and destination repos can be given from the command line, if omitted the script will look at the `SOURCE_REPO` and `DESTINATION_REPO` environment variables.

### Usage options

You can also chose to only copy milestones or issues:

```
$ python -m ghtools --help

 Usage: python -m ghtools [OPTIONS]

 Copy milestones and issues from source to destination repo

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --source                                        TEXT  [default: TemplateRepo]                                                                                                      │
│ --destination                                   TEXT  [default: None]                                                                                                              │
│ --copy-milestones       --no-copy-milestones          [default: copy-milestones]                                                                                                   │
│ --copy-issues           --no-copy-issues              [default: copy-issues]                                                                                                       │
│ --install-completion                                  Install completion for the current shell.                                                                                    │
│ --show-completion                                     Show completion for the current shell, to copy it or customize the installation.                                             │
│ --help                                                Show this message and exit.                                                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
