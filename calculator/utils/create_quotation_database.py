from unicodedata import name
from calculator.models import ProductDim, Buyer, MasterCarton, Quotation, Item


def update_database(context):

    item = Item(
        product=ProductDim.objects.get(product_name=context["size_of_cup"]),
        gsm=context["gsm"],
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
        dollor_rate=context["DollorRate"],
        add_cost_per_sku=context["AddCostperSKU"],
        rate_of_sku=float(context["SKUcostinDollor"]),
        # Form3
        product_name=context["productName"],
        num_of_sku_per_container=context["SKUperConatiner"],
        product_desription=context["DecSub"],
        master_carton_ref=MasterCarton.objects.get(length=350),
    )
    item.save()
    quotation = Quotation(
        quotation_id=context["No_quote"],
        buyer_alias=Buyer.objects.get(buyer_alias=context["Abrv"]),
        created_by=context["created_by"],
    )
    quotation.save()
    quotation.items.add(item)
    quotation.save()
