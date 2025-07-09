import typer
from core import storage

app = typer.Typer()

notes_path = "data/notes.json"

@app.command()
def add_note(note: str):
    """Add a new note."""
    notes = storage.load_data(notes_path)
    notes.append(note)
    storage.save_data(notes_path, notes)
    typer.echo(f"✅ Note added: {note}")