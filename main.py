import typer
from cli import note, todo

app = typer.Typer(help="Personal CLI Assistant ")

app.add_typer(note.app, name="note", help="Manage your notes")



if __name__ == "__main__":
    app()
