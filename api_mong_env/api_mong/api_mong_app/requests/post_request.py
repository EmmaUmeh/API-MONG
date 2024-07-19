# api_mong_app/requests/post_request.py

from rest_framework.response import Response
from rest_framework import status
import requests
import logging

logger = logging.getLogger(__name__)
url = "https://sea-lion-app-ndr9i.ondigitalocean.app/api/v1/api/v1/ordered/"

def isAuthenticated(url):
    try:

        response = requests.get(url, timeout=10)
        
        # Check if the response status code indicates authentication is needed
        if response.status_code in [401, 403, 405]:
            logger.warning("URL requires authentication: Status code %d", response.status_code)
            return True
        else:
            logger.info("URL is accessible without authentication: Status code %d", response.status_code)
            return False
    except requests.RequestException as e:
        logger.error("Error checking URL authentication: %s", str(e))
        return False
    

def handle_post_request(request):
    logger.info("POST request received")
    # Handle POST request logic
    data = request.data
    try:
        if isAuthenticated(url):
            logger.warning("URL is protected. Authentication is required.")
            return Response({"error": "URL is protected. Authentication is required."}, status=status.HTTP_403_FORBIDDEN)
        else:
            response = requests.post(url, json=data)
            response.raise_for_status()
            logger.info(f"POST request to external API successful: {response.status_code}")
            return Response(response.json(), status=status.HTTP_201_CREATED)
    except requests.RequestException as e:
        logger.warning(f"Error making POST request: {str(e)}")
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)