from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserAddForm(UserCreationForm):
	'''
	Extending UserCreationForm - with email

	'''
	email = forms.EmailField(label="メールアドレス",widget=forms.EmailInput(attrs={'placeholder':'eg.rajparmar@.com'}))
	username = forms.CharField(label='ユーザ名',widget=forms.TextInput(attrs={'placeholder':'ユーザ名'}))
	password1 = forms.CharField(label='パスワード',widget=forms.PasswordInput(attrs={'placeholder':'パスワード'}))
	password2 = forms.CharField(label='パスワード確認',widget=forms.PasswordInput(attrs={'placeholder':'パスワード確認'}))

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		

	





class UserLogin(forms.Form):
	username = forms.CharField(label='ユーザ名',widget=forms.TextInput(attrs={'placeholder':'usesrname'}))
	password = forms.CharField(label='パスワード',widget=forms.PasswordInput(attrs={'placeholder':'password'}))


