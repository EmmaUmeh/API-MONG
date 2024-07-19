# api_mong_app/requests/get_request.py

from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)
# data = []

def handle_get_request(request):
    logger.info("GET request received")

    return Response({"message": "GET request received"})
