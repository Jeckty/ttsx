$(document).ready(function () {

    // 选择
    $('.ck01').each(function(i,elemt){
        // this.checked=true
        $(this).change(function(){
            var ischecked = $(this).is(':checked');
            var pid=this.getAttribute("id");
            $.post("/changecart/1/",{"pid":pid,"value":ischecked},function (data) {
                // 修改件数
                var chosenum=document.getElementById("ischose");
                chosenum.innerHTML=data.chosenum;
                // 修改总价
                var totalprice=document.getElementById("totalprice");
                totalprice.innerHTML=data.totalprice;
            })

        });
    });
    // 全选
    $('.ck02').change(function () {
        var ischecked2 = $(this).is(':checked');
        if(ischecked2==true){
            $('.ck01').each(function(i,elemt){
                this.checked=true;
                var pid2=this.getAttribute("id");
                $.post("/changecart/1/",{"pid":pid2,"value":ischecked2},function (data) {
                    // 修改件数
                    var chosenum=document.getElementById("ischose");
                    chosenum.innerHTML=data.chosenum;
                    // 修改总价
                    var totalprice=document.getElementById("totalprice");
                    totalprice.innerHTML=data.totalprice;
                })
            })
        }
    });
// 增加减少
    $('.num_add').each(function (i,elemt) {
        // 增加
        $(elemt).children(".add").click(function () {
            pid=this.getAttribute("ga");
            $.post("/changecart/2/",{"pid":pid},function (data) {
            if(data.status==="success"){
                $(elemt).children(".num_show").val(data.data);
                // $(elemt).parent().next().val(data.price)
                var xiaoji=document.getElementById(pid+"p");
                xiaoji.innerHTML=data.price;
                // 修改总价
                var totalprice=document.getElementById("totalprice");
                totalprice.innerHTML=data.totalprice;
                }

            })
        });
        // 减少
        $(elemt).children(".minus").click(function () {
                pid=this.getAttribute("ga");
                $.post("/changecart/3/",{"pid":pid},function (data) {
                if(data.status==="success"){
                    $(elemt).children(".num_show").val(data.data);
                    var xiaoji=document.getElementById(pid+"p");
                    xiaoji.innerHTML=data.price;
                    // 修改总价
                    var totalprice=document.getElementById("totalprice");
                    totalprice.innerHTML=data.totalprice;
                    }

                })
            })
    });
// 删除
    $('.del').each(function (i,elemt) {
        $(this).click(function () {
            pid=this.getAttribute("ga");
            $.post("/changecart/4/",{"pid":pid},function (data) {
                if (data.status=="success"){
                    window.location.reload();
                }
            })
        });
        // var del=document.getElementById(pid+"d");
        //         xiaoji.innerHTML=data.price
    })
});
