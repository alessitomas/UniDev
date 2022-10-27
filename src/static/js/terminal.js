// consumir uma API RESTful
// get the data from my local API 
fetch('http://127.0.0.1:5000/terminal').then(r =>{
    return r.json()
}) 
.then(corpo=>{
    document.getElementById("titulo").innerHTML = corpo.titulo
    document.getElementById("enunciado").innerHTML = corpo.enunciado
    document.getElementById("tela").innerHTML = corpo.tela
    document.getElementById("pytest").innerHTML = corpo.pytest


})


