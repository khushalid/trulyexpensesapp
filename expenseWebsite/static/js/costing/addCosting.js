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
// document.querySelector('#add-dropdown').addEventListener('click', function(event) {
//     event.preventDefault();
//     var dropdownSection = document.querySelector('.dropdown-section');

//     // Clone the dropdown section
//     var newDropdownSection = dropdownSection.cloneNode(true);

//     // Hide the fields for the cloned section
//     hideDynamicField(newDropdownSection, '.lamination-dynamic-fields')

//     var counter = document.querySelectorAll('.dropdown-section').length;
//     newDropdownSection.classList.add('dropdown-section-' + counter);
    
//     // Append the clone after the last dropdown section
//     document.querySelector('.dropdown-section:last-of-type').after(newDropdownSection);

//      var newDropdown = newDropdownSection.querySelector('.Lamination_Type');  

//     // hideDynamicField('.lamination-dynamic-fields')
//     newDropdown.addEventListener('change', function() {
//         hideDynamicField(newDropdownSection, '.lamination-dynamic-fields')
//         var optionValue = this.value;
//         underscoreValue = optionValue.replace(/ /g, '_')
//         this.parentNode.querySelector('#id_'+underscoreValue+'_Qty').style.display="block";
//         if(optionValue != 'Polly'){
//             this.parentNode.querySelector("#id_Lamination_Cost").style.display="block"
//             this.parentNode.querySelector("#id_Lamination_Output").style.display="block"
//         }else{
//             this.parentNode.querySelector("#id_Lamination_Cost_Polly").style.display="block"
//             this.parentNode.querySelector("#id_Lamination_OutPut_Polly").style.display="block"
//         }
//   });
// });


document.querySelector('#add-dropdown').addEventListener('click', function(event) {
    event.preventDefault();
    var dropdownSection = document.querySelector('.dropdown-section');
    
    var newDropdownSection = dropdownSection.cloneNode(true);
    hideDynamicField(newDropdownSection, '.lamination-dynamic-fields')

    var counter = document.querySelectorAll('.dropdown-section').length;
    newDropdownSection.classList.add('dropdown-section-' + counter);

    var newColumn = document.createElement('div');
    newColumn.classList.add('col', 'laminationColumn');
    
    var lastColumn = document.querySelector('.laminationColumn:last-of-type');

    // Create a new card
    var newCard = document.createElement('div');
    newCard.classList.add('card','h-100', 'border-rounded');
    
    // Create a new card body
    var newCardBody = document.createElement('div');
    newCardBody.classList.add('card-body');

    // Append the clone to the new card body
    

    var link = document.querySelector('#add-dropdown');
    
    newCardBody.innerHTML = "Lamination"
    newCardBody.appendChild(newDropdownSection);
    newCardBody.appendChild(link);

    // Append the new card body to the new card
    newCard.appendChild(newCardBody);

    // Append the new card to the new column
    newColumn.appendChild(newCard);

    // Insert the new column after the last column
    lastColumn.after(newColumn);

    var newDropdown = newDropdownSection.querySelector('.Lamination_Type');
    newDropdown.addEventListener('change', function() {
        hideDynamicField(newDropdownSection, '.lamination-dynamic-fields');
        var optionValue = this.value;
        underscoreValue = optionValue.replace(/ /g, '_');
        this.parentNode.querySelector('#id_'+underscoreValue+'_Qty').style.display="block";
        if(optionValue != 'Polly') {
        this.parentNode.querySelector("#id_Lamination_Cost").style.display="block";
        this.parentNode.querySelector("#id_Lamination_Output").style.display="block";
        } else {
        this.parentNode.querySelector("#id_Lamination_Cost_Polly").style.display="block";
        this.parentNode.querySelector("#id_Lamination_OutPut_Polly").style.display="block";
        }
    });
});



function editRate(rateDisplay) {
    const h6 = rateDisplay.querySelector('h6');
    const input = rateDisplay.querySelector('input');
    
    if (h6.style.display === 'none') {
        h6.textContent = input.value;
        h6.style.display = 'block';
        input.style.display = 'none';
    } else {
        h6.style.display = 'none';
        input.style.display = 'block';
        input.focus();
    }
}

document.addEventListener('click', function(event) {
    const rateInputs = document.querySelectorAll('.rate-display input');
    rateInputs.forEach(rateInput => {
        if (rateInput && !event.target.closest('.rate-display')) {
            const rateDisplay = rateInput.closest('.rate-display');
            const h6 = rateDisplay.querySelector('h6');
            
            h6.textContent = rateInput.value;
            h6.style.display = 'block';
            rateInput.style.display = 'none';
        }
    });
    
});

