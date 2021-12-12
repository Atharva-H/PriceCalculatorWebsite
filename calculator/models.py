from django.db import models
from uuid import uuid4
from datetime import datetime

# class Buyer(models.Model):
#     buyer_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)
#     buyer_alias = models.CharField(max_length=20, blank= False, null=False)
#     company_name = models.CharField(max_length=20, blank= False, null=False)
#     company_address = models.TextField(max_length=1000, blank= False, null=False)
#     primary_phone_number =  models.CharField(max_length=10, blank= False, null=False)
#     secondary_phone_number = models.CharField(max_length=10, blank= False, null=False)
#     email_id =  models.CharField(max_length=100, blank= False, null=False)
#     terms_and_conditions = models.TextField(max_length=500, blank= False, null= False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(default=datetime.now())

# class MasterCarton(models.Model):
#     carton_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)
#     length = models.IntegerField()
#     breadth = models.IntegerField()
#     height = models.IntegerField()

# class Item(models.Model):
    
    
    
#     gsm = models.IntegerField()
#     paper_rate = models.FloatField()
#     scrape_rate = models.FloatField()
#     margin = models.FloatField()
#     cost_per_cup = models.FloatField()
#     cups_per_sku = models.IntegerField()
#     sku_per_mc = models.IntegerField()
#     print_cost = models.FloatField()
#     mc_cost = models.FloatField()
#     freight_per_container = models.FloatField()
#     mc_per_container = models.IntegerField()
#     dollor_rate = models.FloatField()
#     add_cost_per_sku = models.FloatField()


#     size_of_cup = models.CharField(max_length=10)
#     product_name = models.CharField(max_length=10)
#     num_of_sku = models.IntegerField()
#     rate_of_sku = models.IntegerField()
#     product_desription = models.TextField(max_length=20000)
#     num_of_mc = models.IntegerField()
#     sku_per_mc = models.IntegerField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(default=datetime.now())

#     master_carton_ref = models.ForeignKey()
#     buyer_ref = models.ForeignKey()
#     quotation_id = models.CharField(max_length=20)

# # class Quotation():
    
    




class TestData(models.Model):
    text1 = models.CharField(max_length=20)
    text2 = models.CharField(max_length=20)
    num1 = models.IntegerField()


class QuotationData(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    quotation_ID = models.CharField(max_length=20)
    abrv = models.CharField(max_length=15, default="test")
    size = models.CharField(max_length=10)
    gsm = models.IntegerField()
    paper_rate = models.FloatField()
    scrape_rate = models.FloatField()
    margin = models.FloatField()
    cost_per_cup = models.FloatField()
    cups_per_sku = models.IntegerField()
    sku_per_mc = models.IntegerField()
    print_cost = models.FloatField()
    mc_cost = models.FloatField()
    freight_per_container = models.FloatField()
    mc_per_container = models.IntegerField()
    dollor_rate = models.FloatField()
    add_cost_per_sku = models.FloatField()

    def __str__(self):
        return self.abrv


class BuyerData(models.Model):
    abrv = models.ForeignKey(QuotationData, on_delete=models.CASCADE)
    # abrv = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_add = models.TextField()
    buyer_name = models.CharField(max_length=50)
    buyer_info = models.TextField(default="info")
