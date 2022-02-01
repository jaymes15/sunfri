from unittest.mock import patch

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

CHARACTERS_URL = reverse("characters:characters")


def get_quotes_by_character_url(character_id):

    return reverse(
        'characters:quotes_by_character', args=[character_id])


class TestCharactersView(TestCase):

    def setUp(self):
        self.client = APIClient()

    @patch('characters.views.default_get_characters')
    def test_get(self, mock_default_get_characters):
        """Test GET"""

        mock_default_get_characters.return_value = {"id": "344455"}

        response = self.client.get(CHARACTERS_URL)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    @patch('characters.views.default_get_characters')
    def test_exception_case(self, mock_default_get_characters):
        """Test GET request exception case"""

        mock_default_get_characters.side_effect = Exception("BAD REQUEST")

        response = self.client.get(CHARACTERS_URL)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestQuotesByCharacterView(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.id = "344455"

    @patch('characters.views.default_get_quotes_by_character')
    def test_get(self, mock_default_get_quotes_by_character):
        """Test GET"""

        mock_default_get_quotes_by_character.return_value = {"id": self.id}

        response = self.client.get(get_quotes_by_character_url(self.id))

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    @patch('characters.views.default_get_quotes_by_character')
    def test_exception_case(self, mock_default_get_quotes_by_character):
        """Test GET request exception case"""

        mock_default_get_quotes_by_character.side_effect = Exception(
            "BAD REQUEST")

        response = self.client.get(get_quotes_by_character_url(self.id))

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
