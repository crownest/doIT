# Django
from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^api/', include('doIT.api_urls'))
]
