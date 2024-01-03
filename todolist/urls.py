from . import views
from django.urls import path

urlpatterns = [
    path('addtask/', views.addtask,name='addtask'),
    path("remTask",views.remTask,name='remTask'),
]
