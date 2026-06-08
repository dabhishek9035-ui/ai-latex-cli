import typer

app = typer.Typer(
    name="latex-ai",
    help="AI-powered terminal CLI for generating LaTeX reports."
)

@app.command()
def init():
    """
    Initialize a new AI LaTeX project.
    """
    typer.echo("Initializing a new VTU LaTeX project... (Coming soon!)")

@app.command()
def compile(filename: str):
    """
    Compile a .tex file to PDF.
    """
    typer.echo(f"Compiling {filename}... (Coming soon!)")

if __name__ == "__main__":
    app()
