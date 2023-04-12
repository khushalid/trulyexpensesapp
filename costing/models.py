from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
import json

# Create your models here.

class Printing(models.Model):
    Printing_Sheet = models.CharField(max_length=255, null=True)
    Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)

    def __str__(self) -> str:
        return str(self.Printing_Sheet) + '\'s ' + 'rate is: ' + str(self.Rate)

class Lamination(models.Model):
    Lamination_Sheet = models.CharField(max_length=255, null=True)
    Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)

    def __str__(self) -> str:
        return str(self.Lamination_Sheet) + '\'s ' + 'rate is: ' + str(self.Rate)  

class Miscellaneous(models.Model):
    Type = models.CharField(max_length=255, null=True)
    Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)

    def __str__(self) -> str:
        return str(self.Type) + '\'s ' + 'rate is: ' + str(self.Rate)  

class Costing(models.Model):
    Date = models.DateTimeField()
    Job_Name = models.CharField(max_length=255, null=True)
    Job_Size = models.CharField(max_length=255, null=True)
    Printing_Type = models.CharField(max_length=255, null=True)
    Pet_Qty = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Pet_Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Pet_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Pet_HST_Qty = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Pet_HST_Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Pet_HST_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Poly_Qty = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Poly_Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Poly_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Ink_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Ink_Cost_PKG = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Lamination_Type = models.CharField(max_length=255, null=True)
    Met_Qty = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Met_Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Met_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Met_CPP_Qty = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Met_CPP_Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Met_CPP_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Foil_9_Mic_Qty = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Foil_9_Mic_Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Foil_9_Mic_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Foil_30_Mic_Qty = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Foil_30_Mic_Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Foil_30_Mic_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Lamination_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Lamination_Cost_PKG = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Lamination_Output = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Polly_Qty = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Polly_Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Polly_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Lamination_Cost_Polly = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Lamination_Cost_PKG_Polly = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Lamination_OutPut_Polly = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Coating_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Coating_Cost_PKG = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Zipper_Qty = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Zipper_Rate = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Zipper_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Total_Cost = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Lami_total_Output = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Sliting_Output = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Print_Westag = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Lamination_Westag = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Trim_Westag = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Pouch_Westag = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Net_Raw_Material = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Finished_Good = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Wet_Gain_Loss = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)
    Total_Cost_PKG = models.DecimalField(max_length=None, default=None, decimal_places=3, max_digits=20, blank=True ,null=True)

    @property
    def Printing_Qty(self):
        return ''
    
    def __str__(self) -> str:
        return str(vars(self))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_date = self.Date

    def save(self, *args, **kwargs):
        if not self.pk:
            self.Date = timezone.now().strftime('%Y-%m-%dT%H:%M:%S')
        elif self.Date is not None:
            self.Date = self.original_date
        super().save(*args, **kwargs)
