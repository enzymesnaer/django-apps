from django.urls import path
from . import views


app_name = 'docviewercore'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path("logout/", views.logout_request, name="logout"),
    path('filesuploaded/', views.filesuploaded_view, name="filesuploaded"),
    path('viewfile/', views.file_viewer, name="fileviewer"),
    path('download/', views.download, name="download"),
]