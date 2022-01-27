from django.http.response import HttpResponse
from django.shortcuts import render
from .utils.base_cup_cost_calculator import base_cup_cost_calculator
from .utils.pack_cost_calculator import pack_cost_calculator
from .utils.to_pdf import topdf
from .utils.getquote_to_pdf import getquote_topdf
from .utils.create_quotation_database import update_database

import json

from .models import ProductDim, Buyer, Quotation


def base_cup_handler(request):
    if request.method == "GET":
        size = ProductDim.objects.all()
        sizelist = []
        for i in size:
            sizelist.append(i.product_name)
        return render(request, "base_cup_cost_calculator.html", {"size": sizelist})

    if request.method == "POST":
        request_body = dict(request.POST)
        size_of_cup = request_body["size_of_cup"][0]
        gsm = int(request_body["gsm"][0])
        paper_rate = int(request_body["paper_rate"][0])
        scrape_rate = int(request_body["scrape_rate"][0])
        margin = int(request_body["margin"][0])

        base_cup_cost = base_cup_cost_calculator(
            size_of_cup, gsm, paper_rate, scrape_rate, margin
        )
        # return HttpResponse(f"Base cup cost of {size_of_cup} ml is {base_cup_cost} INR")
        context = {}
        context["gsm"] = gsm
        context["base_cup_cost"] = base_cup_cost
        context["paper_rate"] = paper_rate
        context["scrape_rate"] = scrape_rate
        context["size_of_cup"] = size_of_cup
        context["margin"] = margin
        # return render(request, "base_cup_cost_calculator.html", context)
        return render(request, "base_cup_cost_calculator.html", context)


def get_quote_buyer(request):
    if request.method == "GET":

        buyer = Buyer.objects.all()
        last_quote_id = Quotation.objects.last()

        buyerlist = []
        for i in buyer:
            buyerlist.append(i.buyer_alias)

        return render(
            request,
            "getquote_select_buyer.html",
            {"buyerlist": buyerlist, "last_quote_id": last_quote_id},
        )
    if request.method == "POST":
        size = ProductDim.objects.all()
        sizelist = []
        for i in size:
            sizelist.append(i.product_name)

        buyer = Buyer.objects.all()
        buyerlist = []
        for i in buyer:
            buyerlist.append(i.buyer_alias)

        request_body = dict(request.POST)
        # print(request_body)

        if request_body["buyer"][0] != "none":

            buyer_info = Buyer.objects.filter(buyer_alias=request_body["buyer"][0])[0]

            context = {
                "Abrv": buyer_info.buyer_alias,
                "CompName": buyer_info.company_name,
                "CompAdd": buyer_info.company_address,
                "BuyerName": buyer_info.buyer_name,
                "BuyerDet": "Cell: "
                + buyer_info.primary_phone_number
                + "\r\n"
                + "Phone: "
                + buyer_info.secondary_phone_number
                + "\r\n"
                + "Email: "
                + buyer_info.email_id,
                "TandC": buyer_info.terms_and_conditions,
            }

        elif request_body["buyer"][0] == "none":
            context = {
                "Abrv": request_body["Abrv"][0],
                "CompName": request_body["CompanyName"][0],
                "CompAdd": request_body["CompanyAdd"][0],
                "BuyerName": request_body["BuyerName"][0],
                "BuyerDet": request_body["Buyerinfo"][0],
                "TandC": request_body["T&C"][0],
            }
            BuyerDet = context["BuyerDet"].split()

            buyer = Buyer(
                buyer_alias=context["Abrv"],
                buyer_name=context["BuyerName"],
                company_name=context["CompName"],
                company_address=context["CompAdd"],
                primary_phone_number=BuyerDet[1],
                secondary_phone_number=BuyerDet[3],
                email_id=BuyerDet[5],
                terms_and_conditions=context["TandC"],
            )
            buyer.save()
        context["Date"] = request_body["Date"][0]
        context["No_quote"] = request_body["noQuote"][0]
        context["size"] = sizelist
        return render(request, "getquote_base_cup_cost.html", context)


def get_quote_base(request):
    if request.method == "GET":
        size = ProductDim.objects.all()
        sizelist = []
        for i in size:
            sizelist.append(i.product_name)
        return render(request, "getquote_base_cup_cost.html", {"size": sizelist})

    if request.method == "POST":

        request_body = dict(request.POST)

        size_of_cup = request_body["size_of_cup"][0]
        gsm = int(request_body["gsm"][0])
        paper_rate = int(request_body["paper_rate"][0])
        scrape_rate = int(request_body["scrape_rate"][0])
        margin = int(request_body["margin"][0])

        base_cup_cost = base_cup_cost_calculator(
            size_of_cup, gsm, paper_rate, scrape_rate, margin
        )
        context = {
            "Date": request_body["Date"][0],
            "No_quote": request_body["noQuote"][0],
            "Abrv": request_body["Abrv"][0],
            "CompName": request_body["CompanyName"][0],
            "CompAdd": request_body["CompanyAdd"][0],
            "BuyerName": request_body["BuyerName"][0],
            "BuyerDet": request_body["Buyerinfo"][0],
            "TandC": request_body["T&C"][0],
            "size_of_cup": size_of_cup,
            "gsm": gsm,
            "paper_rate": paper_rate,
            "scrape_rate": scrape_rate,
            "margin": margin,
            "base_cup_cost": base_cup_cost,
        }
        if request.method == "POST" and "Calculate" in request.POST:
            return render(request, "getquote_base_cup_cost.html", context)
        if request.method == "POST" and "Next" in request.POST:
            return render(request, "getquote_pack_cost.html", context)


def get_quote_pkg(request):
    if request.method == "GET":
        return render(request, "getquote_pack_cost.html")

    if request.method == "POST":
        request_body = dict(request.POST)
        print("request_body=>>>", request_body)

        context = {
            "Date": request_body["Date"][0],
            "No_quote": request_body["noQuote"][0],
            "Abrv": request_body["Abrv"][0],
            "CompName": request_body["CompanyName"][0],
            "CompAdd": request_body["CompanyAdd"][0],
            "BuyerName": request_body["BuyerName"][0],
            "BuyerDet": request_body["Buyerinfo"][0],
            "TandC": request_body["T&C"][0],
            "size_of_cup": request_body["size_of_cup"][0],
            "gsm": request_body["gsm"][0],
            "paper_rate": request_body["paper_rate"][0],
            "scrape_rate": request_body["scrape_rate"][0],
            "margin": request_body["margin"][0],
            "base_cup_cost": float(request_body["CostperCup"][0]),
            "CupsperSKU": int(request_body["CupsperSKU"][0]),
            "SKUperMC": int(request_body["SKUperMC"][0]),
            "SKUperConatiner": int(request_body["CupsperSKU"][0])
            * int(request_body["SKUperMC"][0]),
            "CostPrintColorperCup": float(request_body["PrintingCost"][0]),
            "LabelCost": float(request_body["LabelCost"][0]),
            "PolyCost": float(request_body["PolyCost"][0]),
            "MCCost": float(request_body["MCCost"][0]),
            "Freight": float(request_body["Freight"][0]),
            "BoxsPerContainer": int(request_body["BoxsPerContainer"][0]),
            "DollorRate": float(request_body["DollorRate"][0]),
            "AddCostperSKU": float(request_body["AddCostperSKU"][0]),
            "size_of_cup": request_body["size_of_cup"][0],
        }
        (
            MCcostinINR,
            MCcostinDollor,
            SKUcostinINR,
            SKUcostinDollor,
        ) = pack_cost_calculator(
            BaseCostperCup=float(request_body["CostperCup"][0]),
            CupsperSKU=int(request_body["CupsperSKU"][0]),
            SKUperMC=int(request_body["SKUperMC"][0]),
            CostPrintColorperCup=float(request_body["PrintingCost"][0]),
            LabelCost=float(request_body["LabelCost"][0]),
            PolyCost=float(request_body["PolyCost"][0]),
            MCCost=float(request_body["MCCost"][0]),
            Freight=float(request_body["Freight"][0]),
            BoxsPerContainer=float(request_body["BoxsPerContainer"][0]),
            DollorRate=float(request_body["DollorRate"][0]),
            AddCostperSKU=float(request_body["AddCostperSKU"][0]),
        )

        context["SKUcostinDollor"] = SKUcostinDollor
        context["SKUcostinINR"] = SKUcostinINR
        context["MCcostinDollor"] = MCcostinDollor
        context["MCcostinINR"] = MCcostinINR

        size = ProductDim.objects.all()

        sizelist = []
        for i in size:
            sizelist.append(i.product_name)
        context["size"] = sizelist

        if request.method == "POST" and "Calculate" in request.POST:
            return render(request, "getquote_pack_cost.html", context)
        if request.method == "POST" and "Next" in request.POST:
            return render(request, "getquote_name_item.html", context)


def get_quote_items(request):
    if request.method == "GET":
        size = ProductDim.objects.all()

        sizelist = []
        for i in size:
            sizelist.append(i.product_name)

        return render(request, "getquote_name_item.html", {"size": sizelist})

    if request.method == "POST":
        request_body = dict(request.POST)

        product_info = ProductDim.objects.filter(
            product_name=request_body["size_of_cup1"][0]
        )[0]

        context = {
            "Date": request_body["Date"][0],
            "No_quote": request_body["noQuote"][0],
            "Abrv": request_body["Abrv"][0],
            "CompName": request_body["CompanyName"][0],
            "CompAdd": request_body["CompanyAdd"][0],
            "BuyerName": request_body["BuyerName"][0],
            "BuyerDet": request_body["Buyerinfo"][0],
            "TandC": request_body["T&C"][0],
            "size_of_cup": request_body["size_of_cup"][0],
            "gsm": request_body["gsm"][0],
            "paper_rate": request_body["paper_rate"][0],
            "scrape_rate": request_body["scrape_rate"][0],
            "margin": request_body["margin"][0],
            "base_cup_cost": request_body["base_cup_cost"][0],
            "CupsperSKU": request_body["CupsperSKU"][0],
            "SKUperMC": int(request_body["SKUperMC"][0]),
            "SKUperConatiner": int(request_body["CupsperSKU"][0])
            * int(request_body["SKUperMC"][0]),
            "CostPrintColorperCup": request_body["PrintingCost"][0],
            "LabelCost": request_body["LabelCost"][0],
            "PolyCost": request_body["PolyCost"][0],
            "MCCost": request_body["MCCost"][0],
            "Freight": request_body["Freight"][0],
            "BoxsPerContainer": request_body["BoxsPerContainer"][0],
            "DollorRate": request_body["DollorRate"][0],
            "AddCostperSKU": request_body["AddCostperSKU"][0],
            "SKUcostinDollor": request_body["SKUcostinDollor"][0],
            "productName": request_body["productName1"][0],
            "Amount": request_body["Amount1"][0],
            "MCSize": request_body["MCSize1"][0],
            "CBMperMC1": request_body["CBMperMC1"][0],
            "CBMper40HQ1": request_body["CBMper40HQ1"][0],
            "DecSub": request_body["DecSub1"][0],
            "TopDia": product_info.top_dia,
            "BottomDia": product_info.bottom_dia,
            "Height": product_info.height,
            "created_by": request_body["created_by"][0],
        }
        print("CostPrintColorperCup=", context["CostPrintColorperCup"])
        print("PrintingCost=", request_body["PrintingCost"][0])
        PDF = getquote_topdf(
            Date=context["Date"],
            No_quote=context["No_quote"],
            CompName=context["CompName"],
            CompAdd=context["CompAdd"],
            BuyerName=context["BuyerName"],
            BuyerDet=context["BuyerDet"],
            TandC=context["TandC"],
            productName=context["productName"],
            NoPacketinConatiner=str(context["SKUperConatiner"]),
            Rate=context["SKUcostinDollor"],
            Amount=context["Amount"],
            NoBoxinConatiner=context["BoxsPerContainer"],
            BoxSize=context["MCSize"],
            CBMperBox=context["CBMperMC1"],
            CBMper40HQ=context["CBMper40HQ1"],
            DecSub=context["DecSub"],
            TopDia=context["TopDia"],
            BottomDia=context["BottomDia"],
            Height=context["Height"],
        )

        filename = "Q-" + request_body["noQuote"][0] + " " + context["CompName"]
        PDF.output(f"quote/{filename}.pdf")
        update_database(context)
        context["Path"] = f"quote/{filename}.pdf"

        return render(request, "getquote_name_item.html", context)


def home_handler(request):
    if request.method == "GET":
        return render(request, "home.html")

    if request.method == "POST":
        return render(request, "home.html")


def pack_cost_handler(request):
    if request.method == "GET":
        return render(request, "pack_cost_calculator.html")

    if request.method == "POST":
        request_body = dict(request.POST)
        context = {}
        context["base_cup_cost"] = float(request_body["CostperCup"][0])
        context["CupsperSKU"] = int(request_body["CupsperSKU"][0])
        context["SKUperMC"] = int(request_body["SKUperMC"][0])
        context["CostPrintColorperCup"] = float(request_body["PrintingCost"][0])
        context["LabelCost"] = float(request_body["LabelCost"][0])
        context["PolyCost"] = float(request_body["PolyCost"][0])
        context["MCCost"] = float(request_body["MCCost"][0])
        context["Freight"] = float(request_body["Freight"][0])
        context["BoxsPerContainer"] = float(request_body["BoxsPerContainer"][0])
        context["DollorRate"] = float(request_body["DollorRate"][0])
        context["AddCostperSKU"] = float(request_body["AddCostperSKU"][0])
        (
            MCcostinINR,
            MCcostinDollor,
            SKUcostinINR,
            SKUcostinDollor,
        ) = pack_cost_calculator(
            BaseCostperCup=float(request_body["CostperCup"][0]),
            CupsperSKU=int(request_body["CupsperSKU"][0]),
            SKUperMC=int(request_body["SKUperMC"][0]),
            CostPrintColorperCup=float(request_body["PrintingCost"][0]),
            LabelCost=float(request_body["LabelCost"][0]),
            PolyCost=float(request_body["PolyCost"][0]),
            MCCost=float(request_body["MCCost"][0]),
            Freight=float(request_body["Freight"][0]),
            BoxsPerContainer=float(request_body["BoxsPerContainer"][0]),
            DollorRate=float(request_body["DollorRate"][0]),
            AddCostperSKU=float(request_body["AddCostperSKU"][0]),
        )

        context["SKUcostinDollor"] = SKUcostinDollor
        context["SKUcostinINR"] = SKUcostinINR
        context["MCcostinDollor"] = MCcostinDollor
        context["MCcostinINR"] = MCcostinINR
        # return HttpResponse(
        #     f"""Cost of Master Carton {MCcostinINR} INR & ${MCcostinDollor} Dollor <br/>
        #     Cost of SKU {SKUcostinINR} INR & ${SKUcostinDollor} Dollor"""
        # )
        return render(request, "pack_cost_calculator.html", context)


def pdf_handler(request):
    if request.method == "GET":
        size = ProductDim.objects.all()
        buyer = Buyer.objects.all()
        last_quote_id = Quotation.objects.last()

        buyerlist = []
        for i in buyer:
            buyerlist.append(i.buyer_alias)

        sizelist = []
        for i in size:
            sizelist.append(i.product_name)

        return render(
            request,
            "to_pdf.html",
            {"size": sizelist, "buyerlist": buyerlist, "last_quote_id": last_quote_id},
        )

    if request.method == "POST":
        request_body = dict(request.POST)

        if request_body["buyer"][0] != "none":

            buyer_info = Buyer.objects.filter(buyer_alias=request_body["buyer"][0])[0]

            context = {
                "Abrv": buyer_info.buyer_alias,
                "CompName": buyer_info.company_name,
                "CompAdd": buyer_info.company_address,
                "BuyerName": buyer_info.buyer_name,
                "BuyerDet": "Cell: "
                + buyer_info.primary_phone_number
                + "\r\n"
                + "Phone: "
                + buyer_info.secondary_phone_number
                + "\r\n"
                + "Email: "
                + buyer_info.email_id,
                "TandC": buyer_info.terms_and_conditions,
            }

        elif request_body["buyer"][0] == "none":
            context = {
                "Abrv": request_body["Abrv"][0],
                "CompName": request_body["CompanyName"][0],
                "CompAdd": request_body["CompanyAdd"][0],
                "BuyerName": request_body["BuyerName"][0],
                "BuyerDet": request_body["Buyerinfo"][0],
                "TandC": request_body["T&C"][0],
            }
            BuyerDet = context["BuyerDet"].split()

            buyer = Buyer(
                buyer_alias=context["Abrv"],
                buyer_name=context["BuyerName"],
                company_name=context["CompName"],
                company_address=context["CompAdd"],
                primary_phone_number=BuyerDet[1],
                secondary_phone_number=BuyerDet[3],
                email_id=BuyerDet[5],
                terms_and_conditions=context["TandC"],
            )
            buyer.save()

        data = []
        for i in [
            "size_of_cup",
            "productName",
            "NoSKUinConatiner",
            "Rate",
            "Amount",
            "NoMCinConatiner",
            "MCSize",
            "CBMperMC",
            "CBMper40HQ",
            "DecSub",
            "top_dia",
            "bottom_dia",
            "height",
        ]:
            col = []
            for j in range(3):
                try:
                    product_info = ProductDim.objects.filter(
                        product_name=request_body[f"size_of_cup{j+1}"][0]
                    )[0]
                    if i == "top_dia":
                        col.append(product_info.top_dia)
                    elif i == "bottom_dia":
                        col.append(product_info.bottom_dia)
                    elif i == "height":
                        col.append(product_info.height)

                    else:
                        col.append(request_body[f"{i}{j+1}"][0])
                except Exception as e:
                    print("Exception occurred due to :  ", e)
            data.append(col)

        print(data)
        PDF = topdf(
            No_quote=request_body["noQuote"][0],
            Date=request_body["Date"][0],
            CompName=context["CompName"],
            CompAdd=context["CompAdd"],
            BuyerName=context["BuyerName"],
            BuyerDet=context["BuyerDet"],
            TandC=context["TandC"],
            productName=data[1],
            NoPacketinConatiner=data[2],
            Rate=data[3],
            Amount=data[4],
            NoBoxinConatiner=data[5],
            BoxSize=data[6],
            CBMperBox=data[7],
            CBMper40HQ=data[8],
            DecSub=data[9],
            TopDia=data[10],
            BottomDia=data[11],
            Height=data[12],
            Item2="Item2" in request_body.keys(),
            Item3="Item3" in request_body.keys(),
        )

        filename = "Q-" + request_body["noQuote"][0] + " " + context["CompName"]
        PDF.output(f"quote/{filename}.pdf")
        return render(request, "to_pdf.html", {"Generated": f"quote/{filename}.pdf"})


def test_handler(request):

    if request.method == "GET":

        return render(request, "test.html")

    if request.method == "POST":
        request_body = dict(request.POST)
        buyer_alias = request_body["buyer_alias"][0]
        result = {}
        buyerdata = Buyer.objects.all()
        for i in buyerdata:
            if i.buyer_alias == buyer_alias:
                # result["buyer_alias"] = str(i.buyer_alias)
                # result["buyer_name"] = str(i.buyer_name)
                # result["company_name"] = str(i.company_name)
                # result["company_address"] = str(i.company_address)
                # result["terms_and_conditions"] = str(i.terms_and_conditions)
                print(type(result))
                result = "Found!!!"
                print(i.buyer_alias)
                break
            else:
                result = "Not Avalable!!!"
        return render(request, "test.html", {"result": result})
