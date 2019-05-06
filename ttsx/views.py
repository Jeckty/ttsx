from django.shortcuts import render,HttpResponse,redirect
from . models import FoodTypes,Goods,User,Cart,Address,Order
from django.http import JsonResponse
import time,random,datetime
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def login(request):
    return render(request,"ttsx/login.html")
def cart(request):
    username = request.session.get("myname")
    userid = request.session.get("myid")
    cartlist = Cart.objects.filter(userAccount=userid,orderid=1)
    chose=Cart.objects.filter(userAccount=userid,isChose=True,orderid=1)
    chosenum=len(chose)
    totalPrice=0
    for item in chose:
        totalPrice+=item.productprice
    totalPrice = round(totalPrice, 2)
    return render(request,"ttsx/cart.html",{"username": username, "cartist": cartlist,"cartnum": len(cartlist),"chosenum":chosenum,"totalprice":totalPrice})
def detail(request):
    return render(request,"ttsx/detail.html")
def index(request):
    username = request.session.get("myname")
    tpyeList=FoodTypes.objects.all()
    neiyiList=Goods.objects.filter(categoryid="4000")[0:4]
    jiaList=Goods.objects.filter(categoryid="80000")[0:4]
    ertongList = Goods.objects.filter(categoryid="71000")[0:4]
    shipingList = Goods.objects.filter(categoryid="5000")[0:4]
    baihuoList = Goods.objects.filter(categoryid="37000")[0:4]
    nvzhuangList = Goods.objects.filter(categoryid="1000")[0:4]
    meizhuangList = Goods.objects.filter(categoryid="2000")[0:4]
    qicheList = Goods.objects.filter(categoryid="34000")[0:4]
    yundongList = Goods.objects.filter(categoryid="38000")[0:4]
    nanzhuangList = Goods.objects.filter(categoryid="7000")[0:4]
    shoujiList = Goods.objects.filter(categoryid="43000")[0:4]
    ll=[neiyiList,ertongList,shipingList,baihuoList,nvzhuangList,meizhuangList,jiaList,qicheList,yundongList,nanzhuangList,shoujiList]
    allList=[]
    for i in range(11):
        dic=[{"type":tpyeList[i],"goods":ll[i]}]
        allList.append(dic)
    return render(request,"ttsx/index.html",{"typeList":allList,"List":tpyeList,"username": username})
def list(request,typeid,page):
    username=request.session.get("myname")
    userid = request.session.get("myid")
    list=FoodTypes.objects.all()
    typename=FoodTypes.objects.get(typeid=typeid)
    foodlist=Goods.objects.filter(categoryid=typeid)
    paginator = Paginator(foodlist, 15)
    foods = paginator.page(page)
    cart=Cart.objects.filter(userAccount=userid,orderid=1)
    cartnum=0
    for item in cart:
        cartnum+=item.productnum
    return render(request,"ttsx/list.html",{"username":username,"List":list,"typename":typename,"foodlist":foods,"cartnum":cartnum})
def place_order(request):
    username = request.session.get("myname")
    userid = request.session.get("myid")
    address=Address.objects.filter(userId=userid)
    order = Cart.objects.filter(userAccount=userid,productnum__gt=0, isChose=True,orderid=1)
    totalPrice = 0
    for item in order:
        totalPrice += item.productprice
    return render(request,"ttsx/place_order.html",{"username": username,"address":address,"order":order,"totalprice":totalPrice,"finnallyprice":totalPrice+10})
def register(request):
    if request.method=="POST":
        userId=request.POST.get("user_id")
        userName=request.POST.get("user_name")
        passWord=request.POST.get("pwd")
        mailId=request.POST.get("email")
        phoneNum=request.POST.get("phonenum")
        userAddress=request.POST.get("address")
        userToken=str(time.time()+random.randrange(1,100000))
        use=User.createUser(userId=userId,userName=userName,passWord=passWord,mailId=mailId,phoneNum=phoneNum,userAddress=userAddress,userToken=userToken)
        use.save()
        request.session["myname"]=userName
        request.session["myid"] = userId
        request.session["usertoken"]=userToken
        return redirect("/user_center_info/")

    else:
        return render(request,"ttsx/register.html")
def user_center_info(request):
    try:
        username=request.session.get("myname")
        usertoken = request.session.get("usertoken")
        user=User.objects.get(userToken=usertoken)
        userid=user.userId
        return render(request,"ttsx/user_center_info.html",{"username":username,"userid":user.userId,"phonenum":user.phoneNum,"useraddress":user.userAddress})
    except:
        return render(request, "ttsx/user_center_info.html")

def user_center_order(request):
    username = request.session.get("myname")
    userid = request.session.get("myid")
    order=Order.objects.filter(userId=userid)
    orderList = []
    for item in order:
        dic={"item":item,"order":item.cart_set.all()}
        orderList.append(dic)
    return render(request,"ttsx/user_center_order.html",{"username":username,"orderList":orderList})
def user_center_site(request):
    username = request.session.get("myname")
    userid = request.session.get("myid")
    address = Address.objects.get(userId=userid,isUsed=True)
    return render(request,"ttsx/user_center_site.html",{"username":username,"address":address})
def checkid(request):
    userid = request.POST.get("uesrid")
    try:
        s=User.objects.get(userId=userid)
        return JsonResponse({"data":"已被注册","status":"error"})
    except User.DoesNotExist as e:
        return JsonResponse({"data":"可以注册","status":"success"})
def checklogin(request):
    if request.method=="POST":
        userid=request.POST.get("username")
        pwd=request.POST.get("pwd")
        try:
            user=User.objects.get(userId=userid)
        except User.DoesNotExist as e:
            return JsonResponse({"data":"该用户不存在","status":"error"})
        password=user.passWord
        if password!=pwd:
            return JsonResponse({"data": "密码错误", "status": "error"})
        else:
            user=User.objects.get(userId=userid)
            usertoken=str(time.time()+random.randrange(1,100000))
            user.userToken=usertoken
            user.save()
            myname=user.userName
            request.session["myname"]=myname
            request.session["myid"] = userid
            request.session["usertoken"]=usertoken
            return JsonResponse({"data": "登陆成功", "status": "success"})
    else:
        return redirect("/login/")

def base(request):
    username=request.session.get("myname")
    return render(request,"ttsx/base.html",{"username":username})

def quit(request):
    logout(request)
    return redirect("/login/")

def changecart(request,id):
    token=request.session.get("usertoken")
    pid=request.POST.get("pid")
    good = Goods.objects.get(productid=pid)
    if  not token:
        return JsonResponse({"data": "-1", "status": "error"})
    userid=request.session.get("myid")
    good=Goods.objects.get(productid=pid)
    if id=="0":
        if good.storenums==0:
            return JsonResponse({"data":"0"})
        try:
            cart=Cart.objects.get(userAccount=userid,productid=pid,orderid=1)
            cart.productnum+=1
            cart.productprice=cart.productnum * good.price
            cart.save()
        except Cart.DoesNotExist as e:
            order=Order.objects.get(id=1)
            c=Cart.createcart(userid, pid, 1, good.price,True, good.picUrl, good.shortName, False,order)
            c.save()
        return JsonResponse({"data": "1", "status": "success"})
    if id=="1":
        ischose=request.POST.get("value")
        if ischose=="false":
            ischose="False"
        if ischose=="true":
            ischose="True"
        cart = Cart.objects.get(userAccount=userid, productid=pid,orderid=1)
        cart.isChose=ischose
        cart.save()
        chose = Cart.objects.filter(userAccount=userid, isChose=True,orderid=1)
        chosenum = len(chose)
        totalPrice = 0
        for item in chose:
            totalPrice += item.productprice
        totalPrice = round(totalPrice, 2)
        return JsonResponse({"data": "1", "status": "success","chosenum":chosenum,"totalprice":totalPrice})
    # 增加购物车
    if id=="2":
        good=Goods.objects.get(productid=pid)
        print(pid)
        goodsort=good.storenums
        cart = Cart.objects.get(userAccount=userid, productid=pid,orderid=1)
        if goodsort>cart.productnum:
            cart.productnum+=1
            cart.productprice=round(cart.productnum * good.price,2)
            cart.save()
            chose = Cart.objects.filter(userAccount=userid, isChose=True,orderid=1)
            totalPrice = 0
            for item in chose:
                totalPrice += item.productprice
            totalPrice=round(totalPrice,2)
            return JsonResponse({"data": cart.productnum, "status": "success","price":cart.productprice,"totalprice":totalPrice})
        else:
            return JsonResponse({"status": "error"})
    # 减少购物车
    if id=="3":
        goodsort=good.storenums
        cart = Cart.objects.get(userAccount=userid, productid=pid,orderid=1)
        if cart.productnum>0:
            cart.productnum-=1
            cart.productprice = round(cart.productnum * good.price ,2)
            cart.save()
            chose = Cart.objects.filter(userAccount=userid, isChose=True,orderid=1)
            totalPrice = 0
            for item in chose:
                totalPrice += item.productprice
                totalPrice = round(totalPrice, 2)
            return JsonResponse({"data": cart.productnum, "status": "success","price":cart.productprice,"totalprice":totalPrice})
        else:
            return JsonResponse({"status": "error"})
    if id=="4":
        cart = Cart.objects.get(userAccount=userid, productid=pid,orderid=1)
        cart.delete()
        return JsonResponse({"status":"success"})

def changeaddress(request,id):
    if id=="1":
        if request.method=="POST":
            userId=request.session.get("myid")
            receiver=request.POST.get("receiver")
            detailAddress=request.POST.get("detailAddress")
            phoneNum=request.POST.get("phoneNum")
            postalCode=request.POST.get("postalCode")
            a=Address.createAddress(userId,receiver,phoneNum,detailAddress,postalCode,False,False)
            a.save()
            return redirect("/place_order/")
        else:
            return render(request,"ttsx/user_center_site.html")
    if id=="2":
        addid=request.POST.get("addid")
        print(addid)
        ad=Address.objects.all()
        for item in ad:
            if item.id==int(addid):
                item.isUsed=True
            else:
                item.isUsed=False
            item.save()
        return JsonResponse({"status":"success"})

def makeorder(request):
    if request.method=="POST":
        payway=request.POST.get("payway")
        userId=request.session.get("myid")
        now_time = datetime.datetime.now() + datetime.timedelta(hours=8)
        t1 = datetime.datetime.strftime(now_time, '%m%d%H%M%S')
        # orderId=userId+"-"+t1
        orderId=int(t1)
        o=Order.createOrder(userId,orderId,payway,False,'','')
        o.save()
        c=Cart.objects.filter(userAccount=userId,isChose=True,isDelete=False,productnum__gt=0,orderid=1)
        for item in c:
            item.orderid=Order.objects.get(orderId=orderId)
            item.save()
        return JsonResponse({"data":orderId,"status":"success"})








