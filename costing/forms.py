from django import forms
from django.forms import formset_factory
from .models import *
from django.utils import timezone


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='')

    # Add CSS classes to the form fields
    search_query.widget.attrs.update({'class': 'form-control', 'placeholder': 'Search...'})

class basicJobElementForm(forms.ModelForm):
    class Meta:
        model = Costing
        fields = ['Date', 'Job_Name', 'Job_Size']
        widgets = {
            'Date': forms.DateInput(attrs={'class': 'form-control mb-3', 'placeholder':'Date', 'type': 'datetime-local'}),
            'Job_Name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder':'Job Name'}),
            'Job_Size': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder':'Job Size'}),  
        }
        
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('Date')
        if not date:
            cleaned_data['Date'] = timezone.now().strftime('%Y-%m-%dT%H:%M:%S')
        else:
            cleaned_data['Date'] = date.strftime('%Y-%m-%dT%H:%M:%S')
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['Date'].initial = timezone.now().strftime('%Y-%m-%dT%H:%M:%S')
        else:
            print(self.instance.Date)
            self.fields['Date'].initial = self.instance.Date
        for field in self.fields.values():
            field.required = False

class printingForm(forms.ModelForm):
    iquery = Printing.objects.values_list('Printing_Sheet', flat=True).distinct()
    iquery_choices = [('', 'Choose')] + [(id, id) for id in iquery]
    Printing_Type = forms.ChoiceField(choices=iquery_choices, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Printing Type', 'id': 'printing'}))
       
    class Meta:
        iquery = Printing.objects.values_list('Printing_Sheet', flat=True).distinct()
        iquery_choices = [('', 'Choose')] + [(id, id) for id in iquery]
        Printing_Type = forms.ChoiceField(choices=iquery_choices, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Printing Type', 'id': 'printing'}))
        model = Costing
        fields = ['Printing_Type']
        widgets = {
            'Printing_Type': forms.Select(attrs={'class': 'form-control mb-3', 'placeholder':'Printing Type', 'id': 'printing'})          
        }
        labels = {
            'Printing_Type': ''
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class laminationForm(forms.ModelForm):
    iquery = Lamination.objects.values_list('Lamination_Sheet', flat=True).distinct()
    iquery_choices = [('', 'Choose')] + [(id, id) for id in iquery]
    Lamination_Type = forms.ChoiceField(choices=iquery_choices,  widget=forms.Select(attrs={'class': 'form-control Lamination_Type', 'placeholder':'Lamination Type', 'id': 'lamination'}))
        
    class Meta:
        iquery = Lamination.objects.values_list('Lamination_Sheet', flat=True).distinct()
        iquery_choices = [('', 'Choose')] + [(id, id) for id in iquery]
        Lamination_Type = forms.ChoiceField(choices=iquery_choices,  widget=forms.Select(attrs={'class': 'form-control Lamination_Type', 'placeholder':'Lamination Type', 'id': 'lamination'}))
        model = Costing
        fields = ['Lamination_Type']
        widgets = {
            'Lamination_Type': forms.Select(attrs={'class': 'form-control Lamination_Type', 'placeholder':'Lamination Type'}),
        }
        labels={
            'Lamination_Type': ''
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class printingDynamicFields(forms.ModelForm):
    
    class Meta:
        model = Costing
        fields = ['Pet_Qty','Pet_HST_Qty','Met_Qty','Poly_Qty','Ink_Cost_PKG']
        widgets = {
            'Pet_Qty': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3 printing-dynamic-fields','style': 'display:none', 'placeholder':'Pet Qty'}),
            'Pet_HST_Qty': forms.TextInput(attrs={'class': 'form-control mb-3 printing-dynamic-fields','style': 'display:none', 'placeholder':'Pet HST Qty'}),
            'Met_Qty': forms.TextInput(attrs={'class': 'form-control mb-3 printing-dynamic-fields', 'style': 'display:none', 'placeholder':'Met Qty'}),
            'Poly_Qty': forms.TextInput(attrs={'class': 'form-control mb-3 printing-dynamic-fields','style': 'display:none', 'placeholder':'Poly Qty'}),
            'Ink_Cost_PKG': forms.TextInput(attrs={'class': 'form-control printing-dynamic-fields', 'style': 'display:none', 'placeholder':'Ink Cost PKG'})
        }
        labels = {
            'Pet_Qty': '', 
            'Pet_HST_Qty': '',
            'Met_Qty': '',
            'Poly_Qty': '',
            'Ink_Cost_PKG': ''
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class laminationDynamicFields(forms.ModelForm):
    
    class Meta:
        model = Costing
        fields = ['Met_Qty', 'Met_CPP_Qty', 'Foil_9_Mic_Qty', 'Foil_30_Mic_Qty', 'Polly_Qty', 'Lamination_Cost', 'Lamination_Output', 'Lamination_Cost_Polly', 'Lamination_OutPut_Polly']
        widgets = {
            'Met_Qty': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3 lamination-dynamic-fields', 'style': 'display:none', 'placeholder':'Met Qty'}),
            'Met_CPP_Qty': forms.TextInput(attrs={'class': 'form-control mb-3 lamination-dynamic-fields','style': 'display:none', 'placeholder':'Met CPP Qty'}),
            'Foil_9_Mic_Qty': forms.TextInput(attrs={'class': 'form-control mb-3 lamination-dynamic-fields','style': 'display:none', 'placeholder':'Foil 9 Mic Qty'}), 
            'Foil_30_Mic_Qty': forms.TextInput(attrs={'class': 'form-control mb-3 lamination-dynamic-fields','style': 'display:none', 'placeholder':'Foil 30 Mic Qty'}), 
            'Polly_Qty': forms.TextInput(attrs={'class': 'form-control mb-3 lamination-dynamic-fields','style': 'display:none', 'placeholder':'Polly Qty'}),
            'Lamination_Cost': forms.TextInput(attrs={'class': 'form-control mb-3 lamination-dynamic-fields','style': 'display:none', 'placeholder':'Lamination Cost'}), 
            'Lamination_Output': forms.TextInput(attrs={'class': 'form-control mb-3 lamination-dynamic-fields','style': 'display:none', 'placeholder':'Lamination Output'}), 
            'Lamination_Cost_Polly': forms.TextInput(attrs={'class': 'form-control mb-3 lamination-dynamic-fields','style': 'display:none', 'placeholder':'Lamination Cost Polly'}), 
            'Lamination_OutPut_Polly': forms.TextInput(attrs={'class': 'form-control mb-3 lamination-dynamic-fields','style': 'display:none', 'placeholder':'Lamination OutPut Polly'})
            
        }
        labels = {
            'Met_Qty': '',
            'Met_CPP_Qty': '', 
            'Foil_9_Mic_Qty': '', 
            'Foil_30_Mic_Qty': '', 
            'Polly_Qty': '',
            'Lamination_Cost': '', 
            'Lamination_Output': '', 
            'Lamination_Cost_Polly': '', 
            'Lamination_OutPut_Polly': ''
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class otherElementForm(forms.ModelForm):

    class Meta:
        model = Costing
        fields = ['Zipper_Qty', 'Coating_Cost', 'Sliting_Output', 'Trim_Westag', 'Finished_Good']
        widgets = {
            'Zipper_Qty': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3', 'placeholder':'Zipper Qty'}),
            'Coating_Cost': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3', 'placeholder':'Coating Cost'}),
            'Sliting_Output': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3', 'placeholder':'Sliting Output'}),
            'Trim_Westag': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3', 'placeholder':'Trim Westag'}),
            'Finished_Good': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3', 'placeholder':'Finished Good'}),
            
        }
        # labels = {
        #     'Zipper_Qty': 'Hello Zipper', 
        #     'Coating_Cost': '', 
        #     'Sliting_Output': '', 
        #     'Trim_Westag': '', 
        #     'Finished_Good': ''

        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False



