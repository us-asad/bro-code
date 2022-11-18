from django.urls import path

from .views import sendMsg


app_name = 'contact'
urlpatterns = [
	path('', sendMsg, name='send-msg'),
]