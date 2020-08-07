import typer

from .beers import app as beers_app

app = typer.Typer()

app.add_typer(beers_app, name='beers')


if __name__ == '__main__':
    app()