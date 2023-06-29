# Create your models here.
from django.db import models


class UserInfo(models.Model):
    first_name = models.CharField(verbose_name="first_name", max_length=16, db_index=True)
    last_name = models.CharField(verbose_name="last_name", max_length=16, db_index=True)
    password = models.CharField(verbose_name="password", max_length=16)
    dob = models.DateField(verbose_name="dob")
    phone = models.CharField(verbose_name="phone", max_length=16)
    email = models.CharField(verbose_name="email", max_length=50, unique=True, db_index=True)
    wechat = models.CharField(verbose_name="wechat", max_length=50, blank=True, null=True)
    address = models.DateField(verbose_name="address", max_length=255, blank=True, null=True)
    register_date = models.DateField(verbose_name="register_date")
    deleted = models.BooleanField(verbose_name="deleted", default=0)
    membership_id = models.ForeignKey(verbose_name='membership_id', to="Membership", on_delete=models.SET_DEFAULT,
                                      default=0)


class Membership(models.Model):
    level = models.IntegerField(verbose_name="level")
    discount = models.DecimalField(verbose_name="discount", max_digits=3, decimal_places=2)
    note = models.TextField(verbose_name='note', blank=True, null=True)
    credit = models.IntegerField(verbose_name="credit", default=0)
    expired_date = models.IntegerField(verbose_name='expired_date', default=12)

    def __str__(self):
        return "Membership Level:" + f" {self.level} " + self.note + "\r\n"


class MemberPayment(models.Model):
    payment_amount = models.IntegerField(verbose_name="payment_amount")
    payment_date = models.DateField(verbose_name="payment_date")
    note = models.TextField(verbose_name='note', blank=True, null=True)
    userInfo_id = models.ForeignKey(verbose_name='userInfo_id', to="UserInfo", on_delete=models.CASCADE)


class MemberConsume(models.Model):
    consume_amount = models.IntegerField(verbose_name="consume_amount")
    consume_date = models.DateField(verbose_name="consume_date")
    note = models.TextField(verbose_name='note', blank=True, null=True)
    deleted = models.BooleanField(verbose_name="deleted", default=0)
    consumeItem_id = models.ForeignKey(verbose_name="consumeItem_id", to="ConsumeItem", on_delete=models.CASCADE)
    userInfo_id = models.ForeignKey(verbose_name='userInfo_id', to="UserInfo", on_delete=models.CASCADE)


class ConsumeItem(models.Model):
    item_name = models.CharField(verbose_name="item_name", max_length=16, db_index=True)
    item_price = models.DecimalField(verbose_name="item_price", max_digits=7, decimal_places=2)
    item_detail = models.TextField(verbose_name="item_detail")
    item_frequency = models.IntegerField(verbose_name="item_frequency", default=1)
    note = models.TextField(verbose_name='note', blank=True, null=True)


class ServiceRecord(models.Model):
    start_date = models.DateField(verbose_name="start_date")
    client_info = models.TextField(verbose_name="client_info")
    consumeItem_id = models.ForeignKey(verbose_name="consumeItem_id", to="ConsumeItem", on_delete=models.CASCADE)
    userInfo_id = models.ForeignKey(verbose_name='userInfo_id', to="UserInfo", on_delete=models.CASCADE)
