from django.contrib import admin
from django.urls import path, include, re_path
# from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/workspace/', include('workspace.urls')),
    path('api/board/', include('board.urls')),
    path('api/card/', include('card.urls')),
    path('api/activitylog/', include('activityLog.urls')),
    path('api/users/', include('users.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
