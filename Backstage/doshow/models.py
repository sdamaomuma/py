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

# dbname = eph_virtual.prop_tbl
class PropTbl(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    unit = models.CharField(max_length=10)
    bean = models.PositiveIntegerField()
    discount = models.FloatField()
    owndiscount = models.FloatField()
    bonusdiscount = models.FloatField()
    proptypeid = models.PositiveIntegerField()
    createtime = models.DateTimeField()
    proplevel = models.PositiveIntegerField()
    comboeffect = models.IntegerField(db_column='comboEffect', blank=True, null=True)
    conbinativeeffect = models.IntegerField(db_column='conbinativeEffect', blank=True,null=True)
    luckgift = models.IntegerField(db_column='luckGift', blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    flashgift = models.IntegerField(blank=True, null=True)
    tip = models.CharField(max_length=50, blank=True, null=True)
    newtip = models.CharField(max_length=50, blank=True, null=True)
    recommend_state = models.IntegerField(blank=True, null=True)
    zhouxing_state = models.CharField(max_length=255, blank=True, null=True)
    is_mobile_activity = models.SmallIntegerField(blank=True, null=True)
    pc_gift_flag = models.IntegerField(blank=True, null=True)
    talk_gift_flag = models.IntegerField(blank=True, null=True)
    phone_gift_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prop_tbl'

# dbname = eph.basic_tbl
class BasicTbl(models.Model):
    uin = models.AutoField(primary_key=True)
    passwd = models.CharField(max_length=16)
    pic = models.PositiveIntegerField()
    nick = models.CharField(unique=True, max_length=16)
    age = models.PositiveIntegerField()
    gender = models.PositiveIntegerField()
    country = models.CharField(max_length=16)
    province = models.CharField(max_length=16)
    city = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=30)
    auth = models.PositiveIntegerField()
    msg_id = models.PositiveIntegerField()
    search = models.PositiveIntegerField()
    oltime = models.PositiveIntegerField()
    userinfo_ver = models.PositiveIntegerField()
    regtime = models.DateTimeField(blank=True, null=True)
    regfrom = models.PositiveIntegerField()
    resv1 = models.PositiveSmallIntegerField()
    resv2 = models.PositiveIntegerField()
    resv3 = models.CharField(max_length=20)
    resv4 = models.CharField(max_length=20)
    signature = models.CharField(max_length=41, blank=True, null=True)
    photo_path = models.CharField(max_length=200, blank=True, null=True)
    last_path = models.CharField(max_length=200, blank=True, null=True)
    photo_flag = models.IntegerField()
    photo_ctime = models.DateTimeField(blank=True, null=True)
    photo_utime = models.DateTimeField(blank=True, null=True)
    avatar_path_large = models.CharField(max_length=80, blank=True, null=True)
    avatar_flag = models.IntegerField(blank=True, null=True)
    avatar_time = models.DateTimeField(blank=True, null=True)
    phone_security = models.CharField(max_length=11, blank=True, null=True)
    phone_ctime = models.DateTimeField(blank=True, null=True)
    phone_utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basic_tbl'
