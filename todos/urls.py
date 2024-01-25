from django.urls import path
from .views import ListTodo ,DetailView

urlpatterns = [
    path('',ListTodo.as_view()),
    path('<int:pk>/',DetailView.as_view())
]
