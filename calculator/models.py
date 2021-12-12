from django.db import models


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
