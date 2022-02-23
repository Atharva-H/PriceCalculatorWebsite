from calculator.models import ProductDim, Quotation, Buyer
from .to_pdf import topdf


def pdf_handler_get():
    size = ProductDim.objects.all()
    buyer = Buyer.objects.all()
    last_quote_id = Quotation.objects.last()
    buyerlist = []
    for i in buyer:
        buyerlist.append(i.buyer_alias)
    sizelist = []
    for i in size:
        sizelist.append(i.product_name)
    return sizelist, last_quote_id, buyerlist


def pdf_handler_post(request_body):
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
    return filename
