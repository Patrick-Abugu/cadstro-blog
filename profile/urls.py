from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name= 'profile'
urlpatterns = [
    #path('signup/', views.signup.as_view(), name= 'signup'),
    path('signup/', views.signup, name= 'signup'),
    path(r'login/', views.login_view, name='login'),
    path(r'logout/', views.logout_view, name= 'logout'),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
