from django.shortcuts import render,redirect
import json 
import os
from django.conf import settings
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
import ast
import numpy as np
from django import forms
from decimal import Decimal
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import F
from django.core.paginator import Paginator


# Create your views here.

def search(request):
    searchValue = request.GET.get('search_query')
    if searchValue:
        jobSearched = Costing.objects.filter(Job_Name__icontains=searchValue)
    else:
        jobSearched = Costing.objects.all().order_by('-Date')

    paginator = Paginator(jobSearched, 10) # 10 records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobSearched':page_obj,
        'search_form': SearchForm()
    }

    return render(request, 'costing/search.html', context)

def add(request):

    printing_sheet = Printing.objects.all()
    lamination_sheet = Lamination.objects.all()
    miscellaneous = Miscellaneous.objects.all()
    if request.method == 'GET':
        context = {
        'basicJobForm': basicJobElementForm,
        'printingForm': printingForm,
        'laminationForm': laminationForm,
        'otherElementsForm': otherElementForm,
        'printingDynamicFields': printingDynamicFields,
        'laminationDynamicFields': laminationDynamicFields,
        'printing_sheet': printing_sheet,
        'lamination_sheet': lamination_sheet,
        'miscellaneous': miscellaneous
        }
        return render(request, 'costing/add.html',context)
    
    if request.method == 'POST':
        form_value = request.POST.copy()
        saveSheetRate(form_value)

        printing_objects = Printing.objects.all()
        lamination_objects = Lamination.objects.all()

        laminationFormValue = form_value.getlist('Lamination_Type')
        

        formOfBasicJobElements = basicJobElementForm(request.POST)
        formOfPrinting = printingForm(request.POST)
        formOfLaminaiton = laminationForm(request.POST)
        formOfPrintingDynamicElements = printingDynamicFields(request.POST)
        formOfLaminaitonDynamicElements = laminationDynamicFields(request.POST)
        formOfOtherElements = otherElementForm(request.POST)

        costing_instance = saveJobCostData(form_value, formOfBasicJobElements, formOfPrinting, formOfLaminaiton, formOfPrintingDynamicElements, formOfLaminaitonDynamicElements, formOfOtherElements)
        costing_instance.Lamination_Type = str(laminationFormValue)
        
        lamination_type_str = costing_instance.Lamination_Type
        laminationTypesList = None
        if(lamination_type_str): 
            laminationTypesList = ast.literal_eval(lamination_type_str) if lamination_type_str != "['']" else []
        
        for printing_object in printing_objects:
            printing_type = printing_object.Printing_Sheet.replace(' ','_') + "_Rate"
            setattr(costing_instance, printing_type, printing_object.Rate)

        for lamination_object in lamination_objects:
            lamination_type = lamination_object.Lamination_Sheet.replace(' ','_') + "_Rate"
            setattr(costing_instance, lamination_type, lamination_object.Rate)

        
        costing_instance = calculateCostOfJob(costing_instance, laminationTypesList)
        print("costing_instance")
        print(costing_instance)
        costing_instance.save()
        return redirect('/costing')
    

def update_job(request,job_id):
    printing_sheet = Printing.objects.all()
    lamination_sheet = Lamination.objects.all()
    miscellaneous = Miscellaneous.objects.all()

    costing = Costing.objects.get(pk=job_id)

    lamination_type_str = costing.Lamination_Type
    laminationTypesList = None
    if(lamination_type_str): 
        laminationTypesList = ast.literal_eval(lamination_type_str) if lamination_type_str != "['']" else []


    if request.method == 'POST':
        form_value = request.POST.copy()

        saveSheetRate(form_value)
        printing_objects = Printing.objects.all()
        lamination_objects = Lamination.objects.all()
        for printing_object in printing_objects:
            printing_type = printing_object.Printing_Sheet.replace(' ','_') + "_Rate"
            setattr(costing, printing_type, printing_object.Rate)

        for lamination_object in lamination_objects:
            lamination_type = lamination_object.Lamination_Sheet.replace(' ','_') + "_Rate"
            setattr(costing, lamination_type, lamination_object.Rate)

        for key in form_value.keys():
            form_value.setlist(key, [value for value in form_value.getlist(key) if value])

        laminationFormValue = form_value.getlist('Lamination_Type')

        formOfBasicJobElements = basicJobElementForm(form_value, instance=costing)
        formOfPrinting = printingForm(form_value, instance=costing)
        formOfLaminaiton = laminationForm(form_value, instance=costing)
        formOfPrintingDynamicElements = printingDynamicFields(form_value, instance=costing)
        formOfLaminaitonDynamicElements = laminationDynamicFields(form_value, instance=costing)
        formOfOtherElements = otherElementForm(form_value, instance=costing)
        if formOfBasicJobElements.is_valid() and formOfPrinting.is_valid() and formOfLaminaiton.is_valid() and formOfOtherElements.is_valid() and formOfLaminaitonDynamicElements.is_valid() and formOfPrintingDynamicElements.is_valid():
            formOfBasicJobElements.save()
            formOfPrinting.save()
            formOfLaminaiton.save()
            formOfPrintingDynamicElements.save()
            formOfLaminaitonDynamicElements.save()
            formOfOtherElements.save()
            
            costing = calculateCostOfJob(costing, laminationTypesList)
            costing.Lamination_Type = str(laminationFormValue)
            costing.save()
            return redirect('/costing')
        
        # call function that populates other values as well
        # this functino will be common for adding new job cost and updating existing one
    else:
        
        formOfBasicJobElements = basicJobElementForm(instance=costing)
        formOfPrinting = printingForm(instance=costing)
        formOfLaminaiton = laminationForm(instance=costing)
        formOfPrintingDynamicElements = printingDynamicFields(instance=costing)
        formOfLaminaitonDynamicElements = laminationDynamicFields(instance = costing)
        formOfOtherElements = otherElementForm(instance=costing)


        context = {
            'basicJobForm': formOfBasicJobElements,
            'printingForm': formOfPrinting,
            'laminationForm': formOfLaminaiton,
            'otherElementsForm': formOfOtherElements,
            'printingDynamicFields': formOfPrintingDynamicElements,
            'laminationDynamicFields': formOfLaminaitonDynamicElements,
            'laminationTypesList': laminationTypesList,
            'printing_sheet': printing_sheet,
            'lamination_sheet': lamination_sheet,
            'miscellaneous': miscellaneous
        }
        return render(request, 'costing/update.html', context)

def total_cost(request, job_id):
    costing = Costing.objects.get(pk=job_id)
    context = {
        'calculated_cost': costing
    }
    return render(request, 'costing/totalCost.html', context)


def floatConvert(value):
        return None if value == '' or value is None else float(value)



        
def saveJobCostData(form_value, formOfBasicJobElements, formOfPrinting, formOfLaminaiton, formOfPrintingDynamicElements, formOfLaminaitonDynamicElements, formOfOtherElements):
    if formOfBasicJobElements.is_valid() and formOfPrinting.is_valid() and formOfLaminaiton.is_valid() and formOfPrintingDynamicElements.is_valid() and formOfLaminaitonDynamicElements.is_valid() and formOfOtherElements.is_valid():
            
            costing_instance = Costing()
        
            # set the relevant fields from the forms on the Costing instance
            costing_instance.Date = formOfBasicJobElements.cleaned_data['Date']
            costing_instance.Job_Name = formOfBasicJobElements.cleaned_data['Job_Name']
            costing_instance.Job_Size = formOfBasicJobElements.cleaned_data['Job_Size']

            costing_instance.Printing_Type = formOfPrinting.cleaned_data['Printing_Type']
            
            costing_instance.Pet_Qty = formOfPrintingDynamicElements.cleaned_data['Pet_Qty']
            costing_instance.Pet_HST_Qty = formOfPrintingDynamicElements.cleaned_data['Pet_HST_Qty']
            costing_instance.Met_Qty = formOfPrintingDynamicElements.cleaned_data['Met_Qty']
            costing_instance.Poly_Qty = formOfPrintingDynamicElements.cleaned_data['Poly_Qty']
            costing_instance.Ink_Cost_PKG = formOfPrintingDynamicElements.cleaned_data['Ink_Cost_PKG']

            costing_instance.Lamination_Type = form_value.getlist('Lamination_Type')   

            costing_instance.Met_Qty = formOfLaminaitonDynamicElements.cleaned_data['Met_Qty']
            costing_instance.Met_CPP_Qty = formOfLaminaitonDynamicElements.cleaned_data['Met_CPP_Qty']
            costing_instance.Foil_9_Mic_Qty = formOfLaminaitonDynamicElements.cleaned_data['Foil_9_Mic_Qty']
            costing_instance.Foil_30_Mic_Qty = formOfLaminaitonDynamicElements.cleaned_data['Foil_30_Mic_Qty']
            costing_instance.Polly_Qty = formOfLaminaitonDynamicElements.cleaned_data['Polly_Qty']
            costing_instance.Lamination_Cost = formOfLaminaitonDynamicElements.cleaned_data['Lamination_Cost']
            costing_instance.Lamination_Output = formOfLaminaitonDynamicElements.cleaned_data['Lamination_Output']
            costing_instance.Lamination_Cost_Polly = formOfLaminaitonDynamicElements.cleaned_data['Lamination_Cost_Polly']
            costing_instance.Lamination_OutPut_Polly = formOfLaminaitonDynamicElements.cleaned_data['Lamination_OutPut_Polly']
            
            costing_instance.Zipper_Qty = formOfOtherElements.cleaned_data['Zipper_Qty']
            costing_instance.Coating_Cost = formOfOtherElements.cleaned_data['Coating_Cost']
            costing_instance.Sliting_Output = formOfOtherElements.cleaned_data['Sliting_Output']
            costing_instance.Trim_Westag = formOfOtherElements.cleaned_data['Trim_Westag']
            costing_instance.Finished_Good = formOfOtherElements.cleaned_data['Finished_Good']
            
            # save the Costing instance to the database
            return costing_instance
    
def calculateCostOfJob(costing_instance, laminationType):
    costing_instance.Pet_Cost = multiply([costing_instance.Pet_Qty, costing_instance.Pet_Rate])
    costing_instance.Pet_HST_Cost = multiply([costing_instance.Pet_HST_Qty, costing_instance.Pet_HST_Rate])
    costing_instance.Poly_Cost = multiply([costing_instance.Poly_Qty, costing_instance.Poly_Rate])
    costing_instance.Met_Cost = multiply([costing_instance.Met_Qty, costing_instance.Met_Rate])
    costing_instance.Met_CPP_Cost = multiply([costing_instance.Met_CPP_Qty, costing_instance.Met_CPP_Rate])
    costing_instance.Foil_9_Mic_Cost = multiply([costing_instance.Foil_9_Mic_Qty, costing_instance.Foil_9_Mic_Rate])
    costing_instance.Foil_30_Mic_Cost = multiply([costing_instance.Foil_30_Mic_Qty, costing_instance.Foil_30_Mic_Rate])
    costing_instance.Polly_Cost = multiply([costing_instance.Polly_Qty, costing_instance.Polly_Rate])

    if(costing_instance.Printing_Type):
        printing_type = costing_instance.Printing_Type.replace(' ','_') + "_Qty"
        costing_instance.Ink_Cost = multiply([getattr(costing_instance, printing_type), costing_instance.Ink_Cost_PKG])

        if(laminationType):
            for item in laminationType:
                lamination_type = item.replace(' ','_') + "_Qty"
                if item == 'Polly':
                    costing_instance.Lamination_Cost_PKG_Polly = divide(costing_instance.Lamination_Cost_Polly, getattr(costing_instance, printing_type))
                else:
                    costing_instance.Lamination_Cost_PKG_Polly = divide(costing_instance.Lamination_Cost, getattr(costing_instance, printing_type))
                    costing_instance.Print_Westag = subtractListElements([getattr(costing_instance, printing_type), getattr(costing_instance, lamination_type)])

    costing_instance.Coating_Cost_PKG = divide(costing_instance.Coating_Cost,costing_instance.Lamination_Output)

    costing_instance.Zipper_Cost = float(multiply([costing_instance.Zipper_Qty, costing_instance.Zipper_Rate]))

    totalCostParameters = [costing_instance.Pet_Cost , costing_instance.Pet_HST_Cost , costing_instance.Ink_Cost , costing_instance.Poly_Cost, costing_instance.Met_Cost , costing_instance.Met_CPP_Cost , costing_instance.Foil_9_Mic_Cost , costing_instance.Foil_30_Mic_Cost , costing_instance.Lamination_Cost , costing_instance.Lamination_Cost_Polly , costing_instance.Polly_Cost , costing_instance.Coating_Cost , costing_instance.Zipper_Cost]
    costing_instance.Total_Cost = sum(listNoneFilter(totalCostParameters)) if totalCostParameters else None

    costing_instance.Lamination_Westag = subtractListElements([costing_instance.Lami_total_Output,  sum(listNoneFilter([costing_instance.Sliting_Output, costing_instance.Trim_Westag]))])

    costing_instance.Pouch_Westag = subtractListElements([sum(listNoneFilter([costing_instance.Sliting_Output, costing_instance.Zipper_Qty])), costing_instance.Finished_Good])

    costing_instance.Net_Raw_Material = sum(listNoneFilter([costing_instance.Pet_Qty, costing_instance.Pet_HST_Qty,costing_instance. Met_Qty, costing_instance.Met_CPP_Qty, costing_instance.Foil_9_Mic_Qty, costing_instance.Foil_30_Mic_Qty, costing_instance.Polly_Qty, costing_instance.Zipper_Qty]))
    
    costing_instance.Wet_Gain_Loss = subtractListElements([costing_instance.Finished_Good, costing_instance.Net_Raw_Material])

    costing_instance.Total_Cost_PKG = divide(costing_instance.Total_Cost, costing_instance.Finished_Good)

    return costing_instance

def listNoneFilter(my_list):
    return [float(value) if value and value != '' else 0 for value in my_list]

def subtractListElements(lst):
    result = Decimal(0)
    for item in lst:
        if item is not None:
            result -= Decimal(item)
    return result

def multiply(list):
    filteredList = listNoneFilter(list)
    value = np.prod(filteredList) if filteredList else None
    return value

def divide(num, denom):
    if num is not None and denom is not None and denom is not float(0):
        return Decimal(num)/Decimal(denom)
    else:
        return None

def saveSheetRate(form):
        printingSheetName = form.getlist('printingSheetName')
        printingSheetRate = form.getlist('printingSheetRate')
        laminationSheetName = form.getlist('laminationSheetName')
        laminationSheetRate = form.getlist('laminationSheetRate')
        miscellaneousType = form.getlist('miscellaneousType')
        miscellaneousRate = form.getlist('miscellaneousRate')

        printing_sheet = Printing.objects.filter(Printing_Sheet__in=printingSheetName)
        lamination_sheet = Lamination.objects.filter(Lamination_Sheet__in=laminationSheetName) | Lamination.objects.filter(Lamination_Sheet__in=printingSheetName)
        miscellaneous_type = Miscellaneous.objects.filter(Type__in=miscellaneousType)

        for sheet, rate in zip(printingSheetName, printingSheetRate):
            print("sheet name:")
            print(sheet)
            if sheet == 'Met':
                print("Yes this is Met")
                printing_sheet.filter(Printing_Sheet=sheet).update(Rate=rate)
                lamination_sheet.filter(Lamination_Sheet=sheet).update(Rate=rate)
            else:
                printing_sheet.filter(Printing_Sheet=sheet).update(Rate=rate)

        for sheet, rate in zip(laminationSheetName, laminationSheetRate):
            lamination_sheet.filter(Lamination_Sheet=sheet).update(Rate=rate)

        for sheet, rate in zip(miscellaneousType, miscellaneousRate):
            miscellaneous_type.filter(Type=sheet).update(Rate=rate)
