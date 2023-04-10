const printingDropdown = document.querySelector('#printing')
const laminaitonDropdown = document.querySelector('#lamination')

//  when there is a change in dropdown value and that value exists then show other elements
printingDropdown.addEventListener("change", (e) => {
    hideDynamicField(document ,'.printing-dynamic-fields')
    showDynamicField(e.target.value, "dynamicFieldsPrinting")
})


laminaitonDropdown.addEventListener("change", (e) => {
    hideDynamicField(laminaitonDropdown.parentNode, '.lamination-dynamic-fields') //counter class send here
    showDynamicField(e.target.value, 'dynamicFieldsLamination')
})

// ******************************* function to show or hide elements *******************************
function showDynamicField(value, dynamicFields){
    dynamicFieldsElements = document.getElementById(dynamicFields)
    console.log(dynamicFieldsElements)
    underscoreValue = value.replace(/ /g, '_')
    if(value){
        dynamicFieldsElements.style.display = "block";
        var element = document.getElementById('id_'+underscoreValue+'_Qty')

        // since met is in printing and lamination we need to select lamination element only which comes second
        if(value == "Met" && dynamicFields == "dynamicFieldsLamination"){
            element = document.querySelectorAll('#id_Met_Qty')[1]
        }

        // whichever element is here will be assigned display block
        element.style.display="block"

        // if it is a printing dropdown then we need to show ink cost which is specific to only printing
        if(element.classList.contains('printing-dynamic-fields')){
            document.getElementById("id_Ink_Cost_PKG").style.display="block"

        } 
        
        // if it is lamination dropdown then we need to shoe lamination cost and output
        else if(element.classList.contains('lamination-dynamic-fields')){

            if(value != 'Polly'){
                document.getElementById("id_Lamination_Cost").style.display="block"
                document.getElementById("id_Lamination_Output").style.display="block"
            }else{
                document.getElementById("id_Lamination_Cost_Polly").style.display="block"
                document.getElementById("id_Lamination_OutPut_Polly").style.display="block"
            }
        }
    } else {
        dynamicFieldsElements.style.display = "none";
      }
}

function hideDynamicField(fromWhereToSelectElement ,value){
    const elements = fromWhereToSelectElement.querySelectorAll(value)
    console.log(fromWhereToSelectElement)
    elements.forEach(element => {
        element.style.display = "none";
      });
}





//************************ To add a new drop down *******************************



// Add a click event listener to the "Add" link
document.querySelector('#add-dropdown').addEventListener('click', function(event) {
    event.preventDefault();
    var dropdownSection = document.querySelector('.dropdown-section');

    // Clone the dropdown section
    var newDropdownSection = dropdownSection.cloneNode(true);

    // Hide the fields for the cloned section
    hideDynamicField(newDropdownSection, '.lamination-dynamic-fields')

    var counter = document.querySelectorAll('.dropdown-section').length;
    // newDropdownSection.id = 'dropdown-section-' + counter;
    newDropdownSection.classList.add('dropdown-section-' + counter);
    
    // Append the clone after the last dropdown section
    document.querySelector('.dropdown-section:last-of-type').after(newDropdownSection);

     var newDropdown = newDropdownSection.querySelector('.Lamination_Type');  

    // hideDynamicField('.lamination-dynamic-fields')
    newDropdown.addEventListener('change', function() {
        hideDynamicField(newDropdownSection, '.lamination-dynamic-fields')
        var optionValue = this.value;
        underscoreValue = optionValue.replace(/ /g, '_')
        this.parentNode.querySelector('#id_'+underscoreValue+'_Qty').style.display="block";
        if(optionValue != 'Polly'){
            this.parentNode.querySelector("#id_Lamination_Cost").style.display="block"
            this.parentNode.querySelector("#id_Lamination_Output").style.display="block"
        }else{
            this.parentNode.querySelector("#id_Lamination_Cost_Polly").style.display="block"
            this.parentNode.querySelector("#id_Lamination_OutPut_Polly").style.display="block"
        }
  });
});

