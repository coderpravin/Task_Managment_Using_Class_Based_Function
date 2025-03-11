
from django.urls import path
from .import views
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete
urlpatterns = [
    path('', TaskList.as_view(), name='TaskList'),
    path('TaskCreate', TaskCreate.as_view(), name='TaskCreate'),
    path('TaskUpdate/<int:pk>', TaskUpdate.as_view(), name='TaskUpdate'),
    path('TaskDelete/<int:pk>', TaskDelete.as_view(), name='TaskDelete'),
    path('home', views.homeLogin, name='homeLogin'),
    path('userLogin', views.userLogin, name='userLogin'),
]
