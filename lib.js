function sendCnpj(){
  var JSONObject = {
    "nome":"John Johnson",
    "age":33,
    "phone":"555 1234567"
  };
  document.getElementById("jname").innerHTML = JSONObject.nome 
  document.getElementById("jage").innerHTML = JSONObject.age
  document.getElementById("jphone").innerHTML = JSONObject.phone 
  for(i = 0; i < document.all.length; i++){
    alert(document.all(i).tagName);
  }
  return true;
  //term = document.forms["form"].q.value.replace(/[^0-9]/g, "")
}
    