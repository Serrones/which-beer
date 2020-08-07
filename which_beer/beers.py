import requests
import typer

from .helpers import (
    url_base,
    format_json,
    get_file_path,
    create_json_file
)

app = typer.Typer()


@app.command()
def by_id(
    id_number: int,
    json_file: bool=False
) -> None:
    """
    Returns a specific beer by id

    """
    if id_number > 0:
        url = url_base()
        url += f'/{str(id_number)}'
        
        response = requests.get(url)
        beer = format_json(response)
        
        if json_file:
            file_dir = get_file_path()
            file_name = file_dir + f'beer-{id_number}.json'
            create_json_file(file_name, response)
        typer.echo(beer)
    else:
        message = (
            'Please insert a valid number'
        ) 
        typer.echo(message)


@app.command()
def random(
    json_file: bool=False
) -> None:
    """
    Returns a randomic beer
    """
    url = url_base()
    url += '/random'

    response = requests.get(url)
    beer = format_json(response)

    if json_file:
            file_dir = get_file_path()
            beer_number = response.json()[0]['id']
            file_name = file_dir + f'beer-{beer_number}.json'
            create_json_file(file_name, response)
    typer.echo(beer)


@app.command()
def brewed_before(
    brew_date: str,
    json_file: bool=False
) -> None:
    """
    Returns a list of beers brewed before
    a given date, formated as mm-yyyy
    """
    url = url_base()
    url += f'?brewed_before={brew_date}'
   
    response = requests.get(url)
    beers = format_json(response)
    
    if json_file:
            file_dir = get_file_path()
            file_name = file_dir + f'beers-brewed-before-{brew_date}.json'
            create_json_file(file_name, response)
    typer.echo(beers)

if __name__ == '__main__':
    app()
