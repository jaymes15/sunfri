import requests

from core.helpers import get_env_variable

THE_ONE_API_URL = get_env_variable('THE_ONE_API_URL')
THE_ONE_API_KEY = get_env_variable('THE_ONE_API_KEY')
THE_ONE_API_REQUEST_HEADER = {
    "Authorization": f"Bearer {THE_ONE_API_KEY}"
}


def get_characters():
    """Returns character from the one api"""
    url = f"{THE_ONE_API_URL}/character"
    response = requests.get(url,
                            headers=THE_ONE_API_REQUEST_HEADER)
    return response.json()


def get_quotes_from_specified_character(character_id):
    """Return all quotes from the specified character"""
    url = f"{THE_ONE_API_URL}/character/{character_id}/quote"
    response = requests.get(url,
                            headers=THE_ONE_API_REQUEST_HEADER)
    print(response.json())
    return response.json()
