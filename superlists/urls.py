from django.conf.urls import include, url

from todolists import views as list_views
from todolists import urls as list_urls

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^todolists/', include(list_urls))
]
