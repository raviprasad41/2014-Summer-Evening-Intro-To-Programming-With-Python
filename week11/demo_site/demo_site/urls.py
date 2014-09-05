from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='index.html')),
                       url(r'^index.html$', TemplateView.as_view(template_name='index.html')),
                       # Examples:
                       # url(r'^$', 'demo_site.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^list?$', 'demo_app.views.index', name='list'),
                       url(r'^ajax?$', 'demo_app.views.ajax', name='ajax'),
                       url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
