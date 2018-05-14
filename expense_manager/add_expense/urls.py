from django.conf.urls import url
from . import views

app_name = 'add_expense'

urlpatterns = [
    url(r'^add_expense/', views.add_expense, name='add_expense'),
    url(r'^view_expense/', views.view_expense, name='view_expense'),
    url(r'^get_expense/(?P<pk>\d+)/', views.get_expense, name='get_expense'),
    url(r'^edit_expense/(?P<pk>\d+)/', views.edit_expense, name='edit_expense')

    ]