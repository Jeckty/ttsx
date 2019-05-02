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


