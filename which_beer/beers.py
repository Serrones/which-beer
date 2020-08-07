import json
import requests
import typer

app = typer.Typer()


@app.command()
def by_id(
    id_number: int
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
        
        typer.echo(beer)
    else:
        message = (
            'Please insert a valid number'
        ) 
        typer.echo(message)

@app.command()
def random():
    """
    Returns a randomic beer
    """
    url = 'https://api.punkapi.com/v2/beers/random'
    
    response = requests.get(url)
    parsed = json.loads(response.text)
    beer = json.dumps(parsed, indent=2)
    typer.echo(beer)

@app.command()
def brewed_before(
    brew_date: str
):
    """
    Returns a list of beers brewed before
    a given date, formated as mm-yyyy
    """
    url = f'https://api.punkapi.com/v2/beers?brewed_before={brew_date}'
   
    response = requests.get(url)
    parsed = json.loads(response.text)
    beer = json.dumps(parsed, indent=2)
    typer.echo(beer)

if __name__ == '__main__':
    app()
