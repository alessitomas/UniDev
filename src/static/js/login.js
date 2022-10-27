$(document).ready(function () {

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
        console.log(response.status, 'testeeeeee');
        if (response.status) {

          localStorage.setItem('id_user_ativo',response.id_user);
          window.location.href = "/cursos";

        }



          
      });
    });
  
    
  });

