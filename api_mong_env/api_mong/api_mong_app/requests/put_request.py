# api_mong_app/requests/put_request.py

from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

def handle_put_request(request):
    logger.info("PUT request received")
    # Handle PUT request logic
    data = request.data
    return Response(data)
