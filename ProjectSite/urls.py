from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import view_post, edit_blog, delete_blog, create_blog, upload_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.view_home, name="home"),
    path('about', views.view_about, name="about"),

    path('resources', views.view_resources, name="resources"),
    path('autosuggest/', views.autosuggest, name="autosuggest"),

    path('upload/', upload_image.as_view(), name="upload_image"),

    path('blog/', views.view_blog, name="blog"),
    path('blog/<str:title>/view/', view_post.as_view(), name="view_post"),
    path('blog/add/', create_blog.as_view(), name='create_blog'),
    path('blog/<str:title>/delete/', delete_blog.as_view(), name="delete_blog"),
    path('blog/<str:title>/edit/', edit_blog.as_view(), name="edit_blog"),
    
    # Authentication
    path('resident-signup/', views.resident_signup, name="resident_signup"),
    path('login/', views.view_login, name="login"),
    path('logout/', views.view_logout, name='logout'),
    path('verify/<str:token>', views.verify),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="ProjectSite/authentication/password_reset/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="ProjectSite/authentication/password_reset/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="ProjectSite/authentication/password_reset/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="ProjectSite/authentication/password_reset/password_reset_complete.html"), name="password_reset_complete"),

    # Resident
    path('resident/profile/', views.resident_profile, name="resident_profile"),
    path('resident/profile/edit', views.resident_profile_edit, name="resident_profile_edit"),

    path('events', views.view_events, name="events"),
    path('create/<str:pk>', views.create_events, name="create_events"),
    path('update/<str:pk>', views.update_events, name="update_events"),
    path('delete/<str:pk>', views.delete_events, name="delete_events"),

    path('calendar-template/', views.view_calendar.as_view(), name="calendar"),
    path('calendar-template/event/', views.calendar_event, name="calendar_event"),
    path('calendar-template/register/', views.register_event, name="register_event"),
    
    path('admin-panel', views.view_admin_panel, name="admin_panel"),
    path('admin-organization/<str:pk>', views.view_admin_organzation, name="admin_organization"),
    path('admin-user-creation', views.view_admin_user_creation, name="admin_user_creation"),
    path('organization-settings', views.view_organization_settings, name="organization_settings"),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)