from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Accounts


class SignupForm(forms.Form):
    phoneNum = forms.CharField(label=_('전화번호'), max_length=15, widget=forms.TextInput(attrs={'placeholder':_('전화번호를 입력해주세요.')}))
    address = forms.CharField(label=_('주소'),
    max_length=150, widget=forms.TextInput(attrs={'placeholder':_('주소를 입력해주세요.')}))

    def signup(self, request, user):
        accounts = Accounts()
        accounts.phoneNum = self.cleaned_data['phoneNum']
        accounts.address = self.cleaned_data['address']
        accounts.save()
        
