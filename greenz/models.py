from django.db import models


class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cart'

    def __str__(self):
        return self.id


class CartItem(models.Model):
    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    cart = models.ForeignKey(Cart, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cart_item'

    def sub_total(self):
        return self.product.cost * self.quantity

    def __str__(self):
        return self.product


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    shipped_date = models.CharField(max_length=135, blank=True, null=True)
    created_date = models.CharField(max_length=135, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    cart = models.ForeignKey(Cart, models.DO_NOTHING)
    status = models.ForeignKey('Status', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders'


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package'


class Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    total = models.FloatField(blank=True, null=True)
    payment_time = models.CharField(max_length=135, blank=True, null=True)
    order = models.OneToOneField(Orders, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length=45, blank=True, null=True)
    origin = models.CharField(max_length=135, blank=True, null=True)
    expirationdate = models.CharField(db_column='expirationDate', max_length=135, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(max_length=135, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    package = models.ForeignKey(Package, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product'


class RAddress(models.Model):
    address = models.CharField(primary_key=True, max_length=135)
    latitude = models.CharField(max_length=45, blank=True, null=True)
    longtitude = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_address'


class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    method = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class RecipeIngredient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    weight = models.CharField(max_length=45, blank=True, null=True)
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recipe_ingredient'


class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=135, blank=True, null=True)
    keyword = models.CharField(max_length=135, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=45)
    password = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=90, blank=True, null=True)
    address = models.CharField(max_length=135, blank=True, null=True)
    phone_number = models.CharField(max_length=135, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class RMAP(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=135, blank=True, null=True)
    address = models.CharField(max_length=135, blank=True, null=True)
    latitude = models.CharField(max_length=45, blank=True, null=True)
    longtitude = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_map'

class FreshFoodList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length=45, blank=True, null=True)
    origin = models.CharField(max_length=135, blank=True, null=True)
    expirationdate = models.CharField(db_column='expirationDate', max_length=135, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=135, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    package = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fresh_food_list'


class SourceList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length=45, blank=True, null=True)
    origin = models.CharField(max_length=135, blank=True, null=True)
    expirationdate = models.CharField(db_column='expirationDate', max_length=135, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=135, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    package = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source_list'
