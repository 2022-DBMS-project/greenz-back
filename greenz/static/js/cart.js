
function CalCountplus(seq){
  var id;
  var all_money;
  var money;
  if(parseInt(seq)==1)
  {
    id="cart_count1";
    all_money="cart_price1";
    money=2800;
  }
  else if(parseInt(seq)==2)
  {
    id="cart_count2";
    all_money="cart_price2";
    money=2682;
  }
  else if(parseInt(seq)==3)
  {
    id="cart_count3";
    all_money="cart_price3";
    money=1990;
  }
  else if(parseInt(seq)==4)
  {
    id="cart_count4";
    all_money="cart_price4";
    money=5480;
  }
  else if(parseInt(seq)==5)
  {
    id="cart_count5";
    all_money="cart_price5";
    money=4980;
  }
  var price=parseInt(document.getElementById(id).value);

  document.getElementById(id).value=price+1;

  var num=document.getElementById(id).value;
  var allprice=(parseInt(num))*parseInt(money);
  document.getElementById(all_money).innerHTML=allprice;

  document.getElementById("sk").innerHTML=parseInt(document.getElementById("sk").innerHTML)+parseInt(money);
  document.getElementById("result_price").innerHTML=parseInt(document.getElementById("sk").innerHTML)+2000;

}

function CalCountminus(seq){

  var id;
  var all_money;
  var money;
  if(parseInt(seq)==1)
  {
    id="cart_count1";
    all_money="cart_price1";
    money=2800;
  }
  else if(parseInt(seq)==2)
  {
    id="cart_count2";
    all_money="cart_price2";
    money=2682;
  }
  else if(parseInt(seq)==3)
  {
    id="cart_count3";
    all_money="cart_price3";
    money=1990;
  }
  else if(parseInt(seq)==4)
  {
    id="cart_count4";
    all_money="cart_price4";
    money=5480;
  }
  else if(parseInt(seq)==5)
  {
    id="cart_count5";
    all_money="cart_price5";
    money=4980;
  }

  var price=parseInt(document.getElementById(id).value);

  document.getElementById(id).value=price-1;

  var num=document.getElementById(id).value;
  var allprice=(parseInt(num))*parseInt(money);
  document.getElementById(all_money).innerHTML=allprice;

  document.getElementById("sk").innerHTML=parseInt(document.getElementById("sk").innerHTML)-parseInt(money);
  document.getElementById("result_price").innerHTML=parseInt(document.getElementById("sk").innerHTML)+2000;

}
function recipe()
{
  alert('You can make vegan tofu sandwiches! \nDo you want to go to the recipe page?');
  document.location.href="../templates/Recipe5.html";
}
