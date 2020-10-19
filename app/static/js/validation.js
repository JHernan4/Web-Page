function main(){
  var vName = checkUsername();
  var vMail = checkEmail();
  var vPass = checkPassword();


  document.getElementById('error').innerHTML = "";
  if(vName==true && vMail==true && vPass==true){
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
  var elem = $("#password")
  var password = elem.val()
  if(password == "" || !!regexpass.test(password)){
    elem.css("borderColor", "red")
    return false;
  }else{
    elem.css("borderColor", "green")
    return true;
  }
}
