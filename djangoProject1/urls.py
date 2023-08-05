"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from studentssms import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('studentssms/', include('studentssms.urls')),
    path('admin/', admin.site.urls),
]




# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('studentssms/', include('studentssms.urls')),
# # ]
# #         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]
# #
# WSGI_APPLICATION = "djangoProject1.wsgi.application"
#
#
# # Database
# # https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#
