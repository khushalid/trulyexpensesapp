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