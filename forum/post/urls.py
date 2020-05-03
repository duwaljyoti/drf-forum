from rest_framework import routers
from .views import PostViewSet, UserViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls
