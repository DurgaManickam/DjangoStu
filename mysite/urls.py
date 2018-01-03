from django.conf.urls import include, url
from django.contrib import admin
from myblog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('myblog.urls')),
    url(r'^testmodel/',views.test_model,name='testmodel'),
    url(r'^testing/',views.post_form_test,name='testing'),
    url(r'^details_view/', views.details_view,name='details_view'),
    url(r'^testformm/',views.test_form,name='testformm'),
    url(r'^fetch_test/', views.fetch_test,name='fetch_test'),
    url(r'^user_entry', views.user_entry,name='user_entry'),
    url(r'^user_save_data/',views.user_save_data,name='user_save_data'),
    url(r'^user_fetch_alldata/',views.user_fetch_alldata,name='user_fetch_alldata'),
    url(r'^user_data_form/',views.user_data_form,name='user_data_form'),
    url(r'^post_fetch_data', views.post_fetch_data,name='post_fetch_data'),
]
