import django_filters
from .models import Skill,Project,Department,Employee

class SkillFilter(django_filters.FilterSet):
    class Meta:
        model = Skill
        fields = ['name', 'id']
        
class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['name', 'location']
        
class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = ['name']
        
class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['name', 'Department']