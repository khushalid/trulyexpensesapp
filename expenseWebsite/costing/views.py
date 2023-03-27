from django.shortcuts import render
import json 
import os
from django.conf import settings
from .models import Costing


# Create your views here.

def index(request):
    Zipper_Rate = floatConvert(179)
    printing = []
    printing_file = os.path.join(settings.BASE_DIR, 'printing.json')
    with open(printing_file, 'r') as json_file:

        data = json.load(json_file)

        for k,v in data.items():
            printing.append({'name': k, 'value': v})

    lamination = []
    lamination_file = os.path.join(settings.BASE_DIR, 'lamination.json')
    with open(lamination_file, 'r') as json_file:

        data = json.load(json_file)

        for k,v in data.items():
            lamination.append({'name': k, 'value': v})
    if request.method == 'GET':
        return render(request, 'costing/index.html', {'printing': printing, 'lamination': lamination})
    
    if request.method == 'POST':

        form_value = request.POST.copy()

        # ********************** Saving Lamination information ************************
        Lamination_OutPut_Polly = Lamination_Output = Lamination_Cost_Polly = Lamination_Cost = Met_Qty = Met_Rate = Met_Cost = Met_CPP_Qty = Met_CPP_Rate = Met_CPP_Cost = Foil_9_Mic_Qty = Foil_9_Mic_Rate = Foil_9_Mic_Cost = Foil_30_Mic_Qty  = Foil_30_Mic_Rate = Foil_30_Mic_Cost = Polly_Qty = Polly_Rate = Polly_Cost = 0
        laminationFormValue = form_value.getlist('lamination')
        laminationCostValues = form_value.getlist('Lamination Cost')
        laminationOutputValues = form_value.getlist('Lamination Output')
        if(laminationFormValue != 'Choose Lamination...'):
            print(laminationFormValue)
            for i in range(0, len(laminationFormValue)):
                if laminationFormValue[i] == 'MET':
                    Met_Qty = form_value.get(laminationFormValue[i])
                    Met_Rate = [lamination[i]['value'] for i in range(0,len(lamination)) if lamination[i]['name'] == 'MET'][0]
                    Met_Cost = floatConvert(Met_Qty)*floatConvert(Met_Rate)
                    Lamination_Cost = floatConvert(laminationCostValues[i])
                    Lamination_Output = floatConvert(laminationOutputValues[i])
                elif laminationFormValue[i] == 'MET CPP':
                    Met_CPP_Qty = form_value.get(laminationFormValue[i])
                    Met_CPP_Rate = [lamination[i]['value'] for i in range(0,len(lamination)) if lamination[i]['name'] == 'MET CPP'][0]
                    Met_CPP_Cost = floatConvert(Met_CPP_Qty)*floatConvert(Met_CPP_Rate)
                    Lamination_Cost = floatConvert(laminationCostValues[i])
                    Lamination_Output = floatConvert(laminationOutputValues[i])
                elif laminationFormValue[i] == 'FOIL 9 MIC':
                    Foil_9_Mic_Qty = form_value.get(laminationFormValue[i])
                    Foil_9_Mic_Rate = [lamination[i]['value'] for i in range(0,len(lamination)) if lamination[i]['name'] == 'FOIL 9 MIC'][0]
                    Foil_9_Mic_Cost = floatConvert(Foil_9_Mic_Qty)*floatConvert(Foil_9_Mic_Rate)
                    Lamination_Cost = floatConvert(laminationCostValues[i])
                    Lamination_Output = floatConvert(laminationOutputValues[i])
                elif laminationFormValue[i] == 'FOIL 30 MIC':
                    Foil_30_Mic_Qty = form_value.get(laminationFormValue[i])
                    Foil_30_Mic_Rate = [lamination[i]['value'] for i in range(0,len(lamination)) if lamination[i]['name'] == 'FOIL 30 MIC'][0]
                    Foil_30_Mic_Cost = floatConvert(Foil_30_Mic_Qty)*floatConvert(Foil_30_Mic_Rate)
                    Lamination_Cost = floatConvert(laminationCostValues[i])
                    Lamination_Output = floatConvert(laminationOutputValues[i])
                elif laminationFormValue[i] == 'Poly':
                    Polly_Qty = form_value.get(laminationFormValue[i])
                    Polly_Rate = [lamination[i]['value'] for i in range(0,len(lamination)) if lamination[i]['name'] == 'Poly'][0]
                    Polly_Cost = floatConvert(Polly_Qty)*floatConvert(Polly_Rate)
                    Lamination_Cost_Polly = floatConvert(laminationCostValues[i])
                    Lamination_OutPut_Polly = floatConvert(laminationOutputValues[i])

        # ********************** Saving Printing information ************************
        Pet_Qty = Lamination_Cost_PKG_Polly = Lamination_Cost_PKG = Coating_Cost_PKG = Pet_HST_Qty = Met_Qty = Pet_Rate = Ink_Cost = Met_Cost = Pet_HST_Rate = Met_Rate = Pet_Cost = Pet_HST_Cost = 0
        printingFormValue = form_value.get('printing')
        if(printingFormValue != 'Choose Printing...'):
            if printingFormValue == 'PET':
                Pet_Qty = floatConvert(form_value.get(printingFormValue))
                Pet_Rate = [printing[i]['value'] for i in range(0,len(printing)) if printing[i]['name'] == 'PET'][0]
                Pet_Cost = floatConvert(Pet_Qty)*floatConvert(Pet_Rate)
                Ink_Cost = floatConvert(form_value.get('INK COST P.KG'))*floatConvert(Pet_Qty)
                Coating_Cost_PKG = floatConvert(form_value.get('Coating Cost'))/floatConvert(Pet_Qty)
                Lamination_Cost_PKG = Lamination_Cost/Pet_Qty
                Lamination_Cost_PKG_Polly = Lamination_Cost_Polly/Pet_Qty
            elif printingFormValue == 'PET HST':
                Pet_HST_Qty = floatConvert(form_value.get(printingFormValue))
                Pet_HST_Rate = [printing[i]['value'] for i in range(0,len(printing)) if printing[i]['name'] == 'PET HST'][0]
                Pet_HST_Cost = floatConvert(Pet_HST_Qty)*floatConvert(Pet_HST_Rate)
                Ink_Cost = floatConvert(form_value.get('INK COST P.KG'))*floatConvert(Pet_HST_Qty)
                Coating_Cost_PKG = floatConvert(form_value.get('Coating Cost'))/floatConvert(Pet_HST_Qty)
                Lamination_Cost_PKG = Lamination_Cost/Pet_HST_Qty
                Lamination_Cost_PKG_Polly = Lamination_Cost_Polly/Pet_HST_Qty
            else:
                Met_Qty = floatConvert(form_value.get(printingFormValue))
                Met_Rate = [printing[i]['value'] for i in range(0,len(printing)) if printing[i]['name'] == 'MET'][0]
                Met_Cost = floatConvert(Met_Qty)*floatConvert(Met_Rate)
                Ink_Cost = floatConvert(form_value.get('INK COST P.KG'))*floatConvert(Met_Qty)
                Coating_Cost_PKG = floatConvert(form_value.get('Coating Cost'))/floatConvert(Met_Qty)
                Lamination_Cost_PKG = Lamination_Cost/Met_CPP_Qty
                Lamination_Cost_PKG_Polly = Lamination_Cost_Polly/Met_Qty

        print(form_value)
        
        Total_Cost = Pet_Cost + Pet_HST_Cost + Ink_Cost + Met_Cost + Met_CPP_Cost + Foil_9_Mic_Cost + Foil_30_Mic_Cost + Lamination_Cost + Lamination_Cost_Polly + Polly_Cost + (floatConvert(form_value.get('Coating Cost'),)) + (Zipper_Rate * floatConvert(form_value.get('Zipper Qty')))
        Net_Raw_Material = floatConvert(Pet_Qty) + floatConvert(Pet_HST_Qty) + floatConvert(Met_Qty) + floatConvert(Met_CPP_Qty) + floatConvert(Foil_9_Mic_Qty) + floatConvert(Foil_30_Mic_Qty) + floatConvert(Polly_Qty) + [floatConvert(form_value.get('Zipper Qty')) if form_value.get('Zipper Qty') != '' else 0][0]
        costing = Costing.objects.create(
            Job_Name = form_value.get('Job Name'),
            Job_Size = (form_value.get('Job Size')),
            Pet_Qty = Pet_Qty,
            Pet_Rate = Pet_Rate,
            Pet_Cost = Pet_Cost,
            Pet_HST_Qty = Pet_HST_Qty,
            Pet_HST_Rate = Pet_HST_Rate,
            Pet_HST_Cost = Pet_HST_Cost,
            Ink_Cost = Ink_Cost,
            Ink_Cost_PKG = floatConvert(form_value.get('INK COST P.KG')),
            Met_Qty  = Met_Qty ,
            Met_Rate = Met_Rate,
            Met_Cost = Met_Cost,
            Met_CPP_Qty  = Met_CPP_Qty ,
            Met_CPP_Rate = Met_CPP_Rate,
            Met_CPP_Cost = Met_CPP_Cost,
            Foil_9_Mic_Qty  = Foil_9_Mic_Qty ,
            Foil_9_Mic_Rate = Foil_9_Mic_Rate,
            Foil_9_Mic_Cost = Foil_9_Mic_Cost,
            Foil_30_Mic_Qty  = Foil_30_Mic_Qty ,
            Foil_30_Mic_Rate = Foil_30_Mic_Rate,
            Foil_30_Mic_Cost = Foil_30_Mic_Cost,
            Lamination_Cost = Lamination_Cost,
            Lamination_Cost_PKG = Lamination_Cost_PKG,
            Lamination_Output = Lamination_Output,
            Polly_Qty  = Polly_Qty ,
            Polly_Rate = Polly_Rate,
            Polly_Cost = Polly_Cost,
            Lamination_Cost_Polly = Lamination_Cost_Polly,
            Lamination_Cost_PKG_Polly = Lamination_Cost_PKG_Polly,
            Lamination_OutPut_Polly = Lamination_OutPut_Polly,
            Coating_Cost = floatConvert(form_value.get('Coating Cost')),
            Coating_Cost_PKG = Coating_Cost_PKG,
            Zipper_Qty = floatConvert(form_value.get('Zipper Qty')),
            Zipper_Rate = Zipper_Rate,
            Zipper_Cost = Zipper_Rate * floatConvert(form_value.get('Zipper Qty')),
            Total_Cost = Total_Cost,
            Lami_total_Output = Lamination_OutPut_Polly,
            Sliting_Output = floatConvert(form_value.get('Sliting Output')),
            Print_Westag = floatConvert(Pet_Qty) - floatConvert(Met_Qty),
            Lamination_Westag = floatConvert(Lamination_OutPut_Polly) - floatConvert(form_value.get('Sliting Output')) - floatConvert(form_value.get('Trim Wastage')),
            Trim_Westag = floatConvert(form_value.get('Trim Wastage')),
            Pouch_Westag = floatConvert(form_value.get('Sliting Output')) - floatConvert(form_value.get('Zipper Qty')) - floatConvert(form_value.get('Finished Goods')),
            Net_Raw_Material = Net_Raw_Material,
            Finished_Good = floatConvert(form_value.get('Finished Goods')),
            Wet_Gain_Loss = floatConvert(form_value.get('Finished Goods')) - Net_Raw_Material,
            Total_Cost_PKG = Total_Cost/floatConvert(form_value.get('Finished Goods'))
            )
        print(costing.Total_Cost_PKG)
    
    context = {
        'calculated_cost': costing
    }
    return render(request, 'costing/totalCost.html', context)

def floatConvert(value):
        return [float(value) if value != '' else 0][0]
        