from django.http.response import HttpResponse
from django.shortcuts import render
from .utils.base_cup_cost_calculator import base_cup_cost_calculator
from .utils.calibrate import calibrate
from .utils.pack_cost_calculator import pack_cost_calculator
from .utils.to_pdf import topdf

import json


def base_cup_handler(request):
    if request.method == "GET":
        return render(request, "base_cup_cost_calculator.html")

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
        return render(request, "base_cup_cost_calculator.html", context)


def data_calib_handler(request):
    if request.method == "GET":
        with open("calculator/utils/calibrate_data/base_cup_data.json") as f:
            RM_Data = json.load(f)
        context = {}
        for i in RM_Data.keys():
            for j in RM_Data[i].keys():
                context[f"{i}{j[0]}{j[1]}"] = RM_Data[i][j]

        return render(request, "calibrate.html", context)

    if request.method == "POST":
        request_body = dict(request.POST)
        final_data = calibrate(request_body)
        with open("calculator/utils/calibrate_data/base_cup_data.json", "w") as fp:
            json.dump(final_data, fp)
        return HttpResponse("Data Calibrated!!!!")


def export_quote_handler(request):
    if request.method == "GET":
        return HttpResponse("Export Calculator")
    if request.method == "POST":
        return HttpResponse("Export Calculator")


def home_handler(request):
    if request.method == "GET":
        data = ["a", "b", "c"]
        return render(request, "home.html")

    if request.method == "POST":
        return HttpResponse("home")


def pack_cost_handler(request):
    if request.method == "GET":
        return render(request, "pack_cost_calculator.html")

    if request.method == "POST":
        request_body = dict(request.POST)
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
        return HttpResponse(
            f"""Cost of Master Carton {MCcostinINR} INR & ${MCcostinDollor} Dollor <br/>
            Cost of SKU {SKUcostinINR} INR & ${SKUcostinDollor} Dollor"""
        )


def pdf_handler(request):
    if request.method == "GET":
        return render(request, "to_pdf copy.html")

    if request.method == "POST":
        request_body = dict(request.POST)
        with open("calculator/utils/calibrate_data/cup_dimention_data.json") as f:
            dim_Data = json.load(f)
        with open("calculator/utils/calibrate_data/buyer_data.json") as g:
            user_data = json.load(g)

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
            "TopDia",
            "BottomDia",
            "Height",
        ]:
            col = []
            for j in range(3):
                try:
                    if i == "TopDia" or i == "BottomDia" or i == "Height":
                        col.append(dim_Data[request_body[f"size_of_cup{j+1}"][0]][i])
                    else:
                        col.append(request_body[f"{i}{j+1}"][0])
                except Exception as e:
                    print("Exception occurred due to :  ", e)
            data.append(col)
        if request_body["Abrv"][0] in user_data.keys():
            CompName = user_data[request_body["Abrv"][0]]["CompanyName"]
            CompAdd = user_data[request_body["Abrv"][0]]["CompanyAdd"]
            BuyerName = user_data[request_body["Abrv"][0]]["BuyerName"]
            BuyerDet = user_data[request_body["Abrv"][0]]["Buyerinfo"]
            TandC = user_data[request_body["Abrv"][0]]["tandc"]
            print(CompAdd)
        else:
            print("data not found")
            CompName = request_body["CompanyName"][0]
            CompAdd = request_body["CompanyAdd"][0]
            BuyerName = request_body["BuyerName"][0]
            BuyerDet = request_body["Buyerinfo"][0]
            TandC = request_body["T&C"][0]

            print("Start-", CompName)
            child = {
                "CompanyName": CompName,
                "CompanyAdd": CompAdd,
                "BuyerName": BuyerName,
                "Buyerinfo": BuyerDet,
                "tandc": TandC,
            }
            user_data[request_body["Abrv"][0]] = child
            print("End-", CompName)

            with open("calculator/utils/calibrate_data/buyer_data.json", "w") as fp:
                json.dump(user_data, fp)

        PDF = topdf(
            No_quote=request_body["noQuote"][0],
            Date=request_body["Date"][0],
            CompName=CompName,
            CompAdd=CompAdd,
            BuyerName=BuyerName,
            BuyerDet=BuyerDet,
            TandC=TandC,
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

        filename = "Q-" + request_body["noQuote"][0] + " " + CompName
        PDF.output(f"quote/{filename}.pdf")
        return render(
            request, "to_pdf copy.html", {"Generated": f"quote/{filename}.pdf"}
        )


def test_handler(request):
    if request.method == "GET":

        return render(request, "test.html")
    else:
        from .models import TestData

        request_body = dict(request.POST)

        t = TestData()

        t.text1 = request_body["text1"][0]
        t.text2 = request_body["text2"][0]
        t.num1 = request_body["num1"][0]
        t.save()
        return render(request, "test.html")
