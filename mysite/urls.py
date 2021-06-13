from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

urlpatterns = [
    # path('', frontpage, name='frontpage'),

    url(r'^', include('apps.core.urls')),
    url(r'^upload_image/', include('apps.upload_image.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
