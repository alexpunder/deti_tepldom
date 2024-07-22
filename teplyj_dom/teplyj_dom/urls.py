from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

handler404 = 'support_pages.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schooling.urls')),
    path('', include('support_pages.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
