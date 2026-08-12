const canvas = document.getElementById("canvas");

const ctx = canvas.getContext("2d");

ctx.fillStyle = "black";

ctx.fillRect(0,0,280,280);

let drawing = false;

canvas.addEventListener("mousedown", () => drawing = true);

canvas.addEventListener("mouseup", () => drawing = false);

canvas.addEventListener("mousemove", draw);

function draw(e){

    if(!drawing) return;

    ctx.fillStyle = "white";

    ctx.beginPath();

    ctx.arc(
        e.offsetX,
        e.offsetY,
        10,
        0,
        Math.PI*2
    );

    ctx.fill();

}

function clearCanvas(){

    ctx.fillStyle="black";

    ctx.fillRect(0,0,280,280);

    document.getElementById("result").innerHTML="";
}

function predict(){

    let image = canvas.toDataURL();

    fetch("/predict",{

        method:"POST",

        headers:{
            "Content-Type":"application/x-www-form-urlencoded"
        },

        body:"image="+encodeURIComponent(image)

    })

    .then(res=>res.json())

    .then(data=>{

        document.getElementById("result").innerHTML=
        "Prediction : "+data.digit;

    });

}