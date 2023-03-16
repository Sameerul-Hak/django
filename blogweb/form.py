from django import forms
from .models import Projects

# class ProjectsForm(forms.ModelForm):
#     class Meta:
#         model=  Projects
#         fields=['project_name','phone_number','basic_idea','project_type']
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class ProjectsForm(forms.ModelForm):
    class Meta:
        model= Projects
        fields=['project_name','phone_number','basic_idea','project_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('project_name', css_class='form-control', placeholder='Enter Project Name'),
            Field('phone_number', css_class='form-control', placeholder='Enter Phone Number'),
            Field('basic_idea', css_class='form-control', placeholder='Enter Basic Idea'),
            Field('project_type', css_class='form-control', placeholder='Enter Project Type'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
