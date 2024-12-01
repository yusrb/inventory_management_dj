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

    path('register/' , user_view.register , name="user_register"),
    path('profile/', user_view.profile, name="user_profile"),
    path('', auth_views.LoginView.as_view(template_name="user/login.html", ), name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='user_logout_success'), name='user_logout'),
    path('logout_success/', TemplateView.as_view(template_name='user/logout.html'), name='user_logout_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)