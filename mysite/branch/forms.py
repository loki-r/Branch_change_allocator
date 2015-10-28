from django import forms
from .models import Info
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class data(forms.ModelForm):

	def clean_roll_no(self):
		roll_no = self.cleaned_data['roll_no']
		num_letters = len(roll_no)
		if num_letters > 9:
			raise forms.ValidationError("Roll Number cannot exceed 9 digits") 
		if roll_no[0] == '1' and roll_no[1] == '4':
			num_letters = num_letters
		else:
			raise forms.ValidationError("Roll Number should start with 14")
		return roll_no
	def clean_cpi(self):
		cpi = self.cleaned_data['cpi']
		if cpi <= 10 and cpi >= 0:
			return cpi
		else:
			raise forms.ValidationError("CPI should be between 0 and 10 (inclusive)")
	class Meta:
		model = Info
		fields = ['name', 'roll_no', 'present_branch', 'cpi', 'category', 'pref_1', 'pref_2']
		labels = {
			'roll_no':_('Roll Number'),
			'cpi':_('CPI'),
			'pref_1':_('1st preference'),
			'pref_2':_('2dn preference'),
		}


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )		