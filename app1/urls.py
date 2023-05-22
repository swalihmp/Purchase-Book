from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.login_p,name='login_p'),
    path('login_form',views.login_form,name='login_form'),
    path('home',views.home,name='home'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('add_short',views.add_short,name='add_short'),
    path('logout_p',views.logout_p,name='logout_p'),
    path('addshort_form',views.addshort_form,name='addshort_form'),
    path('update_sh/<int:id>',views.update_sh,name='update_sh'),
    path('showorder',views.showorder,name='showorder'),
    path('searby_item',views.searby_item,name='searby_item'),
    path('searby_date',views.searby_date,name='searby_date'),
    path('update_sh1/<int:id>',views.update_sh1,name='update_sh1'),
    path('update_exp/<int:id>',views.update_exp,name='update_exp'),
    path('load_data',views.load_data,name='load_data'),
    path('add_exp',views.add_exp,name='add_exp'),
    path('exp_list',views.exp_list,name='exp_list'),
    path('export', views.export_to_excel, name='export_to_excel'),
    path('add_party',views.add_party, name='add_party'),
    path('add_party_form',views.add_party_form,name='add_party_form'),
    
]
