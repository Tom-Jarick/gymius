from django.db import models

# Create your models here.
class User(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    gender_type= {('F','Female'),('M','Male'),}
    gender = models.CharField(max_length=1, choices=gender_type)
    created_on= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class WorkOutInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=30)
    set_count = models.CharField(max_length=30)
    break_time = models.CharField(max_length=30)
    excercise_category = {('PU','PushUp'),('SU','SitUp'),('PL','Plank')}
    excercise = models.CharField(max_length=1, choices=excercise_category)
    activity_time = models.DateTimeField(auto_now_add=True)
    completion = models.BooleanField(default=False)
    def __str__(self):
        return '%s %s' % (self.excercise, self.activity_time)

class Biometrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True, auto_now_add= False)
    def __str__(self):
        return '%s %s %s ' % (self.age, self.height, self.weight)