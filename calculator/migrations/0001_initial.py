# Generated by Django 3.2.9 on 2022-01-24 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('buyer_alias', models.CharField(max_length=20)),
                ('buyer_name', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
                ('company_address', models.TextField(max_length=1000)),
                ('primary_phone_number', models.CharField(max_length=10)),
                ('secondary_phone_number', models.CharField(max_length=10)),
                ('email_id', models.CharField(max_length=100)),
                ('terms_and_conditions', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 1, 24, 22, 55, 47, 180048))),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gsm', models.IntegerField()),
                ('paper_rate', models.FloatField()),
                ('scrape_rate', models.FloatField()),
                ('margin', models.FloatField()),
                ('cost_per_cup', models.FloatField()),
                ('cups_per_sku', models.IntegerField()),
                ('sku_per_mc', models.IntegerField()),
                ('print_cost', models.FloatField()),
                ('mc_cost', models.FloatField()),
                ('freight_per_container', models.FloatField()),
                ('mc_per_container', models.IntegerField()),
                ('dollor_rate', models.FloatField()),
                ('add_cost_per_sku', models.FloatField()),
                ('rate_of_sku', models.IntegerField()),
                ('product_name', models.CharField(max_length=10)),
                ('num_of_sku_per_container', models.IntegerField()),
                ('product_desription', models.TextField(max_length=20000)),
                ('item_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 1, 24, 22, 55, 47, 183042))),
            ],
        ),
        migrations.CreateModel(
            name='MasterCarton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carton_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('length', models.IntegerField()),
                ('breadth', models.IntegerField()),
                ('height', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 1, 24, 22, 55, 47, 182042))),
            ],
        ),
        migrations.CreateModel(
            name='ProductDim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('product_name', models.CharField(max_length=20)),
                ('top_dia', models.FloatField()),
                ('bottom_dia', models.FloatField()),
                ('height', models.FloatField()),
                ('StackHeight', models.FloatField()),
                ('InCupHeight', models.FloatField()),
                ('Weight', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 1, 24, 22, 55, 47, 181045))),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_id', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 1, 24, 22, 55, 47, 184039))),
                ('buyer_alias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.buyer')),
                ('item_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.item')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCalculationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gsm', models.FloatField()),
                ('die_cup_sheet', models.FloatField()),
                ('num_of_blanks_per_sheet', models.IntegerField()),
                ('weight_blank_per_sheet', models.FloatField()),
                ('weight_bottom', models.FloatField()),
                ('over_head_cost', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 1, 24, 22, 55, 47, 182042))),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.productdim')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='master_carton_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.mastercarton'),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.productdim'),
        ),
    ]
