from calculator.models import Buyer, Quotation, ProductDim, User
from .getquote_to_pdf import getquote_topdf
from .database_itemdetails import get_data


from .database_quotation import update_database_item, update_database_quote


def quote_nameitem_get():
    size = ProductDim.objects.all()
    user = User.objects.all()

    userlist = []
    sizelist = []

    for i in user:
        userlist.append(i.username)
    for i in size:
        sizelist.append(i.product_name)
    return userlist, sizelist


def quote_nameitem_post(request_body):

    user = User.objects.all()
    userlist = []
    for i in user:
        userlist.append(i.username)

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
        "bottom_gsm": request_body["bottom_gsm"][0],
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
        "SKUcostinINR": request_body["SKUcostinINR"][0],
        "MCcostinDollor": request_body["MCcostinDollor"][0],
        "MCcostinINR": request_body["MCcostinINR"][0],
        "productName": request_body["productName1"][0],
        "Amount": request_body["Amount1"][0],
        "MCSize": request_body["MCSize1"][0],
        "CBMperMC1": request_body["CBMperMC1"][0],
        "CBMper40HQ1": request_body["CBMper40HQ1"][0],
        "DecSub": request_body["DecSub1"][0],
        "TopDia": product_info.top_dia,
        "BottomDia": product_info.bottom_dia,
        "Height": product_info.height,
        "created_by": request_body["user"][0],
        "userlist": userlist,
        "user": request_body["user"][0],
        "quote_type": request_body["quote_type"][0],
        "currency_type": request_body["currency_type"][0],
        # "item_count": 2,
        "item_count": int(request_body["item_count"][0]),
    }
    update_database_item(context)

    return context


def quote_nameitem_generate(request_body):
    item_data = get_data()

    user = User.objects.all()
    userlist = []
    for i in user:
        userlist.append(i.username)

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
        "bottom_gsm": request_body["bottom_gsm"][0],
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
        "SKUcostinINR": request_body["SKUcostinINR"][0],
        "MCcostinDollor": request_body["MCcostinDollor"][0],
        "MCcostinINR": request_body["MCcostinINR"][0],
        "productName": request_body["productName1"][0],
        "Amount": request_body["Amount1"][0],
        "MCSize": request_body["MCSize1"][0],
        "CBMperMC1": request_body["CBMperMC1"][0],
        "CBMper40HQ1": request_body["CBMper40HQ1"][0],
        "DecSub": request_body["DecSub1"][0],
        "TopDia": product_info.top_dia,
        "BottomDia": product_info.bottom_dia,
        "Height": product_info.height,
        "created_by": request_body["user"][0],
        "userlist": userlist,
        "user": request_body["user"][0],
        "quote_type": request_body["quote_type"][0],
        "currency_type": request_body["currency_type"][0],
        # "item_count": 2,
        "item_count": int(request_body["item_count"][0]),
    }

    PDF = getquote_topdf(
        Date=context["Date"],
        No_quote=context["No_quote"],
        CompName=context["CompName"],
        CompAdd=context["CompAdd"],
        BuyerName=context["BuyerName"],
        BuyerDet=context["BuyerDet"],
        TandC=context["TandC"],
        quote_type=context["quote_type"],
        currency_type=context["currency_type"],
        item_count=context["item_count"],
        CBMperBox=item_data[8],
        CBMper40HQ=item_data[9],
        DecSub=item_data[13],
        TopDia=item_data[10],
        BottomDia=item_data[11],
        Height=item_data[12],
        productName=item_data[0],
        BoxSize=item_data[7],
        item_data=item_data,
    )
    abrv = context["Abrv"]
    filename = "Q-" + request_body["noQuote"][0] + " " + context["CompName"]
    PDF.output(f"{filename}.pdf", "F")

    context = {
        "No_quote": request_body["noQuote"][0],
        "Abrv": request_body["Abrv"][0],
        "created_by": request_body["user"][0],
        "item_count": int(request_body["item_count"][0]),
    }
    context["Path"] = f"{filename}.pdf"
    update_database_quote(context)
    return context
