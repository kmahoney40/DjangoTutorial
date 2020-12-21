from django.urls import path
from . import views

app_name = 'water'
urlpatterns = [
    # ex: /water/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /water/runtime
    path('runtime/', views.RuntimeView.as_view(), name='runtime'),
    # ex: /water/3
    path('<int:pk>/', views.EditView.as_view(), name='edit'),
    
    path('<int:runtimes_id>/save', views.save, name='save'),
]
