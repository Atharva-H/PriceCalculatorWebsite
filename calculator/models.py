from django.db import models
from uuid import uuid4
from datetime import datetime


class Buyer(models.Model):
    buyer_alias = models.CharField(max_length=30, blank=False, null=False)
    buyer_name = models.CharField(max_length=30, blank=False, null=False)
    company_name = models.CharField(max_length=30, blank=False, null=False)
    company_address = models.TextField(max_length=1000, blank=False, null=False)
    primary_phone_number = models.CharField(max_length=15, blank=False, null=False)
    secondary_phone_number = models.CharField(max_length=15, blank=False, null=False)
    email_id = models.CharField(max_length=100, blank=False, null=False)
    terms_and_conditions = models.TextField(max_length=500, blank=False, null=False)

    buyer_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.buyer_alias)


class ProductDim(models.Model):

    product_name = models.CharField(max_length=20, blank=False, null=False)
    top_dia = models.FloatField()
    bottom_dia = models.FloatField()
    height = models.FloatField()
    StackHeight = models.FloatField()
    InCupHeight = models.FloatField()
    Weight = models.FloatField()

    product_id = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid4
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.product_name)


class ProductCalculationData(models.Model):
    product_id = models.ForeignKey(ProductDim, on_delete=models.CASCADE)
    gsm = models.FloatField()
    die_cup_sheet = models.FloatField()
    num_of_blanks_per_sheet = models.IntegerField()
    weight_blank_per_sheet = models.FloatField()
    weight_bottom = models.FloatField()
    over_head_cost = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now())


class MasterCarton(models.Model):
    length = models.IntegerField()
    breadth = models.IntegerField()
    height = models.IntegerField()

    carton_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now())


class Item(models.Model):
    # Form1
    product = models.ForeignKey(ProductDim, on_delete=models.CASCADE)
    gsm = models.IntegerField()
    paper_rate = models.FloatField()
    scrape_rate = models.FloatField()
    margin = models.FloatField()
    cost_per_cup = models.FloatField()

    # Form2
    cups_per_sku = models.IntegerField()
    sku_per_mc = models.IntegerField()
    print_cost = models.FloatField()
    mc_cost = models.FloatField()
    freight_per_container = models.FloatField()
    mc_per_container = models.IntegerField()
    dollor_rate = models.FloatField()
    add_cost_per_sku = models.FloatField()
    rate_of_sku = models.IntegerField()

    # Form3
    product_name = models.CharField(max_length=30)
    num_of_sku_per_container = models.IntegerField()
    product_desription = models.TextField(max_length=20000)

    # Unique ID & ForeignKey For Box Detail
    item_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)
    master_carton_ref = models.ForeignKey(MasterCarton, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.product_name)


class Quotation(models.Model):
    quotation_id = models.CharField(max_length=20)
    buyer_alias = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    # item_1 = models.ForeignKey(Item, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)
    # item_3 = models.ForeignKey(Item, on_delete=models.CASCADE)

    created_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.quotation_id)
