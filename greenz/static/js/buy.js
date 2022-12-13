function selectEmail(ele){
    var $ele = $(ele);
    var $email2 = $('input[name=email2]');

    if($ele.val() == "1"){
        $email2.attr('readonly', false);
        $email2.val('');
    } else {
        $email2.attr('readonly', true);
        $email2.val($ele.val());
    }
}

function order(){

  var checkbox=document.getElementsByName("boxes");
  var msg="Payment Information";

  for(var i=0;i<checkbox.length;i++)
  {
    if(checkbox[i].checked)
    {
      if(i==0)
      {
        var s= document.getElementById("sel2");
        var v= document.getElementById("sel3");
        var x= document.getElementById("cardnum1").value;
        var cont=s.options[s.selectedIndex].value;
        var cons=v.options[v.selectedIndex].value;
        var st="Credit card"
        alert(msg+'\n'+'Payment method: '+st+'\n'+cont+'/'+cons+'/'+x);
        document.location.href="../templates/freshfood.html";
      }
      else if(i==1)
      {
        var s= document.getElementById("sel4");
        var cont=s.options[s.selectedIndex].value;
        var st="make a deposit"
        alert(msg+'\n'+'Payment method: '+st+'\n'+cont);
        document.location.href="../templates/freshfood.html";

      }
      else if(i==2)
      {
        var s= document.getElementById("sel5");
        var cont=s.options[s.selectedIndex].value;
        var st="account transfer"
        alert(msg+'\n'+'Payment method: '+st+'\n'+cont);
        document.location.href="../templates/freshfood.html";
      }
      else if(i==3)
      {
        var s= document.getElementById("sel6");
        var cont=s.options[s.selectedIndex].value;
        var x= document.getElementById("phone").value;
        var st="Mobile phone payment"
        alert(msg+'\n'+'Payment method: '+st+'\n'+cont+'/'+x);
        document.location.href="../templates/freshfood.html";
      }
      }

  }

}
