# Standard Library
import json
from datetime import datetime

from typer.testing import CliRunner

# WHICH_BEER
# which_beer
from which_beer.main import app


runner = CliRunner()


def test_app_should_get_beer_by_id():
    result = runner.invoke(app, ["beers", "by-id", "1"])
    body = json.loads(result.stdout)

    assert result.exit_code == 0
    assert len(body) == 1
    assert body[0]["id"] == 1


def test_app_should_get_randomic_beer():
    result = runner.invoke(app, ["beers", "random"])
    body = json.loads(result.stdout)

    assert result.exit_code == 0
    assert len(body) == 1
    assert body[0]["id"] is not None


def test_app_should_get_list_beers_by_brew_date():
    result = runner.invoke(app, ["beers", "brewed-before", "10-2011"])
    body = json.loads(result.stdout)

    first_brewed = body[0]["first_brewed"]
    date_example = datetime.strptime(first_brewed, "%m/%Y")
    date_reference = datetime.strptime("10-2011", "%m-%Y")

    assert result.exit_code == 0
    assert len(body) > 0
    assert date_example < date_reference
