/**
 * Created by zty-c on 2019/4/28.
 */
$(document).ready(function () {

    $("input.input_submit").click(function () {
        var username=$("#name_input").val();
        var pwd=$("#pass_input").val();

        $.post("/checklogin/",{"username":username,"pwd":pwd},function (data) {
                if(data.status=="success"){
                    self.location="/user_center_info/"
                }else{
                     window.location.reload();
                }
        })
    })
})