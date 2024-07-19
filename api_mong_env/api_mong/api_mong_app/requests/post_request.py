# api_mong_app/requests/post_request.py

from rest_framework.response import Response
from rest_framework import status
import requests
import logging

logger = logging.getLogger(__name__)

def handle_post_request(request):
    logger.info("POST request received")
    # Handle POST request logic
    data = request.data
    try:
        response = requests.post('', json=data)
        response.raise_for_status()
        logger.info(f"POST request to external API successful: {response.status_code}")
        return Response(response.json(), status=status.HTTP_201_CREATED)
    except requests.RequestException as e:
        logger.warning(f"Error making POST request: {str(e)}")
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
