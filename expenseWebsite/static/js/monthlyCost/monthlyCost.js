var today = new Date();
// var previousMonth = new Date(today.getFullYear(), today.getMonth() - 1, 1);
// var monthString = previousMonth.toLocaleString('default', { month: 'long', year: 'numeric' });

// const monthlyTags = document.querySelector('.monthly-tags')

// for (var i=0;i<12;i++){
//     var newCol = document.createElement('div');
//     newCol.classList.add('col');

//     var newCard = document.createElement('div');
//     newCard.classList.add('card', 'monthYear');

//     var newCardBody = document.createElement('div');
//     newCardBody.classList.add('card-body');

//     var previousMonth = new Date(today.getFullYear(), today.getMonth() - i, 1);
//     var monthString = previousMonth.toLocaleString('default', { month: 'short', year: '2-digit' });
//     var monthTextNode = document.createTextNode(monthString);

//     newCardBody.appendChild(monthTextNode)
//     newCard.appendChild(newCardBody)
//     monthlyTags.appendChild(newCard)
// }


// ******************** when a tag is selected **********************
// const monthTags = document.querySelectorAll('.monthYear')

// ******************** By default show this months total qty and cost
// monthTag = monthTags[0].childNodes
// monthTags[0].classList.add('active-tag-monthYear')
// getFormattedDate(monthTag[0].innerHTML)

// // ******************** Get total cost of the month selected *********************
// const monthlyQty = document.querySelector('.monthly-qty')
// monthTags.forEach((monthTag) => {
//     monthTag.addEventListener('click', (e) => {
//         monthlyQty.innerHTML = ''
//         document.querySelectorAll('.active-tag-monthYear').forEach(element => {
//         element.classList.remove('active-tag-monthYear');
//         });
//         monthTag.classList.add('active-tag-monthYear')
//         getFormattedDate(e.target.textContent)
        
        
//     });
//   });


var monthlyQty = document.querySelector('.tab-content')
//   ********************** function to calculate formatted date that is to be passed to the url ********************
function getFormattedDate(value){
  const clickedText = value;
  const clickedMonth = clickedText.slice(0, 3);
  const clickedYear = clickedText.slice(4);
  const clickedDate = new Date(`${clickedMonth}, 20${clickedYear} 00:00:00`);
  const month = clickedDate.getMonth() + 1; // adding 1 because getMonth() method returns a zero-based index
  const year = clickedDate.getFullYear();
  const formattedDate = `${month.toString().padStart(2, '0')} ${year.toString()}`;
  console.log(formattedDate); // Output: "04 2023"
  addTotalQtyAndCost(formattedDate, clickedText)
}

/************************* function to add cards with total cost and qty *********************/
function addTotalQtyAndCost(formattedDate, clickedText){
  var [Pet_Qty, Pet_Cost, Pet_HST_Qty, Pet_HST_Cost, Poly_Qty, Poly_Cost, Ink_Cost, Met_Qty, Met_Cost, Met_CPP_Qty, Met_CPP_Cost, Foil_9_Mic_Qty, Foil_9_Mic_Cost, Foil_30_Mic_Qty, Foil_30_Mic_Cost, Lamination_Cost, Lamination_Cost_Polly, Coating_Cost, Zipper_Qty, Zipper_Cost, Total_Cost, Net_Raw_Material, Finished_Good, Adhesive_Cost] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  fetch(`/monthly_cost/get_cost_data/?date=${formattedDate}`)
  .then(response => response.json())
  .then(data => {
      data.data.forEach(costing => {
          // Access each element of the list here
          Pet_Qty  = parseInt(costing.Pet_Qty || 0) + parseInt(Pet_Qty || 0); 
          Pet_Cost = parseInt(costing.Pet_Cost || 0) + parseInt(Pet_Cost || 0); 
          Pet_HST_Qty = parseInt(costing.Pet_HST_Qty || 0) + parseInt(Pet_HST_Qty || 0); 
          Pet_HST_Cost = parseInt(costing.Pet_HST_Cost || 0) + parseInt(Pet_HST_Cost || 0);  
          Poly_Qty = parseInt(costing.Poly_Qty || 0) + parseInt(costing.Polly_Qty || 0) + parseInt(Poly_Qty || 0); 
          Poly_Cost = parseInt(costing.Poly_Cost || 0) + parseInt(costing.Polly_Cost || 0) + parseInt(Poly_Cost || 0); 
          Ink_Cost = parseInt(costing.Ink_Cost || 0) + parseInt(Ink_Cost || 0);  
          Met_Qty = parseInt(costing.Met_Qty || 0) + parseInt(Met_Qty || 0); 
          Met_Cost = parseInt(costing.Met_Cost || 0) + parseInt(Met_Cost || 0); 
          Met_CPP_Qty = parseInt(costing.Met_CPP_Qty || 0) + parseInt(Met_CPP_Qty || 0); 
          Met_CPP_Cost = parseInt(costing.Met_CPP_Cost || 0) + parseInt(Met_CPP_Cost || 0); 
          Foil_9_Mic_Qty = parseInt(costing.Foil_9_Mic_Qty || 0) + parseInt(Foil_9_Mic_Qty || 0); 
          Foil_9_Mic_Cost = parseInt(costing.Foil_9_Mic_Cost || 0) + parseInt(Foil_9_Mic_Cost || 0); 
          Foil_30_Mic_Qty = parseInt(costing.Foil_30_Mic_Qty || 0) + parseInt(Foil_30_Mic_Qty || 0); 
          Foil_30_Mic_Cost = parseInt(costing.Foil_30_Mic_Cost || 0) + parseInt(Foil_30_Mic_Cost || 0); 
          Lamination_Cost = parseInt(costing.Lamination_Cost || 0) + parseInt(Lamination_Cost || 0); 
          Lamination_Cost_Polly = parseInt(costing.Lamination_Cost_Polly || 0) + parseInt(Lamination_Cost_Polly || 0); 
          Coating_Cost = parseInt(costing.Coating_Cost || 0) + parseInt(Coating_Cost || 0); 
          Zipper_Qty = parseInt(costing.Zipper_Qty || 0) + parseInt(Zipper_Qty || 0); 
          Zipper_Cost = parseInt(costing.Zipper_Cost || 0) + parseInt(Zipper_Cost || 0); 
          Total_Cost = parseInt(costing.Total_Cost || 0) + parseInt(Total_Cost || 0); 
          Net_Raw_Material = parseInt(costing.Net_Raw_Material || 0) + parseInt(Net_Raw_Material || 0); 
          Finished_Good = parseInt(costing.Finished_Good || 0) + parseInt(Finished_Good || 0); 
          Adhesive_Cost = parseInt(Ink_Cost || 0) + parseInt(Lamination_Cost || 0); + parseInt(Lamination_Cost_Polly || 0); + parseInt(Adhesive_Cost || 0);
      });
      const costData = [
          { label: 'PET Month total QTY <br>(' + clickedText+ ')', value: Pet_Qty },
          { label: 'PET Month Total Cost <br>(' + clickedText+ ')', value: Pet_Cost },
          { label: 'PET HST Month Total QTY <br>(' + clickedText+ ')', value: Pet_HST_Qty },
          { label: 'PET HST Month Total Cost <br>(' + clickedText+ ')', value: Pet_HST_Cost },
          { label: 'POLY Month Total QTY <br>(' + clickedText+ ')', value: Poly_Qty },
          { label: 'POLY Month Total Cost <br>(' + clickedText+ ')', value: Poly_Cost },
          { label: 'Ink Month Total Cost <br>(' + clickedText+ ')', value: Ink_Cost },
          { label: 'MET Month Total Cost <br>(' + clickedText+ ')', value: Met_Qty },
          { label: 'MET Month Total Cost <br>(' + clickedText+ ')', value: Met_Cost },
          { label: 'MET CPP Month Total Cost <br>(' + clickedText+ ')', value: Met_CPP_Qty },
          { label: 'MET CPP Month Total Cost <br>(' + clickedText+ ')', value: Met_CPP_Cost },
          { label: 'FOIL 9 MIC Month Total Cost <br>(' + clickedText+ ')', value: Foil_9_Mic_Qty },
          { label: 'FOIL 9 MIC Month Total Cost <br>(' + clickedText+ ')', value: Foil_9_Mic_Cost },
          { label: 'FOIL 30 MIC Month Total Cost <br>(' + clickedText+ ')', value: Foil_30_Mic_Qty },
          { label: 'FOIL 30 MIC Month Total Cost <br>(' + clickedText+ ')', value: Foil_30_Mic_Cost },
          { label: 'Lamination Month Total Cost <br>(' + clickedText+ ')', value: Lamination_Cost },
          { label: 'Lamination Poly Month Total Cost <br>(' + clickedText+ ')', value: Lamination_Cost_Polly },
          { label: 'Coating Month Total Cost <br>(' + clickedText+ ')', value: Coating_Cost },
          { label: 'Month Total Cost <br>(' + clickedText+ ')', value: Total_Cost },
          { label: 'Net Raw Material Month Total Cost <br>(' + clickedText+ ')', value: Net_Raw_Material },
          { label: 'Finished Goods Month Total Cost <br>(' + clickedText+ ')', value: Finished_Good },
          { label: 'Adhesive Month Total Cost <br>(' + clickedText+ ')', value: Adhesive_Cost }
          
      ];
      costData.forEach( data => {
          const newCol = document.createElement('div');
          newCol.classList.add('col');
          const newCard = document.createElement('div');
          newCard.classList.add('card', 'align-items-center', 'border-rounded','tab-pane');
          newCard.setAttribute('data-tab', clickedText)
          const newCardBody = document.createElement('div');
          newCardBody.classList.add('card-body');
          newCardBody.innerHTML = `<div style="text-align: center;"><b>${data.label}</b></div> <hr><div class="mb-3" style="text-align: center;">${data.value}</div>`;
          newCard.appendChild(newCardBody);
          newCard.style.display = "block"
          newCol.appendChild(newCard)
          monthlyQty.appendChild(newCol);
      })
  })
  .catch(error => console.error(error));
} 





// *** delete **
// Get all the tab buttons
// const tabButtons = document.querySelectorAll(".tab-button");

// // Loop through the buttons and add a click event listener to each one
// tabButtons.forEach((button) => {
//   button.addEventListener("click", () => {
//     // Get the tab ID from the button's data attribute
//     const tabId = button.getAttribute("data-tab");

//     // Hide all the tab panes
//     document.querySelectorAll(".tab-pane").forEach((pane) => {
//       pane.classList.remove("active");
//     });

//     // Show the selected tab pane
//     document.querySelector(`.tab-pane[data-tab="${tabId}"]`).classList.add("active");

//     // Remove the active class from all the tab buttons
//     tabButtons.forEach((button) => {
//       button.classList.remove("active");
//     });

//     // Add the active class to the selected tab button
//     button.classList.add("active");
//   });
// });



/******* new tabs thing **********/
const myContainer = document.querySelector('.tab-header')
for (var i=0;i<15;i++){
    var previousMonth = new Date(today.getFullYear(), today.getMonth() - i, 1);
    var monthString = previousMonth.toLocaleString('default', { month: 'short', year: '2-digit' });

    var newButton = document.createElement('button');
    newButton.classList.add('tab-button');
    newButton.setAttribute('data-tab', monthString)
    newButton.innerHTML = monthString

    myContainer.appendChild(newButton)
}
myContainer.childNodes[1].classList.add('active')


/********* default card of this month **************** */
const activeMonth = document.querySelector('.tab-button','.active')
console.log(activeMonth)
getFormattedDate(activeMonth.innerHTML)

/******** */
const mytabButtons = document.querySelectorAll(".tab-button");

// Loop through the buttons and add a click event listener to each one
mytabButtons.forEach((button) => {
  button.addEventListener("click", () => {
    // document.querySelector('.tab-button.active').classList.remove('active')
    // Remove the active class from all the tab buttons
    mytabButtons.forEach((button) => {
        button.classList.remove("active");
      });
  
      // Add the active class to the selected tab button
    button.classList.add("active");
    document.querySelector('.tab-content').innerHTML = ''
    getFormattedDate(button.innerHTML)
    // Get the tab ID from the button's data attribute
    const tabId = button.getAttribute("data-tab");
    // Hide all the tab panes
    document.querySelectorAll(".tab-pane").forEach((pane) => {
      pane.classList.remove("active");
    });

    // Show the selected tab pane

    
  });
});