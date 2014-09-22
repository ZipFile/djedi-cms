from django.views.generic import TemplateView

try:
    from django.conf.urls import patterns, include, url
except ImportError:
    from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
                       url(r'^adm1n/', include(admin.site.urls)))
