from calculator.models import ProductDim, Buyer, MasterCarton, Quotation, Item, Dump


def dump_data(context):
    dump = Dump()

    try:
        dump.product = ProductDim.objects.get(product_name=context["size_of_cup"])
        if "gsm" in context:
            dump.gsm = context["gsm"]
            dump.paper_rate = context["paper_rate"]
            dump.scrape_rate = context["scrape_rate"]
            dump.margin = context["margin"]
            dump.cost_per_cup = context["base_cup_cost"]
        elif "CupsperSKU" in context:
            dump.cost_per_cup = context["base_cup_cost"]
            dump.cups_per_sku = context["CupsperSKU"]
            dump.sku_per_mc = context["SKUperMC"]
            dump.print_cost = context["CostPrintColorperCup"]
            dump.mc_cost = context["MCCost"]
            dump.freight_per_container = context["Freight"]
            dump.mc_per_container = context["BoxsPerContainer"]
            dump.dollor_rate = context["DollorRate"]
            dump.add_cost_per_sku = context["AddCostperSKU"]
            dump.rate_of_sku = float(context["SKUcostinDollor"])
        elif "productName" in context:
            dump.product_name = context["productName"]
            dump.num_of_sku_per_container = context["SKUperConatiner"]
            dump.product_desription = context["DecSub"]
            dump.created_by = context["created_by"]
            # dump.buyer_alias = (Buyer.objects.get(buyer_alia=context["Abrv"]),)
    except Exception as e:
        print("Exception occurred due to :  ", e)
    dump.save()
