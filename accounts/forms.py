from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from .models import Accounts

class CustomSignupForm(forms.Form):
    gender = forms.ChoiceField(required=True, label='성별', widget=forms.RadioSelect, choices=(
        (0, '남'),
        (1, '여')
    ))
    phoneNum = forms.CharField(max_length=15, label='핸드폰 번호', widget=forms.TextInput(attrs={'placeholder': '핸드폰 번호를 입력해주세요.'}))
    birth_day = forms.CharField(max_length=30, label='생년월일', widget=forms.TextInput(attrs={'placeholder': '생년월일을 입력해주세요.'}))
    address = forms.CharField(max_length=100, label='주소', widget=forms.TextInput(attrs={'placeholder': '주소를 입력해주세요.'}))

    def signup(self, request, Accounts):
        Accounts.gender = self.cleaned_data['gender']
        Accounts.phoneNum = self.cleaned_data['phoneNum']
        Accounts.birth_day = self.cleaned_data['birth_day']
        Accounts.address = self.cleaned_data['address']
        Accounts.save()

class CustomSocialSignupForm(forms.Form):
    gender = forms.ChoiceField(required=True, label='성별', widget=forms.RadioSelect, choices=(
        (0, '남'),
        (1, '여')
    ))
    phoneNum = forms.CharField(max_length=15, label='핸드폰 번호', widget=forms.TextInput(attrs={'placeholder': '핸드폰 번호를 입력해주세요.'}))
    birth_day = forms.CharField(max_length=30, label='생년월일', widget=forms.TextInput(attrs={'placeholder': '생년월일을 입력해주세요.'}))
    address = forms.CharField(max_length=100, label='주소', widget=forms.TextInput(attrs={'placeholder': '주소를 입력해주세요.'}))

    def signup(self, request, Accounts):
        Accounts.gender = self.cleaned_data['gender']
        Accounts.phoneNum = self.cleaned_data['phoneNum']
        Accounts.birth_day = self.cleaned_data['birth_day']
        Accounts.address = self.cleaned_data['address']
        Accounts.save()
        