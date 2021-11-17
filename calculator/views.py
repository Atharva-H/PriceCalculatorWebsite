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
        context["some_string"] = base_cup_cost
        return render(request, "base_cup_cost_calculator.html", context)


def pack_cost_handler(request):
    if request.method == "GET":
        return render(request, "pack_cost_calculator.html")

    if request.method == "POST":
        request_body = dict(request.POST)
        costinINR, costinDollor = pack_cost_calculator(
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
            f"Cost of Master Carton {costinINR} INR & ${costinDollor} Dollor"
        )


def home(request):
    if request.method == "GET":
        return render(request, "home.html")

    if request.method == "POST":
        return HttpResponse("home")


def pdf_handler(request):
    if request.method == "GET":
        return render(request, "buyer_info.html")

    if request.method == "POST":
        request_body = dict(request.POST)
        with open("calculator/utils/calibrate_data/cup_dimention_data.json") as f:
            dim_Data = json.load(f)
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
                if i == "TopDia" or i == "BottomDia" or i == "Height":
                    col.append(dim_Data[request_body[f"size_of_cup{j+1}"][0]][i])
                else:
                    col.append(request_body[f"{i}{j+1}"][0])
            data.append(col)

        PDF = topdf(
            No_quote=request_body["noQuote"][0],
            Date=request_body["Date"][0],
            CompName=request_body["CompanyName"][0],
            CompAdd=request_body["CompanyAdd"][0],
            BuyerName=request_body["BuyerName"][0],
            BuyerDet=request_body["Buyerinfo"][0],
            TandC=request_body["T&C"][0],
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

        filename = (
            "Q-" + request_body["noQuote"][0] + " " + request_body["CompanyName"][0]
        )
        PDF.output(f"quote/{filename}.pdf")
        return HttpResponse(f"Quotation File generated in quote/{filename}")


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
