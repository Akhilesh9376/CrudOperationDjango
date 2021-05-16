from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('Delete/<int:id>/',views.Delete,name='Delete'),
    path('Update/<int:id>/',views.Update,name='Update')
]
