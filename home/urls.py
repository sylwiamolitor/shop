from django.urls import path, include
from .views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    #path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]