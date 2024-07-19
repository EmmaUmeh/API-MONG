# api_mong_app/requests/delete_request.py

from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

def handle_delete_request(request):
    logger.info("DELETE request received")
    # Handle DELETE request logic
    return Response(status=status.HTTP_204_NO_CONTENT)
