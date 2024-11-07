function onClickedEstimatePrice(){
   console.log("estimated price button clicked");
   var sqft = document.getElementById("uiSqft");
   var bhk = getBHKValue();
   var bath = getBathValue();

   var locations = document.getElementById("uiLocations");
   var estPrice = document.getElementById("uiEstimatedPrice");
   var url = "http://127.0.0.1:5000//predict_home_price";

   $.post(url,{
    total_sqft:parseFloat(sqft.value),
    bhk:bhk,
    bath:bath,
    location:locations.value

   },function(data,status)
{
    console.log(data.estimated_price);
    uiEstimatedPrice.style.display = "flex";
    estPrice.innerHTML = "<h2>"+data.estimated_price.toString()+"Lakh</h2>";
    console.log(status);
});

}
function getBHKValue()
{
   var bhk = document.getElementsByName("uiBHK");
   for(var i in bhk)
   {
    if (bhk[i].checked)
    {
        console.log(`value is ${i} + 1`)
        return parseInt(i)+1;
    }
    else {
        return 0;
    }
   }
}
function getBathValue()
{
  var  uiBath = document.getElementsByName("uiBathrooms")
  for ( var i in uiBath )
  {
    if(uiBath[i].checked)
    {
        return parseInt(i)+1;
    }
    else {
        return 0;
        }
  }
}



function onPageLoad() {
    console.log("document Loaded");
     var url = "http://127.0.0.1:5000/get_location_names";
    
    $.get(url, function (data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $(uiLocations).empty();  
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $(uiLocations).append(opt);
            }
        }
    });
}

window.onload = onPageLoad();
