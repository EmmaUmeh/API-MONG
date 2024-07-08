# api_mong/views.py

from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
import requests # type: ignore
import logging

logger = logging.getLogger(__name__)

class RequestView(APIView):
    def get(self, request):
        logger.info("GET request received")
        # Handle GET request logic
        return Response({"message": "GET request received"})

    def post(self, request):
        logger.info("POST request received")
        # Handle POST request logic
        data = request.data
        # Example: Forward POST request to an external API
        try:
            response = requests.post('https://sea-lion-app-ndr9i.ondigitalocean.app/api/v1/product/business/6589b49203bbd7ce1064f7a5', json=data)
            response.raise_for_status()
            logger.info(f"POST request to external API successful: {response.status_code}")
            return Response(response.json(), status=status.HTTP_201_CREATED)
        except requests.RequestException as e:
            logger.error(f"Error making POST request: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        logger.info("PUT request received")
        # Handle PUT request logic
        data = request.data
        return Response(data)

    def delete(self, request):
        logger.info("DELETE request received")
        # Handle DELETE request logic
        return Response(status=status.HTTP_204_NO_CONTENT)
