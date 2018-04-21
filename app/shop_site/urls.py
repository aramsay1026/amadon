from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.home),
	url(r'^process$', views.process),
	url(r'^checkout$', views.checkout),
	url(r'^thankyou$', views.thankyou),
	url(r'^return_home$', views.return_home)

]
