from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'tigen_project.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     url(r'^time_engine/', include('time_engine.urls')),
#     url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = [
    # Examples:
    # url(r'^$', 'tigen_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^time_engine/', include('time_engine.urls')),
    url(r'^admin/', include(admin.site.urls)),
]