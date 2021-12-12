"""calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from .views import (
    base_cup_handler,
    data_calib_handler,
    export_quote_handler,
    home_handler,
    pack_cost_handler,
    pdf_handler,
    test_handler,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base", base_cup_handler, name="base cup cost calculator"),
    path("calib", data_calib_handler, name="Calibrate ur data"),
    path("exportquote", export_quote_handler, name="Generate quote for Export"),
    path("", home_handler, name="Calibrate ur data"),
    path("packcost", pack_cost_handler, name="Calculater for Packet Cost"),
    path("topdf", pdf_handler, name="Will create a pdf"),
    path("test", test_handler, name="test ur html here"),
]
