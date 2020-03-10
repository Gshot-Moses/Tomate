import re
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.core.validators import RegexValidator

from .models import UserInfo, Post


phone_validator = RegexValidator(
		regex = r'^[0-9]+$',
		message = "Phone number must contain digits")
name_validator = RegexValidator(
		regex = r'^[a-zA-Z]+$',
		message = "Name must consist of letters only")

def password_validator(password2, password1):
	if password1 != password2:
		raise forms.ValidationError("Passwords dont match") 

class UserRegistrationForm(forms.forms.Form):
	
	first_name = forms.CharField(
		label = "Name",
		validators = [name_validator],
		widget = forms.TextInput())
	last_name = forms.CharField(
		label = "Last Name",
		validators = [name_validator],
		widget = forms.TextInput())
	date_of_birth = forms.DateField(
		label = "Date of Birth",
		widget = forms.SelectDateWidget(
				years = range(1980, 2010)))
	sex = forms.CharField(
		label = "Sex",
		widget = forms.RadioSelect(
				choices = (['male', 'Male'], ['female', 'Female'])))
	phone = forms.CharField(
		#max_value = 100000000,
		label = "Phone Number",
		validators = [phone_validator],
		widget = forms.TextInput())
	email = forms.EmailField(
		label = "Email Address",
		widget = forms.EmailInput())
	password1 = forms.CharField(
		label = "Password",
		widget = forms.PasswordInput())
	password2 = forms.CharField(
		label = "Confirm Password",
		#validators = [password_validator()],
		widget = forms.PasswordInput())
	profile_pic = forms.ImageField(
			required = False,
			label = "Set profile picture",
			widget = forms.FileInput())

	def clean_profile():
		print self.cleaned_data["profile_pic"]
	#	self.num = []
	#	self.num.append(phone)

	#def clean_password(self):
		#if "password2" in self.cleaned_data:
	#	cleaned_data = super().clean()
	#	password1 = cleaned_data.get("password1")
	#	print password1
			#if "password2" in self.cleaned_data:
	#	password2 = cleaned_data.get("password2")
	#	print password2
	#	if password1 and password2:
	#		if password1 == password2:
	#			return password1
	#		else:
	#			raise forms.ValidationError("Passwords dont match")
		#self.invalid["password"] = "Passwords dont match"
		
		#raise forms.ValidationError("Passwords dont match")
		#print self.cleaned_data

	def clean_email(self):
		#if "email" in self.cleaned_data:
		email = self.cleaned_data["email"]
		print email
		try:
			UserInfo.objects.get(email = email)
		except ObjectDoesNotExist:
			return email
		#self.invalid["email"] = "Email already exists"
		raise forms.ValidationError('Email already exists')

	#def clean_name(self):
	#	name = self.cleaned_data["first_name"]
	#	print name
	#	if not re.search(r'^\w+$', name):
			#self.Invalid["first_name"] = "Invalid first name"
	#		raise forms.ValidationError("Field must only contain alpha characters")
		#last_name = self.cleaned_data["last_name"]
		#if not re.search(r'^\w+$', last_name):
			#self.invalid["last_name"] = "Invalid last name"
		#	raise forms.ValidationError("Field must only contain alpha characters")

	#def clean_phone(self):
	#	phone = self.cleaned_data["phone"]
	#	print phone
	#	for c in phone:
	#		if c not in "1234567890":
	#	if not re.search(r'^\d+$', self.num[0]):
	#		self.invalid["phone"] = ["Phone number must not contain letters",]
	#		if len(str(self.num[0])) < 8:
	#			self.invalid["phone"].append("Phone number must contain at least 8 digits")
	#			raise forms.ValidationError("Must contain at least 8 digits")

	
class LoginForm(forms.forms.Form):
	email = forms.EmailField(

		required = False,
		label = "Email Address",
		widget = forms.EmailInput(attrs = {"placeholder": "Email"}))
	password = forms.CharField(
		required = False,
		label = "Password",
		widget = forms.PasswordInput(attrs = {"placeholder": "Password"}))

	def clean_things(self):
		print "I am being tested"
		email = self.cleaned_data["email"]
		passowrd = self.cleaned_data["password"]
		try:
			user = UserInfo.objects.filter(
				email__iexact = email).filter(
				password__exact = password)[0]
		except IndexError:
			raise forms.ValidationError("Email and password dont match")


class PostForm(forms.forms.Form):
	content = forms.CharField(
		label = "",
		widget = forms.Textarea(attrs = {"placeholder": "Say something", "id": "post-text"}))
	image = forms.ImageField(
		label = "",
		required = False,
		widget = forms.FileInput(attrs = {"id": "file", "class": "inputfile"}))


class CommentForm(forms.forms.Form):
	content = forms.CharField(
		label = "",
		widget = forms.TextInput(attrs = {"id": "search", "placeholder": "Your comment"}))


class SearchForm(forms.forms.Form):
	search = forms.CharField(
		label = "",
		widget = forms.TextInput(attrs = {"placeholder": "Search your friend"}))


class ChatForm(forms.forms.Form):
	content = forms.CharField(
		label = "",
		widget = forms.Textarea(attrs = {"placeholder": "Your message"}))


class ChangeProfilePicForm(forms.forms.Form):
	pic = forms.ImageField(
		label = "",
		required = False,
		widget = forms.FileInput(attrs = {"id": "profilepic", "class": "profilepic"}))