from django import forms

class InvestmentForm(forms.Form):
    starting_amout = forms.FloatField(label="начальный период")
    number_of_years = forms.FloatField(label="количество лет")
    return_rate = forms.FloatField(label="процентная ставка")
    annual_additional_contribution = forms.FloatField(label="процентные пополнения")