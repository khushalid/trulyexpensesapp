
/***************** Add an input field when a dropdown input is selected *************************/

/************************************ For Printing ************************************/
const printingDropdown = document.querySelector('#printing')
const printingInput = document.querySelector('.printing-input')

let printingSelectedValue =null;
let printingInputElement =null;

printingDropdown.addEventListener('change', (e) => {
    const queryString = (new URL(document.location)).searchParams;
    const urlParams = new URLSearchParams(queryString);

    const page_type = urlParams.get('printing')
    console.log(queryString)
    console.log(page_type);
    var dropdownSelectedValue = e.target.value;
    if(printingSelectedValue !== dropdownSelectedValue && printingInputElement){
        printingInput.removeChild(printingInputElement);
        printingInputElement=null;
    }

    printingSelectedValue = dropdownSelectedValue;
    if(!printingInputElement){
        printingInputElement = document.createElement("input")
        printingInputElement.id = "printing-qty"
        printingInputElement.type = "text"
        printingInputElement.name = e.target.value
        printingInputElement.placeholder = e.target.value + ' QTY'
        printingInputElement.classList.add('form-control')
        printingInput.appendChild(printingInputElement)
        printingInput.classList.add('mb-3')
    }
})

/********************************** For Lamination ***********************************/
const laminationDropdown = document.querySelector('.select-group-lamination')
laminationDropdown.addEventListener('change', (e) => {
    addLaminationSpecificValuesOnLaminationSelect(e);
    
})


/************************* Add Lamination Dropdown  ***********************************/

console.log(contextLamination)
contextLamination = String(contextLamination).replace(/'/g, '"');
contextLamination = JSON.parse(contextLamination)

const add_lamination = document.querySelector("#add-lamination")
const additional_lamination_field = document.querySelector("#addLaminationField");
const costing_form = document.querySelector("#costing-form")
let i=0

function addInputGroup(){

    const divField = document.createElement("div")
    divField.classList.add("input-group")

    const selectField = document.createElement("select")

    selectField.addEventListener("change", function(e){
        addLaminationSpecificValuesOnLaminationSelect(e)
    })
    selectField.name = "lamination"
    selectField.classList.add("custom-select")
    selectField.classList.add("mb-3")
    selectField.classList.add("select-group-lamination")
    selectField.id = "lamination"

    const optionFieldSelected = document.createElement("option")
    optionFieldSelected.name = "lamination"
    optionFieldSelected.selected
    optionFieldSelected.text = "Choose Lamination..."
    selectField.appendChild(optionFieldSelected)
    
    
    
    for(let l = 0; l<contextLamination.length; l++){
        const optionField = document.createElement("option")
        optionField.name = "lamination"
        optionField.value = contextLamination[l].name
        optionField.text = contextLamination[l].name
        selectField.appendChild(optionField)
    }
    
    divField.appendChild(selectField)

    const QtyDivField = document.createElement("div")
    QtyDivField.setAttribute("class", "lamination-input input-group flex-nowrap")

    additional_lamination_field.appendChild(divField)
    additional_lamination_field.appendChild(QtyDivField)
    additional_lamination_field.classList.add("mb-3")

}

add_lamination.addEventListener("click", addInputGroup)



/****************** Function To Add Lamination Fields On Select *****************/
function addLaminationSpecificValuesOnLaminationSelect(e){
    const laminationInput = document.querySelector('.lamination-input')

    let laminationSelectedValue =null;
    let laminationInputQtyElement = null;
    let laminationInputCostElement = null;
    let laminationInputOutputElement = null;

    var dropdownSelectedValue = e.target.value;
    if(laminationSelectedValue !== dropdownSelectedValue && laminationInputQtyElement){
        laminationInput.removeChild(laminationInputQtyElement);
        laminationInput.removeChild(laminationInputCostElement);
        laminationInput.removeChild(laminationInputOutputElement);
        laminationInputQtyElement = null;
        laminationInputCostElement = null;
        laminationInputOutputElement = null;
    }
    laminationSelectedValue = dropdownSelectedValue;

    if(!laminationInputQtyElement){
        laminationInputQtyElement = document.createElement("input")
        laminationInputQtyElement.id = "lamination-qty"
        laminationInputQtyElement.type = "text"
        laminationInputQtyElement.name = e.target.value
        laminationInputQtyElement.placeholder = 'QTY'
        laminationInputQtyElement.classList.add('form-control')

        laminationInputCostElement = document.createElement("input")
        laminationInputCostElement.id = "lamination-cost"
        laminationInputCostElement.type = "text"
        laminationInputCostElement.name = "Lamination Cost"
        laminationInputCostElement.placeholder = "Lamination Cost"
        laminationInputCostElement.classList.add('form-control')

        laminationInputOutputElement = document.createElement("input")
        laminationInputOutputElement.id = "lamination-output"
        laminationInputOutputElement.type = "text"
        laminationInputOutputElement.name = "Lamination Output"
        laminationInputOutputElement.placeholder = "Lamination Output"
        laminationInputOutputElement.classList.add('form-control')
        
        laminationInput.append(laminationInputQtyElement, laminationInputCostElement, laminationInputOutputElement)
        laminationInput.classList.add("mb-3")
    }

    laminationInput.classList.remove("lamination-input")
}
