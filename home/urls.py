
from django.urls import path
from . import views
from .views import StudentAPI

urlpatterns = [

    # single path but make all method in one 
    path('students/', StudentAPI.as_view()),
    # path('', views.home),
    # path('student/', views.student),
    # path('studentUpdate/<id>/', views.studentUpdate),
    # path('studentUpdateWithpatch/<id>/', views.studentUpdateWithpatch),
    # path('deleteStudent/<id>/', views.deleteStudent),
    # path('books/', views.getBooks),
    # path('addBooks/', views.addBooks),
]