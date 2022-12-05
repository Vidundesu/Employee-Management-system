from django import forms
from .models import Skill,Department,Project,Employee

class TestForm(forms.Form):
    name=forms.CharField()
    
class SkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        fields='__all__'
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'
        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'        
  
    
