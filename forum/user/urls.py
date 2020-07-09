from .views import test_view
from django.urls import path

urlpatterns = [
    path('test-view', test_view, name='something')
]
