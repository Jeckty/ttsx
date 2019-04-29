from django.shortcuts import render,HttpResponse,redirect
from . models import FoodTypes,Goods,User
from django.http import JsonResponse
import time,random

# Create your views here.
def login(request):
    return render(request,"ttsx/login.html")
def cart(request):
    return render(request,"ttsx/cart.html")
def detail(request):
    return render(request,"ttsx/detail.html")
def index(request):
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
    return render(request,"ttsx/index.html",{"typeList":allList})
def list(request):
    return render(request,"ttsx/list.html")
def place_order(request):
    return render(request,"ttsx/place_order.html")
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
        request.session["usertoken"]=userToken
        return redirect("/user_center_info/")

    else:
        return render(request,"ttsx/register.html")
def user_center_info(request):
    try:
        username=request.session.get("myname")
        return render(request,"ttsx/user_center_info.html",{"username":username})
    except:
        return render(request, "ttsx/user_center_info.html")

def user_center_order(request):
    return render(request,"ttsx/user_center_order.html")
def user_center_site(request):
    return render(request,"ttsx/user_center_site.html")
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
            request.session["usertoken"]=usertoken
            return JsonResponse({"data": "登陆成功", "status": "success"})
    else:
        return redirect("/login/")





