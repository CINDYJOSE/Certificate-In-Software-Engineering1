from django.forms import ModelForm

#accessing our models so that we can link them to the forms

from .models import *

#we are updating or ading on the stock
# class Meta is used to access a model and we can  manupliate the model
class registrationform(ModelForm):
    class Meta:
        model = customerRegistratio
        fields = ['recievedQuantity']