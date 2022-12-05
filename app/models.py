from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length= 1000)
    
    def __str__(self):
        return self.name
        
class Department(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.DecimalField(max_digits=10,decimal_places=0)
    
    def __str__(self):
        return self.name
       
       
class Employee(models.Model):
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=20)
    type=(('full time',"Full Time"),
         ('part time',"Part Time"))
    Job_Type=models.CharField(max_length=20,choices=type,default="full time")
    skill = models.ManyToManyField(Skill)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    spouse= models.ForeignKey("self", on_delete=models.CASCADE, blank= True, null= True)
    date_of_marriage= models.DateField(blank= True, null=True)
    
    
    def __str__(self):
        return self.name
        
class Project(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=13,decimal_places=2)
    location = models.CharField(max_length=30)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Workson(models.Model):
    Duration= models.DecimalField(max_digits=5,decimal_places=0)
    employee= models.ForeignKey(Employee,on_delete=models.CASCADE)
    project= models.ForeignKey(Project,on_delete=models.CASCADE)
    
    def __str__(self):
        duration = str(self.Duration)
        return duration