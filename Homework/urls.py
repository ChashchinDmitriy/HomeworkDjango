from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Homework import views

router = routers.DefaultRouter()
router.register(r'reviews_rest', views.ReviewViewSet)
router.register(r'rooms_rest', views.RoomsViewSet)

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:id>/', views.room_detail, name='room_detail'),
    path('rooms/<int:id>/book', views.booking, name='booking'),
    path('rooms/<int:id>/add_review', views.add_review, name='add_review'),
    path('contacts/', views.contacts, name='contacts'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

handler404 = 'Homework.views.handler404'
