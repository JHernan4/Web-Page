function main(){
  var vUName = checkUsername();
  var vMail = checkEmail();
  var vPass = checkPassword();
  var vAge = checkAge();
  var vName = checkName();
  var vS1 = checkSurname1();
  var vS2 = checkSurname2();
  var vPhone = checkPhone();


  document.getElementById('error').innerHTML = "";
  if(vUName==true && vMail==true && vPass==true && vAge==true && vName==true && vS1==true && vS2==true && vPhone==true){
    document.getElementById("error").innerHTML = "Enviando"
    document.getElementById("registrator").submit();
  }else{
    document.getElementById("error").innerHTML = "Revise los campos marcados con rojo."
  }

}

function checkUsername(){
  var elem = document.getElementById("username")
  var username = elem.value
  if(username.length <= 2 || username == ""){
    elem.style.borderColor = "red"
    return false;
  }else{
    elem.style.borderColor = "green"
    return true;
  }
}

function checkEmail(){
  var regexemail = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  var elem = document.getElementById("email")
  var email = elem.value
  if (email == "" || !regexemail.test(email)) {
    elem.style.borderColor = "red";
    return false;
  }else {
    elem.style.borderColor = "green";
    return true;
  }
}

function checkPassword(){
  var regexpass = /^[A-Za-z]\w{7,14}$/;
  var elem = document.getElementById("password")
  var password = elem.value
  if(password == "" || !regexpass.test(password)){
    elem.style.borderColor="red";
    return false;
  }else{
    elem.style.borderColor="green";
    return true;
  }
}

function checkAge(){
  var elem = document.getElementById("age")
  var age = elem.value

  if(age == "" || isNaN(age)){
    elem.style.borderColor = "red"
    return false
  }else{
    elem.style.borderColor = "green"
    return true
  }
}

function checkSurname1(){
  var elem1 = $("#surname1")
  var sur1 = elem1.val()

  if(sur1 == ""){
    elem1.css("borderColor", "red")
    return false
  }else{
    elem1.css("borderColor", "green")
    return true
  }
}

function checkSurname2(){
  var elem2 = $("#surname2")
  var sur2 = elem2.val()

  if(sur2==""){
    elem2.css("borderColor", "red")
    return false
  }else{
    elem2.css("borderColor", "green")
    return true
  }
}

function checkName(){
  var elem = $("#name")
  var name = elem.val()

  if(name==""){
    elem.css("borderColor", "red")
    return false
  }else{
    elem.css("borderColor", "green")
    return true
  }
}

function checkPhone(){
  var elem = document.getElementById("phone")
  var phone = elem.value

  if(phone.length != 9 || isNaN(phone)){
    elem.style.borderColor = "red"
    return false
  }else{
    elem.style.borderColor = "green"
    return true
  }
}
