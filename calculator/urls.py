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

from django.conf import settings

# from django.views.static import serve
# from django.conf.urls import url

from .views import (
    base_cup_handler,
    get_quote_buyer,
    get_quote_base,
    get_quote_pkg,
    get_quote_items,
    home_handler,
    pack_cost_handler,
    pdf_handler,
    test_handler,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base", base_cup_handler, name="base cup cost calculator"),
    path("getquote_1", get_quote_buyer, name="Generate quote"),
    path("getquote_2", get_quote_base, name="Generate quote"),
    path("getquote_3", get_quote_pkg, name="Generate quote"),
    path("getquote_4", get_quote_items, name="Generate quote"),
    path("", home_handler, name="Calibrate ur data"),
    path("packcost", pack_cost_handler, name="Calculater for Packet Cost"),
    path("topdf", pdf_handler, name="Will create a pdf"),
    path("test", test_handler, name="test ur html here"),
    # url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    # url(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
