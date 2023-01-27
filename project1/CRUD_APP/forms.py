
from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'eid': 'EMPLOYEE ID:',
            'fname': 'FIRST NAME:',
			'lname' :'LAST NAME:',
			'address': 'ADDRESS:',
            'age': 'AGE:',
            'contactno': 'CONTACT NUMBER'
        }

        widgets = {
            'address': forms.Textarea()
        }
