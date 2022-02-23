from calculator.models import ProductDim
from .base_cup_cost_calculator import base_cup_cost_calculator
from .database_dump import dump_data


def base_cup_handler_get():
    size = ProductDim.objects.all()
    sizelist = []
    for i in size:
        sizelist.append(i.product_name)
    return sizelist


def base_cup_handler_post(request_body):
    size_of_cup = request_body["size_of_cup"][0]
    gsm = int(request_body["gsm"][0])
    paper_rate = int(request_body["paper_rate"][0])
    scrape_rate = int(request_body["scrape_rate"][0])
    margin = int(request_body["margin"][0])

    try:
        print("run try 1")

        bottom_gsm = int(request_body["bottom_gsm"][0])
        print("run try 2")

        base_cup_cost = base_cup_cost_calculator(
            size_of_cup, gsm, paper_rate, scrape_rate, margin, bottom_gsm
        )
        print("run try 3")

    except Exception as e:
        print("Exception occurred due to :  ", e)
        bottom_gsm = 0
        base_cup_cost = base_cup_cost_calculator(
            size_of_cup, gsm, paper_rate, scrape_rate, margin, bottom_gsm
        )

    context = {}
    context["gsm"] = gsm
    context["base_cup_cost"] = base_cup_cost
    context["paper_rate"] = paper_rate
    context["scrape_rate"] = scrape_rate
    context["size_of_cup"] = size_of_cup
    context["margin"] = margin
    context["bottom_gsm"] = bottom_gsm

    dump_data(context)

    return context
