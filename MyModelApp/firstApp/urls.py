from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('home', views.home),
    path('insert', views.insert),
    path('insertTask', views.insertTask),
    path('show', views.show),
    path('details', views.details),
    path('showTask', views.showTask),
    path('update', views.update),
    path('updateTask', views.updateTask),
    path('delete', views.delete),
    path('deleteTask', views.deleteTask),
# ==============Here student url=====================================
    path('stuhome', views.stuhome),
    path('stuInsert', views.stuInsert),
    path('stuInsertTask', views.stuInsertTask),
    path('studetails', views.studetails),
    path('stuupdate', views.stuupdate),
    path('stuupdateTask', views.stuupdateTask),
    path('studelete', views.studelete),
    path('studeleteTask', views.studeleteTask),

]