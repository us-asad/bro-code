from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
	path('', index, name='index'),
	path('about/', about, name='about'),
	path('team/', team, name='team'),
	path('service/', service, name='service'),
	path('postList/', postList, name='postList'),

	path('post/<id>/', postDetail, name= 'postDetail'),
	path('postNew/', postNew, name='postNew'),
    path('update/<id>/', postUpdate, name='post-update'),
    path('delete/<id>/', postDel, name='post-del')



]

