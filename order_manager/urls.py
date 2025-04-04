from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # This already includes logout
    path('', include('core.urls')),
    path('accounts/login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='registration/login.html'
    )), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)