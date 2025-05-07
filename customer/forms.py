from django import forms
from .models import Customer


### formModel with fields
# Create Add Customer Form
# class AddCustomerForm(forms.ModelForm):
#     first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
#         attrs={"placeholder": "First Name", "class": "form-control"}), label="")
#     last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
#         attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
#     date_of_birth = forms.DateField(required=True,
#                                     widget=forms.widgets.DateInput(attrs={"placeholder": "Email", "class": "form-control"}),
#                             label="")
#
#     email = forms.CharField(required=True,
#                             widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
#                             label="")
#     phone_number = forms.IntegerField(required=True,
#                             widget=forms.widgets.NumberInput(attrs={"placeholder": "Phone", "class": "form-control"}),
#                             label="")
#     address = forms.CharField(required=True,
#                               widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control"}),
#                               label="")
#     city = forms.CharField(required=True,
#                            widget=forms.widgets.TextInput(attrs={"placeholder": "City", "class": "form-control"}),
#                        label="")
#     state = forms.CharField(required=True,
#                             widget=forms.widgets.TextInput(attrs={"placeholder": "State", "class": "form-control"}),
#                             label="")
#     phone = forms.IntegerField(required=True,
#                               widget=forms.widgets.NumberInput(attrs={"placeholder": "Zipcode", "class": "form-control"}),
#                               label="")
#     description = forms.CharField(required=True,
#                               widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control"}),
#                               label="")
#     relationship = forms.CharField(required=True,
#                               widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control"}),
#                               label="")
#     class Meta:
#         model = Customer
#         fields = [] ###

# Define FormModel without Fields


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = []


#
class DateInpute(forms.DateInput):
    input_type = 'date'

