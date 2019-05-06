from django.db import models

# Create your models here.
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)

class Goods(models.Model):
    # 商品id
    productid = models.CharField(max_length=30)
    # 商品图片
    picUrl = models.CharField(max_length=150)
    picUrlFromIc = models.CharField(max_length=150)
    picUrlM = models.CharField(max_length=150)
    picUrlNew = models.CharField(max_length=150)
    # 商品名称
    shortName = models.CharField(max_length=50)
    # 商品长名称
    longName = models.CharField(max_length=500)
    # 规格
    specifics = models.CharField(max_length=20)
    # 价格
    price = models.FloatField()
    # 组id
    categoryid = models.CharField(max_length=10)
    # 子类组id
    childcid = models.CharField(max_length=10)
    # 子类组名称
    childcidname = models.CharField(max_length=10)
    # 库存
    storenums = models.IntegerField()
    # 销量
    productnum = models.IntegerField()

class User(models.Model):
    userId=models.CharField(max_length=25)
    userName=models.CharField(max_length=30)
    passWord=models.CharField(max_length=25)
    mailId=models.CharField(max_length=30)
    phoneNum=models.CharField(max_length=15)
    userAddress=models.CharField(max_length=200)
    userToken=models.CharField(max_length=50)
    @classmethod
    def createUser(cls,userId,userName,passWord,mailId,phoneNum,userAddress,userToken):
        u=cls(userId=userId,userName=userName,passWord=passWord,mailId=mailId,phoneNum=phoneNum,userAddress=userAddress,userToken=userToken)
        return u

class Cart(models.Model):
    userAccount = models.CharField(max_length=25)
    productid = models.CharField(max_length=30)
    productnum = models.IntegerField()
    productprice = models.FloatField()
    isChose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=150)
    productname = models.CharField(max_length=100)
    orderid = models.CharField(max_length=20, default="0")
    isDelete = models.BooleanField(default=False)
    @classmethod
    def createcart(cls, userAccount, productid, productnum, productprice, isChose, productimg, productname, isDelete):
        c = cls(userAccount=userAccount, productid=productid, productnum=productnum, productprice=productprice,
                isChose=isChose, productimg=productimg, productname=productname, isDelete=isDelete)
        return c

class Address(models.Model):
    userId=models.CharField(max_length=25)
    receiver=models.CharField(max_length=20)
    detailAddress=models.CharField(max_length=400)
    phoneNum=models.CharField(max_length=20)
    postalCode=models.CharField(max_length=10)
    isUsed=models.BooleanField(default=False)
    isDelete=models.BooleanField(default=False)
    @classmethod
    def createAddress(cls,userid,receiver,phonenum,detailaddress,postalcode,isused,isdelete):
        a=cls(userId=userid,receiver=receiver,phoneNum=phonenum,detailAddress=detailaddress,postalCode=postalcode,isUsed=isused,isDelete=isdelete)
        return a

class Order(models.Model):
    pass
    userId=models.CharField(max_length=20)
    orderId=models.CharField(max_length=25)
    payWay=models.CharField(max_length=20)
    paymentStatus=models.BooleanField()
    trackNum=models.CharField(max_length=20)
    trackUrl=models.CharField(max_length=50)
    @classmethod
    def createOrder(cls,userId,orderId,payWay,paymentStatus,trackNum,trackUrl):
        o=cls(userId=userId,orderId=orderId,payWay=payWay,paymentStatus=paymentStatus,trackNum=trackNum,trackUrl=trackUrl)
        return o






