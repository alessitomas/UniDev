$(document).ready(function () {

    $("#form-login").submit(function (event) {
      
      event.preventDefault();
   
  
      var settings = {
        "url": "login/",
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
  

        $("#ul-resp").append("<li>username:" + response.username + "</li>")
        $("#ul-resp").append("<li>senha:" + response.senha + "</li>")

  
      });
    });
  
    
  });