from django.conf.urls.defaults import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SoftwareStack.views.home', name='home'),
    # url(r'^SoftwareStack/', include('SoftwareStack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^[/]?$', 'main.views.home'),
    url('^profile', 'main.views.profile'),
    url('^projects', 'main.views.projects'),
    url('^blog', 'main.views.blog'),
    url('^contact', 'main.views.contact'),
    url('^handle_json_req', 'main.views.handle_json_req'),
    url('^login', 'main.views.login'),
    url('^teleport', 'main.views.teleport'),
#    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root': 'frontend/'}),
                       
)