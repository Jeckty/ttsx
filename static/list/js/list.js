$(document).ready(function () {
    var add_goods=document.getElementsByClassName("add_goods")
    for(var i=0;i<add_goods.length;i++){
        add_goods[i].onclick=function () {
            pid=this.getAttribute("ga");
            $.post("/changecart/0/",{"pid":pid},function (data) {
                if(data.data=="-1"){
                    window.location.href = "http://127.0.0.1:8000/login/"
                }if(data.data=="1"){
                    window.location.reload();
                }if (data.data=="0"){
                    alert("加入购物车失败");
                }
            })
        }
    }

})
