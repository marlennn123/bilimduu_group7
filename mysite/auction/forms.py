from allauth.account.forms import SignupForm
from django import forms


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')
    age = forms.IntegerField(label='Возраст')
    country = forms.CharField(max_length=30, label='Страна')

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)

