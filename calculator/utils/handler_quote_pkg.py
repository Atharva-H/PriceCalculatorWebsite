from calculator.models import ProductDim
from .pack_cost_calculator import pack_cost_calculator


def quote_pkg_get():
    pass


def quote_pkg_post(request_body):

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
        "user": request_body["user"][0],
        "quote_type": request_body["quote_type"][0],
        "currency_type": request_body["currency_type"][0],
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
    return context
