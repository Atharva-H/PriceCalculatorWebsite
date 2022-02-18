from calculator.models import ProductDim
from .base_cup_cost_calculator import base_cup_cost_calculator


def quote_base_get():
    size = ProductDim.objects.all()
    sizelist = []
    for i in size:
        sizelist.append(i.product_name)
    return sizelist


def quote_base_post(request_body):
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
        "user": request_body["user"][0],
    }
    return context
