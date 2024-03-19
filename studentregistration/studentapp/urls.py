from django.urls import path
from . import views

urlpatterns=[
    path(route='home', view=views.homePageView,name='home'),
    path(route='about', view=views.aboutPageView,name='about'),
    path(route='login', view=views.loginPageView,name='login'),
    path(route='stlogin', view=views.loginPageView,name='stlogin'),
    path(route='adduser', view=views.adduserStudentView,name='adduser'),
    path(route='save', view=views.saveStudentView,name='save'),
    path(route='all', view=views.getALLStudents,name='all'),
    path(route='<int:student_id>/', view=views.singleStudentView,name='getsinglestudent'),
    path(route='delete/<int:student_id>/', view=views.deleteStudentView,name='deletestudent'),
    path(route='update/<int:student_id>/', view=views.updateStudentView,name='updatestudent'),   
]
