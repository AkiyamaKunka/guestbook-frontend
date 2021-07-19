from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('note-create', views.NoteCreateView)
router.register('note-update', views.NoteUpdateView, basename='note-update')
router.register('user-create', views.UserCreateView, basename='user-create')
# if you use the default method to approach the data, you do not use the basename
# otherwise, use basename attribute
urlpatterns = [
    path('', include(router.urls)),
]
