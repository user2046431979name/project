from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index.as_view(),name='index'),
    path('contact/',contact.as_view(),name='contact'),
]


urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)
