"""Initialize the CLI package."""

from typer import Typer

from .project import init
from .system import status

app = Typer(pretty_exceptions_show_locals=False)

app.command()(init)
app.command()(status)
