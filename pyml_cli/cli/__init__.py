"""Initialize the CLI package."""

from typer import Typer

from .project import initialize

app = Typer()
app.command()(initialize)
