from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new_tag/', views.new_tag, name='new_tag'),
    url(r'^new_date/', views.new_date, name='new_date'),
    url(r'^get_validity/', views.get_validity, name='get_validity'),
    url(r'^rm_tag/', views.rm_tag, name='rm_tag'),
]