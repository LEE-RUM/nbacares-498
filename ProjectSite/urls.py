from django.urls import path
from . import views
from .views import view_post, edit_blog, delete_blog

urlpatterns = [
    path('', views.view_home, name="home"),
    path('events', views.view_events, name="events"),
    path('about', views.view_about, name="about"),
    path('blog/', views.view_blog, name="blog"),
    #path('blog/<str:title>/view/', views.view_post, name="view_post"),
    path('blog/<str:title>/view/', view_post.as_view(), name="view_post"),
    path('blog/add/', views.create_blog, name='create_blog'),
    #path('blog/<str:title>/edit/', views.delete_blog, name="delete_blog"),
    #path('blog/<str:title>/delete/', views.delete_blog, name="delete_blog"),
    path('blog/<str:title>/delete/', delete_blog.as_view(), name="delete_blog"),
    path('blog/<str:title>/edit/', edit_blog.as_view(), name="edit_blog"),
    path('resources', views.view_resources, name="resources"),
    path('login', views.view_login, name="login"),
    path('logout', views.view_logout, name='logout'),
    path('create/<str:pk>', views.create_events, name="create_events"),
    path('update/<str:pk>', views.update_events, name="update_events"),
    path('delete/<str:pk>', views.delete_events, name="delete_events"),
    path('admin-panel', views.view_admin_panel, name="admin_panel"),
    path('admin-organization/<str:pk>', views.view_admin_organzation, name="admin_organization"),
    path('admin-user-creation', views.view_admin_user_creation, name="admin_user_creation"),
    path('organization-settings', views.view_organization_settings, name="organization_settings"),
    path('calendar-template/', views.view_calendar.as_view(), name="calendar"),
]