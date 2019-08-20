from django import forms
from .schools import get_schools
from django.core.exceptions import ValidationError

class CollegeForm(forms.Form):
    def __init__(self,*args,**kwargs):
        self.schools = kwargs.pop('schools')
        schools_tuple = []
        for school in sorted(self.schools):
            schools_tuple.append((school, school))
        super().__init__(*args, **kwargs)
        self.fields['college'].widget = forms.Select(choices=schools_tuple)

    def clean(self):
        cleaned_data = super().clean()

        email_suffix = cleaned_data.get('email').split('@')[1]
        valid_emails = self.schools.get(cleaned_data.get('college'))
        print('College', valid_emails)
        valid = False
        for email in valid_emails:
            if email_suffix == email:
                valid = True
                break

        if not valid:
            raise ValidationError('Invalid College Email')

        return cleaned_data    

    college = forms.CharField(label="College Name")
    email   = forms.EmailField(label="College Email")