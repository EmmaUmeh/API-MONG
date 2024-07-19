# api_mong_app/views.py

from rest_framework.views import APIView # type: ignore
from api_mong_app.requests.get_request import handle_get_request
from api_mong_app.requests.post_request import handle_post_request
from api_mong_app.requests.put_request import handle_put_request
from api_mong_app.requests.delete_request import handle_delete_request

class RequestView(APIView):
    def get(self, request):
        return handle_get_request(request)

    def post(self, request):
        return handle_post_request(request)

    def put(self, request):
        return handle_put_request(request)

    def delete(self, request):
        return handle_delete_request(request)
