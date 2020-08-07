import json
import os
import requests
import typer

app = typer.Typer()


@app.command()
def by_id(
    id_number: int,
    json_file: bool=False
):
    """
    Returns a specific beer by id

    """
    url_base = 'https://api.punkapi.com/v2/beers'
    
    if id_number > 0:
        url_base += f'/{str(id_number)}'
        response = requests.get(url_base)
        parsed = json.loads(response.text)
        beer = json.dumps(parsed, indent=2)
        
        if json_file:
            root_dir = os.getcwd()
            file_dir = root_dir + '/files/'
            file_name = file_dir + f'beer-{id_number}.json'
            with open(file_name, 'w') as outfile:
                json.dump(response.json(), outfile, indent=2)
        typer.echo(beer)
    else:
        message = (
            'Please insert a valid number'
        ) 
        typer.echo(message)

@app.command()
def random(
    json_file: bool=False
):
    """
    Returns a randomic beer
    """
    url = 'https://api.punkapi.com/v2/beers/random'

    response = requests.get(url)
    parsed = json.loads(response.text)
    beer = json.dumps(parsed, indent=2)

    if json_file:
            root_dir = os.getcwd()
            file_dir = root_dir + '/files/'
            beer_number = response.json()[0]['id']
            file_name = file_dir + f'beer-{beer_number}.json'
            with open(file_name, 'w') as outfile:
                json.dump(response.json(), outfile, indent=2)
    typer.echo(beer)

@app.command()
def brewed_before(
    brew_date: str,
    json_file: bool=False
):
    """
    Returns a list of beers brewed before
    a given date, formated as mm-yyyy
    """
    url = f'https://api.punkapi.com/v2/beers?brewed_before={brew_date}'
   
    response = requests.get(url)
    parsed = json.loads(response.text)
    beers = json.dumps(parsed, indent=2)
    
    if json_file:
            root_dir = os.getcwd()
            file_dir = root_dir + '/files/'
            file_name = file_dir + f'beers-brewed-before-{brew_date}.json'
            with open(file_name, 'w') as outfile:
                json.dump(response.json(), outfile, indent=2)
    typer.echo(beers)

if __name__ == '__main__':
    app()
