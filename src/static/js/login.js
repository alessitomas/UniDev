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

          "username": $("#username").val(),
          "senha": $("#senha").val()
        }),
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
  

        $("#ul-resp").append("<li>nome:" + response.nome + "</li>")
        $("#ul-resp").append("<li>username:" + response.isbn + "</li>")
        $("#ul-resp").append("<li>email:" + response.nome + "</li>")

  
      });
    });
  
    
  });