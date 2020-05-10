from rest_framework import routers
from .views import PostViewSet, UserViewSet, CategoryViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories')
urlpatterns = router.urls
