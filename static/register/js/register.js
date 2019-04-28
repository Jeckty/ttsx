$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;
	var error_phone = false;
	var error_address = false;
	var error_id = false;

	$('#user_id').blur(function() {
		check_user_id();
		userid=this.value
		$.post("/checkid/",{"uesrid":userid},function (data) {
			if (data.status=="error"){
				alert("该账户已被注册，请重新输入账号")
			}
        })
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_id(){
		var len = $('#user_id').val().length;
		if(len<5||len>20)
		{
			$('#user_id').next().html('请输入5-20个字符的用户名')
			$('#user_id').next().show();
			error_id = true;
		}
		else
		{
			$('#user_id').next().hide();
			error_id = false;
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}

	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len>20)
		{
			$('#user_name').next().html('最长20位')
			$('#user_name').next().show();
			error_name = true;
		}
		else
		{
			$('#user_name').next().hide();
			error_name = false;
		}
	}

	function check_user_phone(){
		var len = $('#phonenum').val().length;
		if(len!=11)
		{
			$('#phonenum').next().html('请输入正确的电话号码')
			$('#phonenum').next().show();
			error_phone = true;
		}
		else
		{
			$('#phonenum').next().hide();
			error_phone = false;
		}
	}

	function check_user_address(){
		var len = $('#address').val().length;
		if(len>150||len==0)
		{
			$('#address').next().html('请输入正确的字符')
			$('#address').next().show();
			error_address = true;
		}
		else
		{
			$('#address').next().hide();
			error_address = false;
		}
	}

	$('form').submit(function() {

		check_user_id();
		check_user_name()
		check_pwd();
		check_cpwd();
		check_email();
		check_user_phone();
		check_user_address()

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false&&error_phone== false&&error_address == false&&error_id == false)
		{
                return true;
        }
		else
		{
			alert("请正确输入信息")
			return false;

		}

	});








})