// consumir uma API RESTful
// get the data from my local API 



// make a variable with value 1
// + localStorage.getItem('id_user_ativo') + "/curso/" + localStorage.getItem('id_curso_ativo')
// print the variable

if (localStorage.getItem('primeira_vez').toString() == "true") {
  

    fetch('https://insper-unidev.herokuapp.com/terminal/'+'1'+'/curso/'+localStorage.getItem('id_curso_ativo').toString()).then(r =>{
        return r.json()
    }) 
    .then(corpo=>{
        if(corpo.curso_finalizado){
            window.location.href = "https://insper-unidev.herokuapp.com/paginafinal/"
            }
        else{
            console.log("aquiiiiiiiiii sera?")
            localStorage.setItem('tela', corpo.tela)
            document.getElementById("titulo").innerHTML = corpo.titulo
            document.getElementById("enunciado").innerHTML = corpo.enunciado
            document.getElementById("tela").innerHTML = corpo.tela
        }
    })

}
else {

    fetch('https://insper-unidev.herokuapp.com/mudarpg/'+'1'+'/curso/'+localStorage.getItem('id_curso_ativo').toString()+ '/exercicio/' +localStorage.getItem('tela').toString()).then(r =>{
        return r.json()
    }) 
    .then(corpo=>{
        if(corpo.curso_finalizado){
            window.location.href = "https://insper-unidev.herokuapp.com/paginafinal/"
            }
        else{
            console.log("aquiiiiiiiiii foi?")
            localStorage.setItem('tela', corpo.tela)
            document.getElementById("titulo").innerHTML = corpo.titulo
            document.getElementById("enunciado").innerHTML = corpo.enunciado
            document.getElementById("tela").innerHTML = corpo.tela 
        }
        })


}

function sendtela() {
    console.log("aquiiiiiiiiii vaiii")
    if (document.getElementById('code').value!="" && parseInt(localStorage.getItem('tela'))<= parseInt(localStorage.getItem('telas_curso_ativo')) ){
      window.location.reload();
      var xhr = new XMLHttpRequest();
      localStorage.setItem("primeira_vez", false);
      xhr.open("POST", 'https://insper-unidev.herokuapp.com/terminal/'+'1'+'/curso/'+localStorage.getItem('id_curso_ativo').toString()+ '/exercicio/' +localStorage.getItem('tela').toString(), true);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.send(JSON.stringify({
      'exr': document.getElementById('code').value
      
    }));
    console.log('pfr')
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


  $(document).ready(function () {

    $(function () {

      var settings = {
        "url": 'http://insper-unidev.herokuapp.com/terminal/'+'1'+'/curso/'+localStorage.getItem('id_curso_ativo').toString(),
        "method": "GET",
        "timeout": 0
      };

      $.ajax(settings).done(function () {
        var x = localStorage.getItem('tela')
        $("head").append(`<py-env>
        - pytest
        - pytest-reportlog
        - paths:
          - ../static/main2.py
          - ../static/solution.py
          - ../static/test_${x}.py
      </py-env>`);
      $("body").append(` <py-script src="../static/main2.py" ouput="pytest-output">
      </py-script>`)    
    });
    });
});
