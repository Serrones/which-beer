# Standard Library
import os
import shutil

from typer.testing import CliRunner

# which_beer
from which_beer.main import app


runner = CliRunner()


def get_file_path():
    root_path = os.getcwd()
    file_path = root_path + "/files/"
    return file_path


def clean_files_folder():
    file_path = get_file_path()
    shutil.rmtree(file_path)
    os.mkdir(file_path)
    return


def test_app_should_create_json_file():
    result = runner.invoke(app, ["beers", "id", "1", "--json-file"])

    file_path = get_file_path()
    file_list = os.listdir(file_path)

    clean_files_folder()

    assert result.exit_code == 0
    assert file_list[0][-4:] == "json"


def test_app_should_create_csv_file():
    result = runner.invoke(app, ["beers", "id", "1", "--csv-file"])

    file_path = get_file_path()
    file_list = os.listdir(file_path)

    clean_files_folder()

    assert result.exit_code == 0
    assert file_list[0][-3:] == "csv"
