from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Costing(models.Model):
    Date = models.DateTimeField(default=datetime.datetime.today)
    Job_Name = models.CharField(max_length=255, blank=True, null=True)
    Job_Size = models.CharField(max_length=255, blank=True, null=True)
    Pet_Qty = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Pet_Rate = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Pet_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Pet_HST_Qty = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Pet_HST_Rate = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Pet_HST_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Ink_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Ink_Cost_PKG = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Met_Qty = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Met_Rate = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Met_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Met_CPP_Qty = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Met_CPP_Rate = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Met_CPP_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Foil_9_Mic_Qty = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Foil_9_Mic_Rate = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Foil_9_Mic_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Foil_30_Mic_Qty = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Foil_30_Mic_Rate = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Foil_30_Mic_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Lamination_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Lamination_Cost_PKG = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Lamination_Output = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Polly_Qty = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Polly_Rate = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Polly_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Lamination_Cost_Polly = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Lamination_Cost_PKG_Polly = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Lamination_OutPut_Polly = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Coating_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Coating_Cost_PKG = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Zipper_Qty = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Zipper_Rate = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Zipper_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Total_Cost = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Lami_total_Output = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Sliting_Output = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Print_Westag = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Lamination_Westag = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Trim_Westag = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Pouch_Westag = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Net_Raw_Material = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Finished_Good = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Wet_Gain_Loss = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)
    Total_Cost_PKG = models.DecimalField(max_length=None, decimal_places=3, max_digits=20, null=True)

    def __str__(self) -> str:
        return str(user) + '\'s ' + 'costing'   
