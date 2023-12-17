from django import forms


class RegisterFrom(forms.Form):
    login = forms.CharField(label = 'Введите желаемый логин')
    name = forms.CharField(label='Введите ваше имя')
    surname = forms.CharField(label='Введите фамилию')