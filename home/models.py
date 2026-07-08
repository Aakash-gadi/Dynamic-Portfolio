from django.db import models

# # Create your models here.
class hero(models.Model):
    name=models.CharField()
    role1=models.CharField()
    role2=models.CharField()
    
    image = models.ImageField(
    upload_to="profile_images/",
    blank=True,
    null=True
)
    role3=models.CharField()
    email=models.EmailField()
    phone=models.CharField()
    profile=models.CharField()
    aboutme=models.TextField(default="Your Description here",blank=True,null=True)
    Address=models.CharField(default="Address")
    summary=models.TextField(default="Summary about you")
    

    #this above default is just when all have data but only single have none then 
    # it display the default 
    # but if every thing has none it dont get the default
# class hero():
#     name:str
#     role1:str
#     role2:str
#     role3:str
#     email:str
#     phone:int
#     profile:str

# class hero(models.Model):
#     name:models.IntegerField
#     role1:models.CharField(max_length=100)
#     role2:str
#     role3:str

class skills(models.Model):
    skill=models.CharField()
    skillrate=models.CharField()

class education(models.Model):
    name=models.CharField()
    year=models.CharField(default="From-to")
    address=models.CharField()
    desc=models.TextField()

class experience(models.Model):
    nameofposition=models.CharField()
    nameofcompany=models.CharField()
    years=models.TextField()
    address=models.CharField()
    desc1=models.CharField()
    desc2=models.CharField(default="Description 2")
    desc3=models.CharField(default="Description 3")

class project(models.Model):
    name=models.CharField()
    description=models.TextField()
    link=models.TextField()    
# class hero():
#     name:str
#     role1:str
#     role2:str
#     role3:str
#     email:str
#     phone:int
#     profile:str 
#     aboutme:str
#     Address=str
#     summary=str


  
# class skills():
#     skill:str
#     skillrate:int
 
# class education():
#     name:str
#     year:str
#     address:str
#     desc:str

# class experience():
#     nameofposition:str
#     nameofcompany:str
#     years:str
#     address:str
#     desc1:str
#     desc2:str
#     desc3:str
 

# class project():
#     name=str
#     description=str
#     link=str

