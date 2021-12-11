from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bloger.urls', namespace='bloger')),
    path('api/', include('blog_api.urls', namespace='blog_api')),
    path('api/fabbi/', include('blogfabbi.urls',namespace='blogfabbi')),
    path('api/user/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/blog/', include('blog_it.urls'), name= 'blog_it'),
    path('summernote/', include('django_summernote.urls')),
    path('api/contacts/', include('contacts.urls')),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
