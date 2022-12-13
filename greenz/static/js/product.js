function allPrice(){
  var num=document.getElementById("number").value;
  var one=document.getElementById("product1").innerHTML;
  var price=(parseInt(num))*(parseInt(one));

  document.getElementById("private").innerHTML=price;
}

function Carting(){
  var name=document.getElementById("product").innerHTML;
  var sum=document.getElementById("private").innerHTML;
  var num=document.getElementById("number").value;

  alert('Purchased goods : '+name+'\n'+'Number : '+num+'\n'+'Sum : '+sum+'\n');


}
