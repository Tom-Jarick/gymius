var timer = setInterval("mytimer()",1000);
var inputValue = document.getElementById("duration").nodeValue;
seconds = 100;
function mytimer()
{
document.getElementById("div_timer").innerHTML = seconds; // this is the same as $("div_timer").html(timer) in       jquery.
seconds--;
} 