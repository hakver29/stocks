# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Sequelizemeta(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'SequelizeMeta'


class Accounts(models.Model):
    account_code = models.CharField(max_length=255, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_market_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    money_available = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Depth(models.Model):
    i = models.CharField(max_length=255, blank=True, null=True)
    m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_id = models.CharField(max_length=255, blank=True, null=True)
    tick_timestamp = models.DateTimeField(blank=True, null=True)
    bid1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_volume1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_orders1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_volume1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_orders1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_volume2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_orders2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_volume2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_orders2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_volume3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_orders3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_volume3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_orders3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_volume4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_orders4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_volume4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_orders4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_volume5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_orders5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_volume5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_orders5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'depth'


class Orders(models.Model):
    ticker = models.CharField(max_length=255, blank=True, null=True)
    ticker_id = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    market_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    order_type = models.CharField(max_length=255, blank=True, null=True)
    side = models.CharField(max_length=255, blank=True, null=True)
    traded_volume = models.IntegerField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    order_state = models.CharField(max_length=255, blank=True, null=True)
    action_state = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Positions(models.Model):
    ticker = models.CharField(max_length=255, blank=True, null=True)
    ticker_id = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    market_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'positions'


class Potentialorder(models.Model):
    data_id = models.CharField(max_length=255, blank=True, null=True)
    side = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    attempted = models.BooleanField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'potentialOrder'


class Price(models.Model):
    i = models.CharField(max_length=255, blank=True, null=True)
    m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trade_timestamp = models.DateTimeField(blank=True, null=True)
    tick_timestamp = models.DateTimeField(blank=True, null=True)
    bid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bid_volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ask_volume = models.IntegerField(blank=True, null=True)
    close = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    high = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    open = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    turnover_volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price'


class Stock(models.Model):
    ticker = models.CharField(max_length=255, blank=True, null=True)
    ticker_id = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    market_id = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class Trade(models.Model):
    i = models.CharField(max_length=255, blank=True, null=True)
    market_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_id = models.CharField(max_length=255, blank=True, null=True)
    trade_timestamp = models.DateTimeField(blank=True, null=True)
    trade_type = models.CharField(max_length=255, blank=True, null=True)
    trade_id = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trade'
