from django import forms

class CoursesForms(forms.Form):
    nome = forms.CharField(label='nome', max_length=200)
    email = forms.EmailField(label='e-mail')
    menssagem = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)
