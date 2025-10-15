from django.urls import path
from .views import ToDoListCreate, ToDoDetail, ToDoComplete

urlpatterns = [
    path('', ToDoListCreate.as_view(), name='api_todolist_list'),
    path('<int:pk>/', ToDoDetail.as_view(), name='api_todolist_detail'),
    path('<int:pk>/complete/', ToDoComplete.as_view(), name='api_todolist_complete'),
]