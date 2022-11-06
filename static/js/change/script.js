const signUpButton = document.getElementById('signUp');//overlay
const signInButton = document.getElementById('signIn');//overlay
const container = document.getElementById('container');//overlay
const togglePassword = document.querySelector('#togglePassword');//hide password id
const password = document.querySelector('#loginPassword');
const rpwd = document.querySelector('#password');
const rcpwd = document.querySelector('#cpassword');
const togglePasswordReg = document.querySelector('#togglePasswordReg');
const togglePasswordRegConfirm = document.querySelector('#togglePasswordRegConfirm');

togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon '/'
    this.classList.toggle('fa-eye-slash');
});

togglePasswordReg.addEventListener('click', function(e){
    const type = rpwd.getAttribute('type') === 'password' ? 'text' : 'password';
    rpwd.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

togglePasswordRegConfirm.addEventListener('click', function(e){
    const type = rcpwd.getAttribute('type') === 'password' ? 'text' : 'password';
    rcpwd.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

signUpButton.addEventListener('click', () => {
   container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
   container.classList.remove("right-panel-active");
});

      //Registration button click
        function registerValid(){
            var isValid=true;
            var nameCityPattern =  /^[a-zA-Z]+$/;
            var pwdPattern=/^(?=.*\d)(?=.*[A-Z]).{6,}/;
            var contactPattern = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
            var emailPattern = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
            var validFirstname = document.getElementById("fname").value;
            var validLastname = document.getElementById("lname").value;
            var validCity = document.getElementById("city").value;
            var validContact = document.getElementById("contact").value;
            var validEmail = document.getElementById("email").value;
            var validPassword1 = document.getElementById("password").value;
            var validPassword2 = document.getElementById("cpassword").value;

           //firstName validation on buttonClick
            if(validFirstname==null || validFirstname==""){
                document.getElementById("fnameValidate").innerHTML="First Name Required";
                isValid=false;
            }
            else if(!validFirstname.match(nameCityPattern)){
                document.getElementById("fnameValidate").innerHTML="Only characters are acceptable";
                isValid=false;
            }

            //lastName validation on buttonClick
            if(validLastname==null || validLastname==""){
                document.getElementById("lnameValidate").innerHTML="Last Name Required";
                isValid=false;
            }
            else if(!validLastname.match(nameCityPattern)){
                document.getElementById("lnameValidate").innerHTML="Only characters are acceptable";
                isValid=false;
            }

            //city validation on buttonClick
            if(validCity==null || validCity==""){
                document.getElementById("cityValidate").innerHTML="City Required";
                isValid=false;
            }
            else if(!validCity.match(nameCityPattern)){
                document.getElementById("cityValidate").innerHTML="Invalid City";
                isValid=false;
            }

            //contact validation on buttonClick
            if(validContact==null || validContact==""){
                document.getElementById("contactValidate").innerHTML="Contact Required";
                isValid=false;
            }
            else if(!validContact.match(contactPattern)){
                document.getElementById("contactValidate").innerHTML="Invalid contact number";
                isValid=false;
            }

            //email validation on buttonClick
            if(validEmail==null || validEmail==""){
                document.getElementById("emailValidate").innerHTML="Email Required";
                isValid=false;
            }
            else if(!validEmail.match(emailPattern)){
                document.getElementById("emailValidate").innerHTML="Invalid email";
                isValid=false;
            }

            //password validation on buttonClick
            if(validPassword1==null || validPassword1==""){
                document.getElementById("passwordValidate").innerHTML="Password Required";
                isValid=false;
            }
            else if(!validPassword1.match(pwdPattern)){
                alert("Password should have atleast 8 characters with one alphaneumeric, one uppercase and one lowercase");
                isValid=false;
            }

            //confirm password on buttonClick
            if(validPassword2==null || validPassword2==""){
                document.getElementById("cpasswordValidate").innerHTML="Password Required";
                isValid=false;
            }
            else if(validPassword1!=validPassword2){
                document.getElementById("cpasswordValidate").innerHTML="Enter same password";
                isValid=false;
            }
            else if(!validPassword2.match(pwdPattern)){
                alert("Password should have atleast 8 characters with one alphaneumeric, one uppercase and one lowercase");
                isValid=false;
            }
            return isValid;
        }

        //validate first name with various conditions
      function fnameValidate(){
         var firstname = document.getElementById("fname").value;
         var pattern =  /^[a-zA-Z]+$/;
         isValid=true;
         if(firstname.match(pattern)){
            document.getElementById("fnameValidate").innerHTML="";
         }
         else if(!firstname){
            document.getElementById("fnameValidate").innerHTML="First Name Required";
            isValid=false;
         }
         else{
            document.getElementById("fnameValidate").innerHTML="Only characters are acceptable";
            isValid=false;
         }
         return isValid;
      }

      function lnameValidate(){
         var lastname = document.getElementById("lname").value;
         var pattern =  /^[a-zA-Z]+$/;
         isValid=true;
         if(lastname.match(pattern)){
            document.getElementById("lnameValidate").innerHTML="";
         }
         else if(!lastname){
            document.getElementById("lnameValidate").innerHTML="Last Name Required";
            isValid=false;
         }
         else{
            document.getElementById("lnameValidate").innerHTML="Only characters are acceptable";
            isValid=false;
         }
         return isValid;
      }

      function emailValidate(){
         var email = document.getElementById("email").value;
         var pattern = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
         isValid=true;
         if(email.match(pattern)){
            document.getElementById("emailValidate").innerHTML="";
          }
          else if(!email){
            document.getElementById("emailValidate").innerHTML="Email Required";
            isValid=false;
         }
          else{
            document.getElementById("emailValidate").innerHTML="Invalid email";
            isValid=false;
          }
          return isValid;
      }
      function cnoValidate(){
         var cno = document.getElementById("contact").value;
         var pattern = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
         isValid=true;
         if(cno.match(pattern)){
            document.getElementById("contactValidate").innerHTML="";
         }
         else if(!cno){
            document.getElementById("contactValidate").innerHTML="Number required";
            isValid=false;
         }
         else{
            document.getElementById("contactValidate").innerHTML="Invalid Contact Number";
            isValid=false;
         }
         return isValid;
         
      }

      function validateconfirmPassword(){
         var cpassword = document.getElementById("cpassword").value;
         var password = document.getElementById("password").value;
         isValid=true;
         if(cpassword!=password){
            document.getElementById("cpasswordValidate").innerHTML="Enter same password";
         }
         else if(!cpassword){
            document.getElementById("cpasswordValidate").innerHTML="Password Required";
            isValid=false;
         }
         else{
             document.getElementById("cpasswordValidate").innerHTML="";
            isValid=false;
         }
         return isValid;

      }

      function validatepwd(){
         var password = document.getElementById("password").value;
         var pattern=/^(?=.*\d)(?=.*[A-Z]).{6,}/;
         isValid=true;
         if(password.match(pattern)){
            document.getElementById("passwordValidate").innerHTML="";  
         }
         else if(!password){
            document.getElementById("passwordValidate").innerHTML="Password Required";
            isValid=false;
         }
         else{
            isValid=false;
         }
         return isValid;
         
      }
      function validatecity(){
         var city = document.getElementById("city").value;
         var pattern =  /^[a-zA-Z]+$/;
         isValid=true;
         if(city.match(pattern)){
            document.getElementById("cityValidate").innerHTML="";
         }
         else if(!city){
            document.getElementById("cityValidate").innerHTML="City Required";
            isValid=false;
         }
         else{
            document.getElementById("cityValidate").innerHTML="Invalid city";
            isValid=false;
         }
         return isValid;
      }


//Login button click
      function loginValid(){
            var loginEmail = document.getElementById("loginEmail").value;
            var loginEmailPattern = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
            isValid=true;
            if(loginEmail.match(loginEmailPattern)){
                document.getElementById("validateEmail").innerHTML="";
            }
            else if(!loginEmail){
                document.getElementById("validateEmail").innerHTML="Email Required";
                isValid=false;
            }
            else{
                document.getElementById("validateEmail").innerHTML="Invalid email";
                isValid=false;
            }


            var loginPassword = document.getElementById("loginPassword").value;
            var loginPasswordPattern=/^(?=.*\d)(?=.*[A-Z]).{6,}/;
            isValid=true;
            if(loginPassword.match(loginPasswordPattern)){
                document.getElementById("validatePassword").innerHTML="";
            }
            else if(!loginPassword){
                document.getElementById("validatePassword").innerHTML="Password Required";
                isValid=false;
            }
            else{
                alert("Password should have atleast 8 characters with one alphaneumeric, one uppercase and one lowercase");
                isValid=false;
            }
            return isValid;
        }

      function loginEmailValidate(){
          var loginEmail = document.getElementById("loginEmail").value;
            var loginEmailPattern = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
            isValid=true;
            if(loginEmail.match(loginEmailPattern)){
                document.getElementById("validateEmail").innerHTML="";
            }
            else if(!loginEmail){
                document.getElementById("validateEmail").innerHTML="Email Required";
               isValid=false;
                     }
            else{
               document.getElementById("validateEmail").innerHTML="Invalid email";
               isValid=false;
           }
            return isValid;
      }

      function loginPasswordValidate(){
         var loginPassword = document.getElementById("loginPassword").value;
            var loginPasswordPattern=/^(?=.*\d)(?=.*[A-Z]).{6,}/;
              isValid=true;
            if(loginPassword.match(loginPasswordPattern)){
                document.getElementById("validatePassword").innerHTML="";
            }
            else if(!loginPassword){
                document.getElementById("validatePassword").innerHTML="Password Required";
                isValid=false;
            }
            else{
                isValid=false;
           }
           return isValid;
      }