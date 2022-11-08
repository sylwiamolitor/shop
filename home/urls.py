from django.urls import path, include

from .views import index

urlpatterns = [
    path('', index, name='index'),
    # path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
]
