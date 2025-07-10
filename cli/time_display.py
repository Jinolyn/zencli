from datetime import datetime
import typer

app = typer.Typer(help="Time Display CLI")

@app.command()
def get_current_time():
    """Get the current time in a formatted string."""
    typer.echo(f"⏰ {datetime.now().strftime('%I:%M %p')}")

