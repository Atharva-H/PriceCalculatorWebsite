from django.http import FileResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from .utils.handler_base_cup import base_cup_handler_get, base_cup_handler_post
from .utils.handler_pack_cost import pack_cost_handler_get, pack_cost_handler_post
from .utils.handler_pdf import pdf_handler_get, pdf_handler_post
from .utils.handler_test import test_handler_get, test_handler_post
from .utils.handler_quote_buyer import quote_buyer_get, quote_buyer_post
from .utils.handler_quote_base import quote_base_get, quote_base_post
from .utils.handler_quote_pkg import quote_pkg_get, quote_pkg_post
from .utils.handler_quote_nameitem import (
    quote_nameitem_get,
    quote_nameitem_post,
    quote_nameitem_generate,
)
from .utils.database_itemdetails import get_data
from rich import print


def home_handler(request):
    if request.method == "GET":
        return render(request, "home.html")

    if request.method == "POST":
        return render(request, "home.html")


def base_cup_handler(request):
    if request.method == "GET":
        sizelist = base_cup_handler_get()
        return render(request, "base_cup_cost_calculator.html", {"size": sizelist})

    if request.method == "POST":
        request_body = dict(request.POST)

        # return HttpResponse(f"Base cup cost of {size_of_cup} ml is {base_cup_cost} INR")
        context = base_cup_handler_post(request_body)

        # return render(request, "base_cup_cost_calculator.html", context)
        return render(request, "base_cup_cost_calculator.html", context)


def pack_cost_handler(request):
    if request.method == "GET":
        sizelist = pack_cost_handler_get()
        return render(request, "pack_cost_calculator.html", {"size": sizelist})

    if request.method == "POST":
        request_body = dict(request.POST)
        context = pack_cost_handler_post(request_body)
        # return HttpResponse(
        #     f"""Cost of Master Carton {MCcostinINR} INR & ${MCcostinDollor} Dollor <br/>
        #     Cost of SKU {SKUcostinINR} INR & ${SKUcostinDollor} Dollor"""
        # )
        return render(request, "pack_cost_calculator.html", context)


def pdf_handler(request):
    if request.method == "GET":
        (sizelist, last_quote_id, buyerlist) = pdf_handler_get()

        return render(
            request,
            "to_pdf.html",
            {"size": sizelist, "buyerlist": buyerlist, "last_quote_id": last_quote_id},
        )

    if request.method == "POST":
        request_body = dict(request.POST)
        filename = pdf_handler_post(request_body)
        return render(request, "to_pdf.html", {"Generated": f"quote/{filename}.pdf"})


def get_quote_buyer(request):
    if request.method == "GET":
        last_data = quote_buyer_get()
        return render(request, "getquote_select_buyer.html", last_data)

    if request.method == "POST":
        request_body = dict(request.POST)
        context = quote_buyer_post(request_body)
        return render(request, "getquote_base_cup_cost.html", context)


def get_quote_base(request):
    if request.method == "GET":
        sizelist = quote_base_get()
        return render(request, "getquote_base_cup_cost.html", {"size": sizelist})

    if request.method == "POST":

        request_body = dict(request.POST)

        context = quote_base_post(request_body)
        if request.method == "POST" and "Calculate" in request.POST:
            return render(request, "getquote_base_cup_cost.html", context)
        if request.method == "POST" and "Next" in request.POST:
            return render(request, "getquote_pack_cost.html", context)


def get_quote_pkg(request):
    if request.method == "GET":
        context = quote_pkg_get()
        return render(request, "getquote_pack_cost.html", context)

    if request.method == "POST":
        request_body = dict(request.POST)

        context = quote_pkg_post(request_body)

        if request.method == "POST" and "Calculate" in request.POST:
            return render(request, "getquote_pack_cost.html", context)
        if (
            request.method == "POST"
            and "Next" in request.POST
            and request_body["quote_type"][0] == "quote_type_mc"
        ):
            return render(request, "getquote_name_item_mc.html", context)
        if (
            request.method == "POST"
            and "Next" in request.POST
            and request_body["quote_type"][0] == "quote_type_sku"
        ):
            return render(request, "getquote_name_item_sku.html", context)


def get_quote_items(request):
    if request.method == "GET":
        (userlist, sizelist) = quote_nameitem_get()

        return render(
            request, "getquote_name_item.html", {"size": sizelist, "user": userlist}
        )

    if request.method == "POST":
        request_body = dict(request.POST)
        context = quote_nameitem_post(request_body)
        if request.method == "POST" and "Generate" in request.POST:
            context = quote_nameitem_generate(request_body)
            return FileResponse(open(context["Path"], "rb"))
            # return render(request, "location.html", context)
        # if request.method == "POST" and "Add Item" in request.POST:
        else:
            return render(request, "getquote_base_cup_cost.html", context)


def test_handler(request):

    if request.method == "GET":
        userlist = test_handler_get()
        get_data(item_count=3)

        return render(request, "test.html", {"user": userlist})

    if request.method == "POST":
        request_body = dict(request.POST)
        get_data(item_count=3)

        return render(request, "test.html", {"user": userlist})
