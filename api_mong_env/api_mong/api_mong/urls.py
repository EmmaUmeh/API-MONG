from django.contrib import admin
from django.urls import path
from api_mong_app.views import RequestView

urlpatterns = [
    path("admin/", admin.site.urls),
     path('request/', RequestView.as_view(), name='request'),
]
