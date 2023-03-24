import typer
from rich.console import Console
from rich.table import Table

from .pb_github import Message, PybitesGithub

app = typer.Typer()
console = Console()


def _show_results(output: list[Message], *, col_name) -> None:
    console.print("Result:")
    table = Table("Status", col_name)
    for line in output:
        icon = "✅" if line.success else "❌"
        table.add_row(icon, line.msg)
    console.print(table)


@app.command()
def main(
    destination_repo_name: str,
    copy_milestones: bool = True,
    copy_issues: bool = True,
):
    pb_gh = PybitesGithub(destination_repo_name)

    if copy_milestones:
        console.print("[green]Copying milestones ...[/green]")
        output = pb_gh.copy_milestones()
        _show_results(output, col_name="Milestone")

    if copy_issues:
        console.print("[green]Copying issues ...[/green]")
        output = pb_gh.copy_issues()
        _show_results(output, col_name="Issue")


if __name__ == "__main__":
    app()
