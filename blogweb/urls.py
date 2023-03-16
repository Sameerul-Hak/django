
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
     path('createblog/',views.createblog),
     path('viewblogs/',views.viewblogs),
     path("projects/",views.projects_save),    
     path("blog/<int:id>/",views.productdetail,name='product_detail'),
     path('viewprojects/',views.login_view),
]