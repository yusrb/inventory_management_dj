from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from user import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('dashboard.urls' , 'dashboard'), namespace="dashboard")),

    path('profile/', user_view.profile, name="user_profile"),
    path('profile/update', user_view.profile_update, name="user_profile_update"),

    path('register/' , user_view.register , name="user_register"),
    path('', auth_views.LoginView.as_view(template_name="user/login.html", ), name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='user_logout_success'), name='user_logout'),
    path('logout_success/', TemplateView.as_view(template_name='user/logout.html'), name='user_logout_success'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"), name="user_password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>' , auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"), name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)