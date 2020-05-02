from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'posts', PostViewSet, basename='post')
urlpatterns = router.urls
