from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name= 'site'
urlpatterns = [
    path(r'', views.home, name='home'),#path for home page
    path(r'create_post/', views.create_post, name='create_post'),#path for create post view
    path(r'(?P<slug>[\w-]+)/', views.post_body, name= 'details'),# create slug for each post link in order to rediret user to a particular post details
    path(r'feedback/', views.feedback, name='feedback'),#path for feedback
    path(r'(?P<slug>[\w-]+)/edit/', views.editpost, name = 'edit'), #appending editpost to the end of post detail slug url will direct to editpost view
    path(r'(?P<slug>[\w-]+)/delete/', views.deletepost, name = 'delete'),
    #path(r'(?P<slug>[\w-]+)/comment/', views.comment, name = 'comment'),
    #path(r'(?P<slug>[\w-]+)/reply/', views.reply, name = 'reply'),
    #path(r'search/', views.search, name = 'search')


]
urlpatterns += staticfiles_urlpatterns()    #append url pattern to ojur staticfiles
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
