function sendMail(){
     var params = {
         name: document.getElementById("").value,
         email: document.getElementById("mails").value,
         message: document.getElementById("").value,


     };
     const serviceID = "service_gfph1lm"
     const templateID = "template_661q1io"
     emailjs.send(serviceID,templateID,params)
     .then((res) => {
         document.getElementById("").value = "",
         document.getElementById("").value = "",
         document.getElementById("").value = "",
         console.log(res);
         alert("success")
      })
    .catch((err) => console.log(err));
}

