import math
from calculator.models import ProductDim, Buyer, MasterCarton, Quotation, Item
from rich import print


def boxsize(item):
    l = MasterCarton.objects.get(carton_id=item.master_carton_ref.carton_id).length
    b = MasterCarton.objects.get(carton_id=item.master_carton_ref.carton_id).breadth
    h = MasterCarton.objects.get(carton_id=item.master_carton_ref.carton_id).height
    return str(l) + "x" + str(b) + "x" + str(h) + "mm"


def cbmofbox(item):
    l = MasterCarton.objects.get(carton_id=item.master_carton_ref.carton_id).length
    b = MasterCarton.objects.get(carton_id=item.master_carton_ref.carton_id).breadth
    h = MasterCarton.objects.get(carton_id=item.master_carton_ref.carton_id).height
    return round(l * b * h * (10 ** -9), 3)


def cbmofcontainer(item):
    box_count = item.mc_per_container
    l = MasterCarton.objects.get(carton_id=item.master_carton_ref.carton_id).length
    b = MasterCarton.objects.get(carton_id=item.master_carton_ref.carton_id).breadth
    h = MasterCarton.objects.get(carton_id=item.master_carton_ref.carton_id).height
    return round(l * b * h * (10 ** -9) * box_count, 3)


def topdia(item):
    top_dia = ProductDim.objects.get(product_name=item.product.product_name).top_dia
    return top_dia


def bottomdia(item):
    bottom_dia = ProductDim.objects.get(
        product_name=item.product.product_name
    ).bottom_dia
    return bottom_dia


def height(item):
    height = ProductDim.objects.get(product_name=item.product.product_name).height
    return height


def get_data():
    item = Item.objects.all().order_by("-created_at")
    productName = [item[0].product_name, item[1].product_name, item[2].product_name]
    NoPacketinConatiner = [item[0].sku_per_mc, item[1].sku_per_mc, item[2].sku_per_mc]
    mc_dollor_rate = [
        item[0].mc_dollor_rate,
        item[1].mc_dollor_rate,
        item[2].mc_dollor_rate,
    ]
    sku_dollor_rate = [
        item[0].sku_dollor_rate,
        item[1].sku_dollor_rate,
        item[2].sku_dollor_rate,
    ]
    mc_inr_rate = [
        item[0].mc_inr_rate,
        item[1].mc_inr_rate,
        item[2].mc_inr_rate,
    ]
    sku_inr_rate = [
        item[0].sku_inr_rate,
        item[1].sku_inr_rate,
        item[2].sku_inr_rate,
    ]
    NoBoxinConatiner = [
        item[0].mc_per_container,
        item[1].mc_per_container,
        item[2].mc_per_container,
    ]
    BoxSize = [
        boxsize(item[0]),
        boxsize(item[1]),
        boxsize(item[2]),
    ]
    CBMperBox = [
        cbmofbox(item[0]),
        cbmofbox(item[1]),
        cbmofbox(item[2]),
    ]
    CBMper40HQ = [
        cbmofcontainer(item[0]),
        cbmofcontainer(item[1]),
        cbmofcontainer(item[2]),
    ]
    TopDia = [
        topdia(item[0]),
        topdia(item[1]),
        topdia(item[2]),
    ]
    BottomDia = [
        bottomdia(item[0]),
        bottomdia(item[1]),
        bottomdia(item[2]),
    ]
    Height = [
        height(item[0]),
        height(item[1]),
        height(item[2]),
    ]
    DecSub = [
        item[0].product_desription,
        item[1].product_desription,
        item[2].product_desription,
    ]
    items_data = [
        productName,
        NoPacketinConatiner,
        NoBoxinConatiner,
        mc_dollor_rate,
        sku_dollor_rate,
        mc_inr_rate,
        sku_inr_rate,
        BoxSize,
        CBMperBox,
        CBMper40HQ,
        TopDia,
        BottomDia,
        Height,
        DecSub,
    ]
    return items_data
