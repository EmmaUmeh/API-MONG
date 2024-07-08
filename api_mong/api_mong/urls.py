from django.contrib import admin
from django.urls import path
from api_mong_app.views import  RequestView

urlpatterns = [
    path("admin/", admin.site.urls),
     path('request/', RequestView.as_view(), name='request_view'),
    #  path('post/', PostRequest.as_view(), name='post_request'),
    # path('get/', GetRequest.as_view(), name='get_request'),
    # path('put/', PutRequest.as_view(), name='put_request'),
    # path('delete/', DeleteRequest.as_view(), name='delete_request'),
]
