from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'awards', views.AwardViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'publisherlocations', views.PublisherLocationViewSet)
router.register(r'bookeditions', views.BookEditionViewSet)
router.register(r'libraries', views.LibraryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]