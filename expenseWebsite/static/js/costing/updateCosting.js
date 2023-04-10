const printingDropdown = document.querySelector('#printing')
const laminaitonDropdowns = document.querySelectorAll('#laminationAlreadyPresent')

// on page load check if there is value available in dropdowns
showDynamicField(printingDropdown.value, "dynamicFieldsPrinting")

var i=1
laminaitonDropdowns.forEach(laminaitonDropdown => {
    console.log(laminaitonDropdown)
    showDynamicField(laminaitonDropdown.value, "dynamicFieldsLamination"+i)
    console.log("dynamicFieldsLamination"+i)
    i++
})


//  when there is a change in dropdown value and that value exists then show other elements

printingDropdown.addEventListener("change", (e) => {
    hideDynamicField(document ,'.printing-dynamic-fields')
    showDynamicField(e.target.value, "dynamicFieldsPrinting")
})




// ******************************* function to show or hide elements *******************************
function showDynamicField(value, dynamicFields){
    dynamicFieldsElements = document.getElementById(dynamicFields)
    underscoreValue = value.replace(/ /g, '_')
    if(value){
        dynamicFieldsElements.style.display = "block";
        var element = dynamicFieldsElements.querySelector('#id_'+underscoreValue+'_Qty')

        // whichever element is here will be assigned display block
        element.style.display="block"

        // if it is a printing dropdown then we need to show ink cost which is specific to only printing
        if(element.classList.contains('printing-dynamic-fields')){
            document.getElementById("id_Ink_Cost_PKG").style.display="block"

        } 
        
        // if it is lamination dropdown then we need to shoe lamination cost and output
        else if(element.classList.contains('lamination-dynamic-fields')){

            if(value != 'Polly'){
                dynamicFieldsElements.querySelector("#id_Lamination_Cost").style.display="block"
                dynamicFieldsElements.querySelector("#id_Lamination_Output").style.display="block"
            }else{
                dynamicFieldsElements.querySelector("#id_Lamination_Cost_Polly").style.display="block"
                dynamicFieldsElements.querySelector("#id_Lamination_OutPut_Polly").style.display="block"
            }
        }
    } else {
        dynamicFieldsElements.style.display = "none";
      }
}

function hideDynamicField(fromWhereToSelectElement ,value){
    const elements = fromWhereToSelectElement.querySelectorAll(value)
    elements.forEach(element => {
        element.style.display = "none";
      });
}



//************************ If already no lamination present ************************
const laminaitonDropdownNew = document.querySelector('#lamination')

if(laminaitonDropdownNew){
    laminaitonDropdownNew.addEventListener("change", (e) => {
        hideDynamicField(laminaitonDropdownNew.parentNode, '.lamination-dynamic-fields') 
        showDynamicField(e.target.value, 'dynamicFieldsLamination')
    })
}



//************************ To add a new drop down *******************************


// Add a click event listener to the "Add" link
document.querySelector('#add-dropdown').addEventListener('click', function(event) {
    event.preventDefault();
    var dropdownSection = document.querySelector('.dropdown-section');

//     // Clone the dropdown section
    var newDropdownSection = dropdownSection.cloneNode(true);
    console.log(dropdownSection)
    console.log(newDropdownSection)

//     // Hide the fields for the cloned section
    hideDynamicField(newDropdownSection, '.lamination-dynamic-fields')
    if(newDropdownSection.style.display == 'none'){
        newDropdownSection.style.display = 'block'
    }

    var counter = document.querySelectorAll('.dropdown-section').length;
    // newDropdownSection.id = 'dropdown-section-' + counter;
    newDropdownSection.classList.add('dropdown-section-' + counter);
    
//     // Append the clone after the last dropdown section
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



// // // ******************************* Add a change event listener to each dropdown *******************************
// // var originalDropdowns = document.querySelectorAll('.dropdown-section:first-of-type .Lamination_Type');
// // console.log(originalDropdowns)
// // originalDropdowns.forEach(function(dropdown) {
// //   dropdown.addEventListener('change', function() {
// //     var optionValue = this.value;
// //     underscoreValue = optionValue.replace(/ /g, '_')
// //     this.parentNode.querySelector('#id_'+underscoreValue+'_Qty').style.display="block";
// //     if(optionValue != 'Polly'){
// //         this.parentNode.querySelector("#id_Lamination_Cost").style.display="block"
// //         this.parentNode.querySelector("#id_Lamination_Output").style.display="block"
// //     }else{
// //         this.parentNode.querySelector("#id_Lamination_Cost_Polly").style.display="block"
// //         this.parentNode.querySelector("#id_Lamination_OutPut_Polly").style.display="block"
// //     }
// //   });
// // });



// //******************************* To add fields qty and lamination cost and lamination output when an option is selected *******************************
// const laminationTypeElements = document.querySelectorAll('.itemOfLaminationType');
// for (let i = 0; i < laminationTypeElements.length; i++) {
//     const laminationType = laminationTypeElements[i].getAttribute('data-lamination-type');
//     underscoredLaminationType = laminationType.replace(/ /g, '_')
//     console.log(underscoredLaminationType);

//     var laminationTypeQty = document.getElementById("id_"+underscoredLaminationType+"_Qty");
//     laminationTypeQty.style.display = "block";
//     laminationTypeQty.classList.remove('lamination-dynamic-fields');

//     if(underscoredLaminationType == 'Polly'){
//         var laminationCost = document.getElementById("id_Lamination_Cost_Polly");
//         laminationCost.style.display = "block";
//         laminationCost.classList.remove('lamination-dynamic-fields');

//         var laminationOutput = document.getElementById("id_Lamination_OutPut_Polly");
//         laminationOutput.style.display = "block"
//         laminationOutput.classList.remove('lamination-dynamic-fields');

//     }
//     else{
//         var laminationCost = document.getElementById("id_Lamination_Cost");
//         laminationCost.style.display = "block";
//         laminationCost.classList.remove('lamination-dynamic-fields');

//         var laminationOutput = document.getElementById("id_Lamination_Output");
//         laminationOutput.style.display = "block"
//         laminationOutput.classList.remove('lamination-dynamic-fields');
//     }

//     console.log(laminationType)
//     const divToRemoveFrom = document.querySelector(`[data-lamination-type="${laminationType}"]`);
//     console.log(divToRemoveFrom)
//     const elementsToRemove = divToRemoveFrom.querySelectorAll('.lamination-dynamic-fields')
//     for (let i = 0; i < elementsToRemove.length; i++) {
//         elementsToRemove[i].remove();
//       }
// }


// // //************************ To add a new drop down *******************************

// // var dropdownSection = document.querySelector('.dropdown-section');

// // // Add a click event listener to the "Add" link
// // document.querySelector('#add-dropdown').addEventListener('click', function(event) {
// //   event.preventDefault();

// //   // Clone the dropdown section
// //   var newDropdownSection = dropdownSection.cloneNode(true);
// //   alert("Hello" + newDropdownSection)

// //   // Hide the fields for the cloned section
// //   newDropdownSection.querySelector('.lamination-dynamic-fields').style.display = 'none';

// //   // Append the clone after the last dropdown section
// //   document.querySelector('.dropdown-section:last-of-type').after(newDropdownSection);

// //   var newDropdown = newDropdownSection.querySelector('.Lamination_Type');
// //   hideDynamicField('.lamination-dynamic-fields')
// //   newDropdown.addEventListener('change', function() {
// //     var optionValue = this.value;
// //     underscoreValue = optionValue.replace(/ /g, '_')
// //     this.parentNode.querySelector('#id_'+underscoreValue+'_Qty').style.display="block";
// //     if(optionValue != 'Polly'){
// //         this.parentNode.querySelector("#id_Lamination_Cost").style.display="block"
// //         this.parentNode.querySelector("#id_Lamination_Output").style.display="block"
// //     }else{
// //         this.parentNode.querySelector("#id_Lamination_Cost_Polly").style.display="block"
// //         this.parentNode.querySelector("#id_Lamination_OutPut_Polly").style.display="block"
// //     }
// //   });
// // });

// // // ******************************* Add a change event listener to each dropdown *******************************
// // var originalDropdowns = document.querySelectorAll('.dropdown-section:first-of-type .Lamination_Type');
// // console.log(originalDropdowns)
// // originalDropdowns.forEach(function(dropdown) {
// //   dropdown.addEventListener('change', function() {
// //     var optionValue = this.value;
// //     underscoreValue = optionValue.replace(/ /g, '_')
// //     this.parentNode.querySelector('#id_'+underscoreValue+'_Qty').style.display="block";
// //     if(optionValue != 'Polly'){
// //         this.parentNode.querySelector("#id_Lamination_Cost").style.display="block"
// //         this.parentNode.querySelector("#id_Lamination_Output").style.display="block"
// //     }else{
// //         this.parentNode.querySelector("#id_Lamination_Cost_Polly").style.display="block"
// //         this.parentNode.querySelector("#id_Lamination_OutPut_Polly").style.display="block"
// //     }
// //   });
// // });




