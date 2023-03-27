/* selecting the query with id usernameField*/
const usernameField = document.querySelector('#usernameField')
/* selecting the query with class invalid-feedback*/
const feedbackArea = document.querySelector('.invalid_feedback')
/* selecting the query with class usernameSuccessOutput */
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput')
/* To disable the submit button whenever there is an error */
const submitBtn = document.querySelector('#submit-btn')

/* on key press*/
usernameField.addEventListener("keyup", (e) => {
    /* the value we are entering in username field */
    const usernameValue = e.target.value;
    
    /* display this query before API call when key is presses */
    usernameSuccessOutput.style.display = "block";
    /* setting text content to be displayed in this query*/
    usernameSuccessOutput.textContent = `Checking ${usernameValue}`;

    /* before API call remove is-invalid from usernameField query and display none*/
    usernameField.classList.remove("form-control","is-invalid");
    feedbackArea.style.display='none';

    console.log("hello");
    /* if value we are entering is not null */
    if(usernameValue.length > 0){
        /* calling the API that validates username */
        fetch('/authentication/usernameValidation',{
            body:JSON.stringify({username: usernameValue}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data)=>{
            /* dont display this query after API call */
            usernameSuccessOutput.style.display = "none"
            /* if data from API has username_error*/
            if(data.username_error){
                submitBtn.disabled=true
                usernameField.classList.add("form-control", "is-invalid");
                feedbackArea.style.display='block'
                feedbackArea.innerHTML=`<p>${data.username_error}</p>`
                

            }else{
                submitBtn.disabled=false
            }
        })
    }
    
})


/* email validation */
const emailField = document.querySelector('#emailField')
const emailFeedbackArea = document.querySelector('.emailFeedBackArea')
const emailSuccessOutput = document.querySelector('.emailSuccessOutput')

emailField.addEventListener("keyup", (e) => {
    /* the value we are entering in username field */
    const emailValue = e.target.value;
    
    emailSuccessOutput.style.display="block";

    emailSuccessOutput.textContent = `Checking ${emailValue}`;
    /* before API call remove is-invalid from usernameField query and display none*/
    emailField.classList.remove("form-control","is-invalid");
    emailFeedbackArea.style.display='none'


    /* if value we are entering is not null */
    if(emailValue.length > 0){
        /* calling the API that validates username */
        fetch('/authentication/emailValidation',{
            body:JSON.stringify({email: emailValue}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data)=>{
            console.log("data: ", data)
            emailSuccessOutput.style.display = "none"
            /* if data from API has username_error*/
            if(data.email_error){
                submitBtn.disabled=true
                emailField.classList.add("form-control", "is-invalid");
                emailFeedbackArea.style.display='block'
                emailFeedbackArea.innerHTML=`<p>${data.email_error}</p>`
            }else{
                submitBtn.disabled=false
            }
        })
    }
})


/* Password Toggle */
const showPasswordToggle = document.querySelector(".showPasswordToggle")
const passwordField = document.querySelector("#passwordField")

const handleToggleInput=(e) => {
    if(showPasswordToggle.textContent === 'SHOW'){
        showPasswordToggle.textContent = 'HIDE'
        passwordField.setAttribute("type", "text")
    }else{
        showPasswordToggle.textContent = 'SHOW'

        passwordField.setAttribute("type", "password")
    }



}
/* on clicking the query call function handleToggleInput */
showPasswordToggle.addEventListener('click', handleToggleInput)