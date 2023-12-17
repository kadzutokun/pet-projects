from django import forms


class BioFrom(forms.Form):
    choicesorderstatus = [
        ('KFU','Казанский Федеральный Университет'),
        ('KAI','Казанский Авиационный Институт'),
        ('КНИТУ','Казанский национальный исследовательский технологический университет'),
        ('КГЭУ','Казанский государственный экономический университет'),
        ('Другой','Нет в списке')
    ]
    name = forms.CharField(label='Введите ваше имя')
    surname = forms.CharField(label='Введите фамилию')
    university = forms.ChoiceField(label='Выберите с какого вы университета', choices=choicesorderstatus)