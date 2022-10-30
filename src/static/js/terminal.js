// consumir uma API RESTful
// get the data from my local API 



// make a variable with value 1
// + localStorage.getItem('id_user_ativo') + "/curso/" + localStorage.getItem('id_curso_ativo')
// print the variable
console.log('http://127.0.0.1:5000/terminal/' + localStorage.getItem('id_user_ativo') + "/curso/" + localStorage.getItem('id_curso_ativo'), "testeeeeeeeeee");


fetch('http://127.0.0.1:5000/terminal/'+localStorage.getItem('id_user_ativo').toString()+'/curso/'+localStorage.getItem('id_curso_ativo').toString()).then(r =>{
    return r.json()
}) 



.then(corpo=>{
    localStorage.setItem('tela', corpo.tela)
    document.getElementById("titulo").innerHTML = corpo.titulo
    document.getElementById("enunciado").innerHTML = corpo.enunciado
    document.getElementById("tela").innerHTML = corpo.tela

})

$(document).ready(function () {

    $(function () {

      var settings = {
        "url": 'http://127.0.0.1:5000/terminal/'+localStorage.getItem('id_user_ativo').toString()+'/curso/'+localStorage.getItem('id_curso_ativo').toString(),
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