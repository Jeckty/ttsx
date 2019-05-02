$(document).ready(function () {
    // alert("****")
    // var check=document.getElementsByClassName("checked")
    // var checkbox=document.getElementsByClassName("checked")
    // for (var i=0;i<check.length;i++){
    //     check[i].addEventListener()
    // }

    $('.ck01').each(function(i,elemt){
        // this.checked=true
        $(this).change(function(){
            var ischecked = $(this).is(':checked');
            var pid=this.getAttribute("id")
            $.post("/changecart/1/",{"pid":pid,"value":ischecked},function () {})
            // $(this).siblings('input').prop("checked",ischecked);
        });
    })
    $('.ck02').change(function () {
        var ischecked2 = $(this).is(':checked');
        if(ischecked2==true){
            $('.ck01').each(function(i,elemt){
                this.checked=true
                var pid2=this.getAttribute("id")
                $.post("/changecart/1/",{"pid":pid2,"value":ischecked2},function () {})
            })
        }
    })
})
