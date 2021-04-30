from django import forms
from .models import Comment

class CommentModelForm(forms.ModelForm):
    # print("Entrou no CommentModelForm.")
    # error_messages = {
    #         'email_errado': ("Digite o Email Correto Burro")
    # }
    # email = forms.EmailField(label=("Email"),
    #                          widget=forms.EmailInput,
    #                          help_text= ("Entre com o email correto para verificação."))

    class Meta:
        # print('MEU DEUS ...... ')
        model = Comment
        fields = ['name', 'comment', 'email']

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if email.split('@')[1] is False:
    #         print("FALSE")
    #         raise forms.ValidationError(
    #             self.error_messages['email_errado'],
    #             code == 'email_errado'
    #         )
    #     else:
    #         print("TRUE")

# class CommentForm(forms.Form):
    # print("Entrou no CommentForm.")
    # email = self.cleaned_data.get('email')
    # email = form['email'].value().split('@')[1]
    # email = forms.EmailField(label='SEU EMAIL canalha')
    # teste_data = forms.EmailField(label='seu email canalha', max_length=100)

    # def clean_email(self):
    #     print('def clean_email')
    #     email = self.cleaned_data['email']
    #     # email = form['email'].value().split('@')[1]
    #     if email.split('@')[1] is False:
    #         print("FALSE")
    #         raise forms.ValidationError(
    #             self.error_messages['email_errado'],
    #             code=='email_errado'
    #         )
    #     else:
    #         print("TRUE")
    #     # print(email)
    #     return email



