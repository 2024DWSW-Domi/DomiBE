from django.urls import path, include, re_path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')), # 메인 페이지
    path('users/', include('users.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
