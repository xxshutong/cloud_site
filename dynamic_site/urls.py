from django.conf.urls import patterns, include, url
from dynamic_site import settings
from dynamic_site.core.controllers import dashboard

from django.contrib import admin

admin.autodiscover()

# Landing
urlpatterns = patterns('dynamic_site.core.controllers.dashboard',
                       # Home page.
                       url(r'^$', dashboard.home, name='home'),
                       url(r'^upload/flash/xml/focus_pics.xml$', dashboard.flash),
                       )

urlpatterns += patterns('',
                        # Examples:
                        # url(r'^$', 'dynamic_site.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),

                        url(r'^admin/', include(admin.site.urls)),
)

