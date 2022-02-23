from calculator.models import Buyer, Quotation, ProductDim, User


def quote_buyer_get():
    buyer = Buyer.objects.all()
    user = User.objects.all()
    last_data = {
        "last_quote_id": Quotation.objects.last(),
        "Abrv": Buyer.objects.last().buyer_alias,
        "CompName": Buyer.objects.last().company_name,
        "CompAdd": Buyer.objects.last().company_address,
        "BuyerName": Buyer.objects.last().buyer_name,
        "BuyerDet": "Cell: "
        + Buyer.objects.last().primary_phone_number
        + "\r\n"
        + "Phone: "
        + Buyer.objects.last().secondary_phone_number
        + "\r\n"
        + "Email: "
        + Buyer.objects.last().email_id,
        "TandC": Buyer.objects.last().terms_and_conditions,
    }
    buyerlist = []
    userlist = []

    for i in buyer:
        buyerlist.append(i.buyer_alias)

    for i in user:
        userlist.append(i.username)

    last_data["buyerlist"] = buyerlist
    last_data["userlist"] = userlist
    return last_data


def quote_buyer_post(request_body):
    size = ProductDim.objects.all()
    sizelist = []
    for i in size:
        sizelist.append(i.product_name)
    buyer = Buyer.objects.all()
    buyerlist = []
    for i in buyer:
        buyerlist.append(i.buyer_alias)
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
    context["user"] = request_body["user"][0]
    return context
