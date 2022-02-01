from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from core.integrations.defaults import (default_get_characters,
                                        default_get_quotes_by_character)


# Create your views here.
class CharactersView(APIView):
    """API Endpoint to all characters"""

    def get(self, request):

        try:

            return Response(
                default_get_characters(),
                status=status.HTTP_200_OK)

        except Exception as error:
            message = {"message": str(error)}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class QuotesByCharacterView(APIView):
    """API endpoint to get quotes by a character"""

    def get(self, request, character_id):

        try:

            return Response(
                default_get_quotes_by_character(character_id=character_id),
                status=status.HTTP_200_OK)

        except Exception as error:
            message = {"message": str(error)}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
