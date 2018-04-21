from django.db import models

# dbname = doshow.Bxslider
class Bxslider(models.Model):
    status = models.IntegerField()
    name = models.CharField(max_length=60, blank=True, null=True)
    img_url = models.CharField(max_length=255)
    href = models.CharField(max_length=255)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Bxslider'

# dbname = eph_virtual.present_prop_tbl
class PresentPropTbl(models.Model):
    fromuin = models.PositiveIntegerField()
    touin = models.PositiveIntegerField()
    ownuin = models.PositiveIntegerField()
    propid = models.PositiveIntegerField()
    propnum = models.PositiveIntegerField()
    sendbean = models.PositiveIntegerField()
    receivebean = models.PositiveIntegerField()
    ownbean = models.PositiveIntegerField()
    discount = models.FloatField()
    taxbean = models.PositiveIntegerField()
    fromremainbean = models.PositiveIntegerField()
    toremainbean = models.PositiveIntegerField()
    ownremainbean = models.PositiveIntegerField()
    createtime = models.DateTimeField()
    toflag = models.PositiveIntegerField()
    ownflag = models.PositiveIntegerField()
    curcount = models.IntegerField()
    subownuin = models.PositiveIntegerField(blank=True, null=True)
    subownbean = models.PositiveIntegerField(blank=True, null=True)
    subdiscount = models.FloatField(blank=True, null=True)
    subownremainbean = models.PositiveIntegerField(blank=True, null=True)
    rootroomid = models.PositiveIntegerField(blank=True, null=True)
    roomid = models.PositiveIntegerField(blank=True, null=True)
    appflag = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'present_prop_tbl'


# dbname = self.dw_money_flow
class DwMoneyFlow(models.Model):
    consume_type = models.IntegerField()
    order_id = models.IntegerField()
    consume_uin = models.IntegerField()
    accept_uin = models.IntegerField()
    payment_id = models.IntegerField(blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    money = models.IntegerField()
    before_money = models.IntegerField()
    after_money = models.IntegerField()
    mark = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField()
    state = models.IntegerField()
    state_time = models.DateTimeField()
    appflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dw_money_flow'

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)