// consumir uma API RESTful
// get the data from my local API 



// make a variable with value 1
// + localStorage.getItem('id_user_ativo') + "/curso/" + localStorage.getItem('id_curso_ativo')
// print the variable

if (localStorage.getItem('primeira_vez').toString() == "true") {
  

    fetch('http://127.0.0.1:5000/terminal/'+localStorage.getItem('id_user_ativo').toString()+'/curso/'+localStorage.getItem('id_curso_ativo').toString()).then(r =>{
        return r.json()
    }) 
    .then(corpo=>{
        if(corpo.curso_finalizado){
            window.location.href = "http://127.0.0.1:5000/paginafinal/"
            }
        else{
            localStorage.setItem('tela', corpo.tela)
            document.getElementById("titulo").innerHTML = corpo.titulo
            document.getElementById("enunciado").innerHTML = corpo.enunciado
            document.getElementById("tela").innerHTML = corpo.tela
        }
    })

}
else {

    fetch('http://127.0.0.1:5000/mudarpg/'+localStorage.getItem('id_user_ativo').toString()+'/curso/'+localStorage.getItem('id_curso_ativo').toString()+ '/exercicio/' +localStorage.getItem('tela').toString()).then(r =>{
        return r.json()
    }) 
    .then(corpo=>{
        if(corpo.curso_finalizado){
            window.location.href = "http://127.0.0.1:5000/paginafinal/"
            }
        else{
            localStorage.setItem('tela', corpo.tela)
            document.getElementById("titulo").innerHTML = corpo.titulo
            document.getElementById("enunciado").innerHTML = corpo.enunciado
            document.getElementById("tela").innerHTML = corpo.tela 
        }
        })


}

function sendtela() {
    if (document.getElementById('code').value!="" && parseInt(localStorage.getItem('tela'))<= parseInt(localStorage.getItem('telas_curso_ativo')) ){
      window.location.reload();
      var xhr = new XMLHttpRequest();
      localStorage.setItem("primeira_vez", false);
      xhr.open("POST", 'http://127.0.0.1:5000/terminal/'+localStorage.getItem('id_user_ativo').toString()+'/curso/'+localStorage.getItem('id_curso_ativo').toString()+ '/exercicio/' +localStorage.getItem('tela').toString(), true);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.send(JSON.stringify({
      'exr': document.getElementById('code').value
    }));
    localStorage.setItem("tela", parseInt(localStorage.getItem('tela'))+1);
        }
    else{
      console.log("aquiiiiiiiiii");
        }
  }


function voltar() {
    localStorage.setItem("primeira_vez", false);
    if (parseInt(localStorage.getItem('tela'))>1){
      localStorage.setItem("tela", parseInt(localStorage.getItem('tela'))-1);
    }

    window.location.reload()
  }

