# urls.py (of your project or app)

from django.urls import path
from .views import send_test_email  # Adjust the import based on your project structure

urlpatterns = [
    path('send-email/', send_test_email, name='send_email'),
]
