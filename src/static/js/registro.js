$(document).ready(function () {

    $("#meu-form").submit(function (event) {
      
      event.preventDefault();
  
   
  
      var settings = {
        "url": "usuario/",
        "method": "POST",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/json"
        },
        "data": JSON.stringify({
          "nome": $("#nome").val(),
          "username": $("#username").val(),
          "email": $("#email").val(),
          "senha": $("#senha").val()
        }),
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
  

        $("#ul-resp").append("<li>nome:" +' ' +response.nome + "</li>")
        $("#ul-resp").append("<li>username:" +' '+ response.username + "</li>")
        $("#ul-resp").append("<li>email:" +' '+ response.email + "</li>")

  
      });
    });
  
    
  });