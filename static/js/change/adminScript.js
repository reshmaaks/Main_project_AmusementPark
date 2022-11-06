const togglePasswordOld = document.querySelector('#togglePasswordOld');//hide password id
const oldPassword = document.querySelector('#currPassword')
const newPassword = document.querySelector('#newPwd');
const confirmNewPassword = document.querySelector('#confirmNewPassword');
const togglePasswordNew = document.querySelector('#togglePasswordNew');
const togglePasswordNewConfirm = document.querySelector('#togglePasswordNewConfirm');

togglePasswordOld.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = currPassword.getAttribute('type') === 'password' ? 'text' : 'password';
    currPassword.setAttribute('type', type);
    // toggle the eye slash icon '/'
    this.classList.toggle('fa-eye-slash');
});

togglePasswordNew.addEventListener('click', function(e){
    const type = newPassword.getAttribute('type') === 'password' ? 'text' : 'password';
    newPassword.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

togglePasswordNewConfirm.addEventListener('click', function(e){
    const type = confirmNewPassword.getAttribute('type') === 'password' ? 'text' : 'password';
    confirmNewPassword.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

//         function addstationValid(){
//             var isValid=true;
//             var nameCityPattern =  /(^[A-Za-z]{3,16})([ ]{0,1})/;
//             var contactPattern = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
//             var emailPattern = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
//             var validStationname = document.getElementById("sname").value;
//             var validPlace = document.getElementById("place").value;
//             var validContact = document.getElementById("contact").value;
//             var validEmail = document.getElementById("email").value;

//             if(validStationname==null || validStationname==""){
//                 document.getElementById("stationnameValidate").innerHTML="Station Name Required";
//                 isValid=false;
//             }
//             else if(!validStationname.match(nameCityPattern)){
//                 document.getElementById("stationnameValidate").innerHTML="Invalid Name";
//                 isValid=false;
//             }

//              if(validPlace==null || validPlace==""){
//                 document.getElementById("placeValidate").innerHTML="Place Required";
//                 isValid=false;
//             }
//             else if(!validPlace.match(nameCityPattern)){
//                 document.getElementById("placeValidate").innerHTML="Invalid Place";
//                 isValid=false;
//             }
//             //contact validation on buttonClick
//             if(validContact==null || validContact==""){
//                 document.getElementById("cnoValidate").innerHTML="Contact Required";
//                 isValid=false;
//             }
//             else if(!validContact.match(contactPattern)){
//                 document.getElementById("cnoValidate").innerHTML="Invalid contact number";
//                 isValid=false;
//             }

//             //email validation on buttonClick
//             if(validEmail==null || validEmail==""){
//                 document.getElementById("emailValidate").innerHTML="Email Required";
//                 isValid=false;
//             }
//             else if(!validEmail.match(emailPattern)){
//                 document.getElementById("emailValidate").innerHTML="Invalid email";
//                 isValid=false;
//             }
//             return isValid;
//          }

// function stationnameValidate(){
//          var stationname = document.getElementById("sname").value;
//          var pattern =  /(^[A-Za-z]{3,16})([ ]{0,1})/;
//          isValid=true;
//          if(stationname.match(pattern)){
//             document.getElementById("stationnameValidate").innerHTML="";
//          }
//          else if(!stationname){
//             document.getElementById("stationnameValidate").innerHTML="Station Name Required";
//             isValid=false;
//          }
//          else{
//             document.getElementById("stationnameValidate").innerHTML="Invalid Name";
//             isValid=false;
//          }
//          return isValid;
//       }

// function placeValidate(){
//          var place = document.getElementById("place").value;
//          var pattern =  /^[a-zA-Z]+$/;
//          isValid=true;
//          if(place.match(pattern)){
//             document.getElementById("placeValidate").innerHTML="";
//          }
//          else if(!place){
//             document.getElementById("placeValidate").innerHTML="Place Required";
//             isValid=false;
//          }
//          else{
//             document.getElementById("placeValidate").innerHTML="Only characters are acceptable";
//             isValid=false;
//          }
//          return isValid;
//       }

//       function cnoValidate(){
//          var cno = document.getElementById("contact").value;
//          var pattern = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
//          isValid=true;
//          if(cno.match(pattern)){
//             document.getElementById("cnoValidate").innerHTML="";
//          }
//          else if(!cno){
//             document.getElementById("cnoValidate").innerHTML="Number required";
//             isValid=false;
//          }
//          else{
//             document.getElementById("cnoValidate").innerHTML="Invalid Contact Number";
//             isValid=false;
//          }
//          return isValid;
         
//       }

//       function emailValidate(){
//          var email = document.getElementById("email").value;
//          var pattern = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
//          isValid=true;
//          if(email.match(pattern)){
//             document.getElementById("emailValidate").innerHTML="";
//           }
//           else if(!email){
//             document.getElementById("emailValidate").innerHTML="Email Required";
//             isValid=false;
//          }
//           else{
//             document.getElementById("emailValidate").innerHTML="Invalid email";
//             isValid=false;
//           }
//           return isValid;
//       }

