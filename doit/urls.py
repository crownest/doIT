# Django
from django.contrib import admin
from django.conf.urls import url, include

# Local Django
from doit.views import DocumentationView


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Documentation
    url(r'^docs/$', DocumentationView.as_view(), name='docs'),
    url(r'^docs/(?P<path>.*)$', DocumentationView.as_view(), name='docs'),

    # Api
    url(r'^api/', include('doit.api_urls')),

    # Djoser
    url(r'^api-auth/', include('djoser.urls.authtoken')),
]