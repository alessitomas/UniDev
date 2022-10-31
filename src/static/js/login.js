$(document).ready(function () {
  console.log("login.js loaded");
  $("#form-login").submit(function (event) {
    event.preventDefault();
    var settings = {
      "url": "/login",
      "method": "POST",
      "timeout": 0,
      "headers": {
        "Content-Type": "application/json"
      },
      "data": JSON.stringify({
        "id_user": $("#id_user").val()
      }),
    };
    // get response if status == True redirect 
    


    $.ajax(settings).done(function (response) {
      console.log(response.status);
      if (response.status) {

        localStorage.setItem('id_user_ativo',response.id_user);
        console.log('passou aq')
        console.log(localStorage.getItem('id_user_ativo'))
        window.location.href = "/cursos";

      }
    });
  });

  
});

