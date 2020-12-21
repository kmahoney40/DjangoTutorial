from django.urls import path
from . import views

app_name = 'water'
urlpatterns = [
    # ex: /water/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /water/runtime
    path('runtime/', views.RuntimeView.as_view(), name='runtime'),
    # ex: /water/runtime/save
    path('runtime/save', views.save, name='save'),
    # ex: /water/3
    path('<int:pk>/', views.EditView.as_view(), name='edit'),
]
