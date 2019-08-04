from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ListUsuario.as_view()),
    path('<int:pk>/', views.DetailUsuario.as_view()),
    #path('rest-auth/', include('rest_auth.urls')),  
    path('rest-auth/', include('django_expiring_token.urls')),
]