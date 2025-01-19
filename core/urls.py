from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Simple view for the root URL (to avoid 404)
def home_view(request):
    return HttpResponse("Welcome to the Task Management System!")

urlpatterns = [
    path('', home_view),  # Add the root URL pattern
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Existing API routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
