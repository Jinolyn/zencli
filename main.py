#!/usr/bin/env python3

import typer
from cli import note, todo, time_display

app = typer.Typer(help="Personal CLI Assistant ")

app.add_typer(note.app, name="note", help="Manage your notes")
app.add_typer(time_display.app, name="time", help="Display current time")
app.add_typer(todo.app, name="todo", help="Manage your to-do list")


if __name__ == "__main__":
    app()
