from rest_framework import routers
from .views import PostViewSet, UserViewSet, CategoryViewSet, ClassBasedView, function_based_view, post_with_replies,\
    post_with_replies_using_join
from django.urls import path

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls

urlpatterns += [
    path('class-based-view', ClassBasedView.as_view()),
    path('function-based-view', function_based_view, name='function-based-view'),
    path('post-with-replies-using-subquery', post_with_replies, name='post-with-replies'),
    path('post-with-replies-using-join', post_with_replies_using_join, name='post-with-replies'),
]

