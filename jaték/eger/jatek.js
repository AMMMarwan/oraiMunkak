div = document.createElement("div");
div.style.position = "absolute";
div.style.left = "0px";
div.style.top = "0px";
div.style.width = "100px";
div.style.height = "100px";
div.style.background = "red";
div.style.color = "blue";
div.style.borderRadius = "100%";
//div.style.border = "2px solid blue";
document.body.appendChild(div);

talalt = 0
katt = 0
div.addEventListener('click', function (e) {
    talalt++;
    w = div.style.width.valueOf().replace("px","")
    document.getElementById("katt").innerHTML = "Talált: "
    +talalt
    if (talalt % 5 == 0 ) {
        div.style.width = w*0.75+"px"
        div.style.height = w*0.75+"px"

    }
})
document.addEventListener('mouseup', function (e) {
    katt++
    document.getElementById("kattint").innerHTML="Kattintva: " +katt
})
var h = setInterval(function(){
    div.style.left = Math.floor(Math.random()*400)+'px'
    div.style.top = Math.floor(Math.random()*400)+'px'
},1000)