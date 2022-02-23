import imp
from calculator.models import ProductDim, Buyer, MasterCarton, Quotation, Item
from re import findall
from rich import print


def update_database_item(context):
    size = context["MCSize"]
    size = findall(r"\d+", size)

    try:
        mastercarton = (
            MasterCarton.objects.filter(length=int(size[0]))
            .filter(breadth=int(size[1]))
            .filter(height=int(size[2]))
        )[0]

    except Exception as e:
        print("Exception occurred due to :  ", e)
        mastercarton = MasterCarton(
            length=int(size[0]),
            breadth=int(size[1]),
            height=int(size[2]),
        )
        mastercarton.save()
    item = Item(
        product=ProductDim.objects.get(product_name=context["size_of_cup"]),
        gsm=context["gsm"],
        bottom_gsm=context["bottom_gsm"],
        paper_rate=context["paper_rate"],
        scrape_rate=context["scrape_rate"],
        margin=context["margin"],
        cost_per_cup=context["base_cup_cost"],
        # Form2
        cups_per_sku=context["CupsperSKU"],
        sku_per_mc=context["SKUperMC"],
        print_cost=context["CostPrintColorperCup"],
        mc_cost=context["MCCost"],
        freight_per_container=context["Freight"],
        mc_per_container=context["BoxsPerContainer"],
        dollor_rate=float(context["DollorRate"]),
        add_cost_per_sku=context["AddCostperSKU"],
        mc_dollor_rate=float(context["MCcostinDollor"]),
        sku_dollor_rate=float(context["SKUcostinDollor"]),
        mc_inr_rate=float(context["MCcostinINR"]),
        sku_inr_rate=float(context["SKUcostinINR"]),
        # Form3
        product_name=context["productName"],
        num_of_sku_per_container=context["SKUperConatiner"],
        product_desription=context["DecSub"],
        master_carton_ref=mastercarton,
    )
    item.save()


def update_database_quote(context):
    n = context["item_count"]
    item = Item.objects.all().order_by("-created_at")
    quotation = Quotation(
        quotation_id=context["No_quote"],
        buyer_alias=Buyer.objects.get(buyer_alias=context["Abrv"]),
        created_by=context["created_by"],
    )
    quotation.save()
    for i in range(n):
        quotation.items.add(item[i])
    quotation.save()
