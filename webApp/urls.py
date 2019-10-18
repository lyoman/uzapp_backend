"""webApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include , path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = "UzApp"
admin.site.index_title = 'UzApp Site Administration'

urlpatterns = [
    path('', admin.site.urls),
    path('api/auth/token/', obtain_jwt_token),
    path('api/users/', include(("users.api.urls",'register-api'), namespace='register-api')),
    path('api/users/', include(("users.api.urls",'login-api'), namespace='login-api')),
    path('api/students/', include(("students.api.urls",'register1-api'), namespace='register1-api')),
    path('api/guests/', include(("guests.api.urls",'guests-api'), namespace='guests-api')),
    path('api/students/', include(("students.api.urls",'login1-api'), namespace='login1-api')),
    path('api/news/', include(("news.api.urls",'news-api'), namespace='news-api')),
    path('api/directories/', include(("directories.api.urls",'directories-api'), namespace='directories-api')),
    path('api/ambulance/', include(("ambulance.api.urls",'ambulance-api'), namespace='ambulance-api')),
    path('api/foodordering/', include(("foodordering.api.urls",'foodordering-api'), namespace='foodordering-api')),
    path('api/restaurants/', include(("restaurants.api.urls",'restaurants-api'), namespace='restaurants-api')),
    path('api/laptops_register/', include(("laptopreg.api.urls",'laptopreg-api'), namespace='laptopreg-api')),
    path('api/ResidenceHalls/', include(("ResidenceHalls.api.urls",'ResidenceHalls-api'), namespace='ResidenceHalls-api')),
    path('api/cordinates/', include(("cordinates.api.urls",'cordinates-api'), namespace='cordinates-api')),
    path('api/financial/', include(("financial.api.urls",'financial-api'), namespace='financial-api')),
    path('api/faqs/', include(("faqs.api.urls",'faqs-api'), namespace='faqs-api')),
    path('api/healthtips/', include(("healthtips.api.urls",'healthtips-api'), namespace='healthtips-api')),
    path('api/rules/', include(("rules.api.urls",'rules-api'), namespace='rules-api')),
    path('api/drugs/', include(("drugs.api.urls",'drugs-api'), namespace='drugs-api')),
    path('api/SportsandFacility/', include(("SportsandFacility.api.urls",'SportsandFacility-api'), namespace='SportsandFacility-api')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
