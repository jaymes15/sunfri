import requests

from core.helpers import get_env_variable

THE_ONE_API_URL = get_env_variable('THE_ONE_API_URL')
THE_ONE_API_KEY = get_env_variable('THE_ONE_API_KEY')


def get_characters():
    """Returns character from the one api"""
    url = f"{THE_ONE_API_URL}/characters"
    response = requests.get(url)
    return response.json()


def get_quotes_from_specified_character(character_id):
    """Return all quotes from the specified character"""
    url = f"{THE_ONE_API_URL}/characters/{character_id}/quotes"
    response = requests.get(url)
    return response.json()
