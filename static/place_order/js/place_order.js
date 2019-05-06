$(document).ready(function () {
    $('.addre').each(function (i,elemt) {
        $(this).change(function () {
            var addid=this.getAttribute("id")
            $.post("/changeaddress/2/",{"addid":addid},function (data) { })
        })
    });
    $('#order_btn').click(function () {
        var payway= $("input[name='pay_style']:checked").val();
        $.post("/makeorder/",{"payway":payway},function (data) {
            if (data.status=="success"){
                alert("订单提交成功,订单号："+data.data);
                window.location.href="http://127.0.0.1:8000/user_center_order/"
            }
        })
    })
})