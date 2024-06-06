from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import dashboard_view, home_view, register, login

urlpatterns = [
    path('', home_view, name='home'),
    path('dashboard', dashboard_view, name='dashboard'),
    path('login', login, name='login'),
    path('register', register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




