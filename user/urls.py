from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from security import views as securityViews
from administration import views as adminViews
from user import views as userViews  # <- Aquí están tus vistas de login, registrar, etc.
from user.views import custom_logout
from . import views
from administration.views import computers_view, registrar_computadora

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alerts/', adminViews.alerts, name='alerts'),
    path('api/alerts/', adminViews.alertas_json, name='alertas_json'),
    path('update/alerts/', adminViews.update_alert, name='update_alert'),
    path('personnel', userViews.personnel, name='personnel'),
    path('registrar/', userViews.registrar_usuario, name='registrar_usuario'),
    path('login/', userViews.login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('administrar-usuarios/', userViews.admin_users_view, name='admin_users'),
    path('administrar-usuarios/eliminar/<int:user_id>/', userViews.delete_user_view, name='delete_user'),
    path('computadoras/', computers_view, name='computadoras'),
    path('computadoras/registrar/', adminViews.registrar_computadora, name='registrar_computadora'),
    path('computadora/eliminar/<int:computadora_id>/', adminViews.eliminar_computadora, name='eliminar_computadora'),
    path('update/photos/', adminViews.update_photos, name='update_photos'),
   
    # Manejo de archivos multimedia
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('personnel', userViews.personnel, name='personnel'),
    path('about/', views.about, name='about'),
     path('', views.index, name='index'),  # Redirecciona según el estado de sesión
    path('home/', userViews.home, name='home'),
    path('landing/', views.landing_page, name='landing'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Extra para debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
