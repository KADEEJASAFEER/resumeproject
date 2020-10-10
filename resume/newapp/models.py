from django.db import models

# Create your models here.

class ResumeModel(models.Model):
    fullname=models.CharField(max_length=120)
    email=models.EmailField(max_length=100)
    dob=models.CharField(max_length=50)
    choice=(
        ('10','10'),
        ('+2','+2'),
        ('Diploma', 'Diploma'),
        ('Degree', 'Degree'),
        ('P.G', 'P.G'),
        ('B.Tech', 'B.Tech'),
        ('M.Tech','M.tech')
    )
    qualification=models.CharField(max_length=50,choices=choice)
    profilepicture=models.ImageField(upload_to="images")

    def __str__(self):
        return self.fullname
