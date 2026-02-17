from django.db import models

class UOM(models.Model):
    uom_id = models.AutoField(primary_key=True)
    uom_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'uom'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, db_column='uom_id')
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'customers'

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'

class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_details'
