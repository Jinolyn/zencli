import typer
from core import storage

app = typer.Typer(help="Manage your to-do list")
todo_path = "data/todos.json"

@app.command()
def add_task(task: str):
    """Add a new task to your to-do list."""
    tasks = storage.load_data(todo_path)
    tasks.append(task)
    storage.save_data(todo_path, tasks)
    typer.echo(f"Task '{task}' added to your to-do list.")


@app.command()
def todo_list():
    """List all tasks in your to-do list."""
    tasks = storage.load_data(todo_path)
    if not tasks:
        typer.echo("Your to-do list is empty.")
    else:
        typer.echo("📝 To-Do List:")
        for i, task in enumerate(tasks, start=1):
            typer.echo(f"{i}. {task}")