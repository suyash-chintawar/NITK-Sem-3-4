//validates all fields using switch case
function validate(field) {
	var fname= field.name;
	var re_email =/^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+.com$/;
	var re_uname =/[a-zA-Z0-9_]{6,}/;
	var re_pswd = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%&*_-])[a-zA-Z0-9@#$%&*_-]{6,}$/;
	var re_pincode=/[0-9]{6}/;
	var re_name=/[a-zA-Z0-9_ ]{2,}/;
	var re_contact=/[6-9][0-9]{9}/;
	switch(fname)
	{
		case "email"://for email field
			if(re_email.test(field.value))
			{
				field.style.border="solid 5px #46ab43";
				document.getElementById("valid_email").innerHTML="&#9989";
				return true;
			}
			else	
			{
				field.style.border="solid 5px red";
				document.getElementById("valid_email").innerHTML="&#10062";
				return false;
			}	
		break;
		case "uname"://for username field
			if(re_uname.test(field.value)) 
			{
				field.style.border="solid 5px #46ab43";
				document.getElementById("valid_uname").innerHTML="&#9989";
				return true;
			}
			else
			{
				field.style.border="solid 5px red";
				document.getElementById("valid_uname").innerHTML="&#10062";
				return false;
			}
		break;
		case "name"://for name field(differs from uname in presence of space)
			if(re_name.test(field.value)) 
			{
				field.style.border="solid 5px #46ab43";
				document.getElementById("valid_name").innerHTML="&#9989";
				return true;
			}
			else
			{
				field.style.border="solid 5px red";
				document.getElementById("valid_name").innerHTML="&#10062";
				return false;
			}
		break;
		case "pswd"://for password field
			if(re_pswd.test(field.value))
			{
				field.style.border="solid 5px #46ab43";
				document.getElementById("valid_pswd").innerHTML="&#9989";
				return true;
			}
			else	
			{
				field.style.border="solid 5px red";
				document.getElementById("valid_pswd").innerHTML="&#10062";
				return false;
			}	
		break;
		case "cfmpswd"://for confirm password field
			if(re_pswd.test(field.value)) 
			{
				field.style.border="solid 5px #46ab43";
				document.getElementById("valid_cfmpswd").innerHTML="&#9989";
				return true;
			}
			else
			{
				field.style.border="solid 5px red";
				document.getElementById("valid_cfmpswd").innerHTML="&#10062";
				return false;
			}
		break;
		case "pincode"://for pincode field
			if(re_pincode.test(field.value)) 
			{
				field.style.border="solid 5px #46ab43";
				document.getElementById("valid_pincode").innerHTML="&#9989";
				return true;
			}
			else
			{
				field.style.border="solid 5px red";
				document.getElementById("valid_pincode").innerHTML="&#10062";
				return false;
			}
		break;
		case "contact"://for mobile number
			if(re_contact.test(field.value))
			{
				field.style.border="solid 5px #46ab43";
				document.getElementById("valid_contact").innerHTML="&#9989";
				return true;
			}
			else	
			{
				field.style.border="solid 5px red";
				document.getElementById("valid_contact").innerHTML="&#10062";
				return false;
			}	
		break;
	}
}

//validation of signup form
function signup_validation(form) {
	//check for null
	if(form.pswd.value=="" || form.cfmpswd.value=="" || form.email.value=="" || form.uname.value=="")
	{
		alert("Please fill all fields!!");
		return false;
	}
	//if not null re-check input fields
	if(!validate(form.uname))
	{
		alert("Username format invalid!!");
		form.uname.value="";
		return false;
	}
	if(!validate(form.email))
	{
		alert("Email format invalid!!");
		form.email.value="";
		return false;
	}
	if(!validate(form.pswd) && !validate(form.cfmpswd))
	{
		alert("Password format invalid!!");
		form.pswd.value="";
		form.cfmpswd.value="";
		return false;
	}
	if(form.pswd.value != form.cfmpswd.value)
	{
		alert("Passwords don't match!!");
		form.pswd.value="";
		form.cfmpswd.value="";
		return false;
	}
	//check whether checkbox is selected
	if(!form.terms.checked)
	{
		alert("Terms of service not accepted!!");
		return false;
	}
	//radio button validation
	var radioGroup = form.gender;
    var genderCheck = false;

    var i = 0;
    while (!genderCheck && i < radioGroup.length) {
        if (radioGroup[i].checked) genderCheck = true;
        i++;        
    }

    if (!genderCheck) 
    {
   		alert("Please select gender!!");
   		return false;
   	}
   	confirm("Do you want to submit the form?");
  	alert("SUCCESSFULLY SUBMITTED!");
}

//validation of login form
function login_validation(form) {
	if(form.pswd.value=="" || form.uname.value=="")
	{
		alert("Please fill all fields!!");
		return false;
	}
	if(!validate(form.uname))
	{
		alert("Username format invalid!!");
		form.uname.value="";
		return false;
	}
	if(!validate(form.pswd))
	{
		alert("Password format invalid!!");
		form.pswd.value="";
		return false;
	}
	confirm("Do you want to submit the form?");
  	alert("SUCCESSFULLY SUBMITTED!");
}

//validation of demo details form(in demo.html)
function demo_validation(form) {
	if(form.name.value=="" || form.contact.value=="" || form.address.value=="" || form.pincode.value=="")
	{
		alert("Please fill all fields!!");
		return false;
	}
	if(!validate(form.name))
	{
		alert("Name format invalid!!");
		form.name.value="";
		return false;
	}
	if(!validate(form.contact))
	{
		alert("Contact no. format invalid!!");
		form.contact.value="";
		return false;
	}
	if(!validate(form.pincode))
	{
		alert("Pincode format invalid!!");
		form.pincode.value="";
		return false;
	}
	var radioGroup = form.cod;
    var  codCheck = false;

    var i = 0;
    while (!codCheck && i < radioGroup.length) {
        if (radioGroup[i].checked) codCheck = true;
        i++;        
    }

    if (!codCheck) 
  	{
  		alert("Please select yes/no for Pay on Delivery!!");
  		return false;
  	}
  	confirm("Do you want to submit the form?");
  	alert("SUCCESSFULLY SUBMITTED!");
  	prompt("How was your experience?","Your review");
}

//for current date and time 
function startTime() {
	var today = new Date();
	var dd =today.getDate();
	var mm = today.getMonth()+1;
	var yyyy = today.getFullYear();
	var hr = today.getHours();
	var min = today.getMinutes();
	var sec = today.getSeconds();
	hr= check(hr);
	min= check(min);
	sec= check(sec);
	dd= check(dd);
	mm= check(mm);
	document.getElementById("time").innerHTML = dd+'/'+mm+'/'+yyyy+"  "+hr+":"+min+":"+sec;
	var t=setTimeout(startTime, 1000);
}

//check if value is less than 10 to append extra zero at start
function check(i) {
		if (i<10) i=("0"+i);
		return i;
}

//image slider
var i=0;
var images=[];
images[0]="assets/images/iphone12pro.png";
images[1]="assets/images/img2.png";
images[2]="assets/images/img3.png";
function changeImg() {
	document.imgslider.src=images[i];
	if(i<images.length-1)
	{
		i++;
	}
	else{
		i=0;
	}
	setTimeout(changeImg,3000);//change image every 3 seconds
}

//create a cookie
function setCookie(uname,exdays,count1) {
	var d = new Date();
  	d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  	var expires = "expires="+d.toGMTString();
  	document.cookie="username="+String(uname);
  	document.cookie="count="+String(count1);
}

//check value in name-value pair of cookie
function getCookie(cname) {
	var name = cname;
  	var ca = document.cookie.split(';');
  	var flag=0;
  	for(var j = 0; j < ca.length; j++) {
    var c = ca[j];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
     	res= c.substring(name.length, c.length);
     	flag=1;
     	break;
    }
  }
  if(flag==1) return res;
  else return "";
}

//check whether username is present or not
function checkCookie(uname) {
	var user = getCookie("username=");
	if(user!="" && user==uname)
	{
		return true;
	}
	else return false;
}

//called in home page once loaded to store cookies
function home() {
	var uname = prompt("Enter your name","name");
	var check = checkCookie(uname);
	if(!check)
	{
		setCookie(uname,30,1);
		alert("Hello "+uname+"! This is your first visit!");
	}
	else 
	{
		var cnt = getCookie("count=");
		setCookie(uname,30,parseInt(cnt)+1);
		var cnt1= getCookie("count=");
		var temp="Hello "+uname+"! You have visited this page "+cnt1+" times!";
		alert(temp);
		
	}
}

