from django.contrib import admin
from .models import (
    Buyer,
    Quotation,
    Item,
    ProductDim,
    ProductCalculationData,
    MasterCarton,
    Dump,
)

# user: Atharva
# Password: 1234


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ("buyer_alias", "company_name", "buyer_name", "company_address")
    search_fields = ("buyer_alias", "company_name", "buyer_name", "company_address")


@admin.register(ProductDim)
class ProductDimAdmin(admin.ModelAdmin):
    list_display = ("product_name", "top_dia", "bottom_dia", "height")
    search_fields = ("product_name", "top_dia", "bottom_dia", "height")


@admin.register(ProductCalculationData)
class ProductCalculationDataAdmin(admin.ModelAdmin):
    list_display = (
        "product_id",
        "gsm",
        "die_cup_sheet",
        "num_of_blanks_per_sheet",
        "weight_blank_per_sheet",
        "weight_bottom",
        "over_head_cost",
    )
    search_fields = ("product_id__product_name",)


@admin.register(MasterCarton)
class MasterCartonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "length",
        "breadth",
        "height",
    )
    search_fields = ()


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "product",
        "gsm",
        "paper_rate",
        "margin",
        "freight_per_container",
        "cost_per_cup",
        "mc_dollor_rate",
        "mc_inr_rate",
    )
    search_fields = (
        "product__product_name",
        "gsm",
        "paper_rate",
        "product_name",
    )


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ("quotation_id", "buyer_alias", "created_by")
    search_fields = ("quotation_id", "buyer_alias__buyer_alias", "created_by")


@admin.register(Dump)
class DumpAdmin(admin.ModelAdmin):
    list_display = ("product", "product_id", "product_name", "created_by", "created_at")
    search_fields = ("product", "created_at", "created_by")
