from django.urls import path
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
#from rest_framework.authtoken import views
from todo import views

urlpatterns = [

    url(r'^todo/set-user-perm/$', views.SetUserPermission.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^todo/companies/$', views.CompanyList.as_view()),
    url(r'^todo/desks/$', views.DeskList.as_view()),

    url(r'^todo/(?P<name_company>\w+)/token', views.CustomAuthToken.as_view()),
    url(r'^todo/(?P<name_company>\w+)/desks', views.CompanyDeskList.as_view()),
    url(r'^todo/(?P<name_company>\w+)/(?P<date>[-\w]+)/$', views.CompanyDateList.as_view()),

    #url(r'^todo/(?P<company>\w+)/(?P<idsession>\w+)/', views.CompanyList.as_view()),


    #url(r'^todo/(?P<pk>\w+)/$', views.company_todo),
    #url(r'^todo/done/(?P<pk>\w+)/$', views.todo_done),
    #url(r'^todo/detail/(?P<pk>\w+)/$', views.todo_detail),

    #url(r'^desks/$', views.desk_list),
    #url(r'^desks/detail/$', views.desk_detail),

    #url(r'^users/', views.UserList.as_view()),
    ##url(r'^auth/(?P<pk>\w+)/$', views.auth_user),
    #url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),
    #url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetail.as_view()),
    #url(r'^user/', views.UserDetail.as_view()),
    #url(r'^registration/', views.create_auth),

    #url(r'^test/$', views.TestDetail.as_view()),"""

]

urlpatterns = format_suffix_patterns(urlpatterns)
