// consumir uma API RESTful
// get the data from my local API 



// make a variable with value 1
var i = 1;


fetch('http://127.0.0.1:5000/terminal/' + i.toString() ).then(r =>{
    return r.json()
}) 
.then(corpo=>{
    document.getElementById("titulo").innerHTML = corpo.titulo
    document.getElementById("enunciado").innerHTML = corpo.enunciado
    document.getElementById("tela").innerHTML = corpo.tela
    document.getElementById("pytest").innerHTML = corpo.pytest


})


