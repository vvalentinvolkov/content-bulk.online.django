from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from rest_framework import status
from rest_framework.response import Response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zen.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]


def trigger_error(request):
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        return HttpResponse('sentry-debug', status=status.HTTP_400_BAD_REQUEST)


urlpatterns.append(path('sentry-debug/', trigger_error))
