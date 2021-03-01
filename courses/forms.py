from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template


class CoursesForms(forms.Form):
    nome = forms.CharField(label='nome', max_length=200)
    email = forms.EmailField(label='e-mail')
    menssagem = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)


    def send_mail(self, course):
        subject = '[%s] Contato' % course
        context = {
            'nome': self.cleaned_data['nome'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['menssagem']
        }
        template_name = 'cursos/contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )
