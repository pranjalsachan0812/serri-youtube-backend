from django.urls import path, include

urlpatterns = [
    path('api/', include('videos.urls')),  # include the app urls
]
