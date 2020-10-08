from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('nimda/', admin.site.urls),
    path('', include('blog.urls')),
    path('users/', include('users.urls')),
    path('sentry-debug/', trigger_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for images in development


