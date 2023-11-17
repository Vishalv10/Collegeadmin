from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login,name='login'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('addcourse1',views.addcourse1,name='addcourse1'),
    path('addstudent1',views.addstudent1,name='addstudent1'),
    path('studentdetails',views.studentdetails,name='studentdetails'),
    path('editpage/<int:student_id>',views.editpage,name='editpage'),
    path('update/<int:student_id>/', views.updatestudent, name='updatestudent'),
    path('deletepage/<int:student_id>',views.deletepage,name='deletepage'),
    path('teacher',views.teacher,name='teacher'),
    path('admin1',views.admin1,name='admin1'),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
    path('showteacher',views.showteacher,name='showteacher'),
    path('addteacher',views.addteacher,name='addteacher'),
    path('showteacherdetails',views.showteacherdetails,name='showteacherdetails'),
    path('editteacher/<int:teacher_id>/',views.editteacher, name='editteacher'),
    path('update_teacher/<int:teacher_id>/',views.update_teacher, name='update_teacher'),
    path('showteacherdetails/',views.showteacherdetails, name='show_teacher_details'),
    path('deleteteacher/<int:teacher_id>/',views.deleteteacher, name='deleteteacher'),
    path('teacherdetails',views.teacherdetails,name='teacherdetails'),
    path('teacheradmin',views.teacheradmin,name='teacheradmin'),
    



]
    
    
    
    


    

