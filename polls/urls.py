from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.get_token, name="auth"),
    path('auth/validate', views.validate_token, name="auth-validate"),
    path('', include(router.urls)),
]

urlpatterns += router.urls