from calculator.models import ProductDim
from .pack_cost_calculator import pack_cost_calculator
from .database_dump import dump_data


def pack_cost_handler_get():
    size = ProductDim.objects.all()
    sizelist = []
    for i in size:
        sizelist.append(i.product_name)
    return sizelist


def pack_cost_handler_post(request_body):
    context = {}
    context["size_of_cup"] = request_body["size_of_cup"][0]
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

    dump_data(context)

    return context
