# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CateProduct(models.Model):
    cate3_id_new = models.ForeignKey(
        "Category", models.DO_NOTHING, db_column="cate3_id_new"
    )
    product = models.ForeignKey("Products", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "cate_product"


class Category(models.Model):
    cate3_id_new = models.CharField(primary_key=True, max_length=80)
    cate1_id = models.CharField(max_length=80)
    cate1_name = models.TextField()
    cate2_id = models.CharField(max_length=80)
    cate2_name = models.TextField()
    cate3_id = models.CharField(max_length=80)
    cate3_name = models.TextField()

    class Meta:
        managed = False
        db_table = "category"


class Products(models.Model):
    product_id = models.CharField(primary_key=True, max_length=80)
    product_name = models.TextField()
    uri = models.TextField(blank=True, null=True)
    oldprice = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    value_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "products"


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=80)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    mac_address = models.CharField(max_length=50, blank=True, null=True)
    last_activity = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "users"


# Not in Database class
class Category_1(models.Model):
    cate1_id = models.CharField(max_length=80)
    cate1_name = models.TextField()

    class Meta:
        managed = False
        db_table = "category"

