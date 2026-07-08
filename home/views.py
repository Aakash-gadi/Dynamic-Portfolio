from django.shortcuts import render,redirect
from .models import hero ,skills,experience,education,project
from django.contrib import messages
from django.contrib.messages import get_messages
from urllib.parse import quote
# det=hero()
# det.name="Aakash"
# det.role3="Android Developer"
# det.role2="Software Engineer"
# det.role1="WebDeveloper"
# det.profile="Full stack Engineer"
# det.email="gabhjbjh@gmail"
# det.phone=976548656
# Create your views here.
def home(request):
    # Check if we redirected from saving new data via query parameter '?saved=true'
    came_from_save = request.GET.get('saved') == 'true'

    # If we didn't just come from save (e.g. page refresh or direct navigation), clear the DB
    if not came_from_save:
        hero.objects.all().delete()
        skills.objects.all().delete()
        education.objects.all().delete()
        experience.objects.all().delete()
        project.objects.all().delete()
    det = hero.objects.first()
    skill = skills.objects.all()
    edu = education.objects.all()
    exp = experience.objects.all()
    project1 = project.objects.all()
    # hero=hero()
    # skill=skills()
    # experience=experience()
    # education=education()
    # project=project()

    # profile1=request.session.pop("profile",None)
    # skill1=request.session.pop("skill",None)
    # experience1=request.session.pop("experience",None)
    # education1=request.session.pop("education",None)
    # project1=request.session.pop("project",None)
    

    # Apply placeholders if database table is empty
    if det is None:
        det = hero(
            name="Your name",
            role1="Role 1",
            role2="Role 2",
            role3="Role 3",
            email="yourmail@gmail.com",
            phone="Your number",
            profile="Your Profile",
            aboutme="Your Description",
            summary="Summary about you",
            Address="Address"
        )

    if not skill.exists():
        skill = [
            {"skill": "HTML", "skillrate": "100"},
            {"skill": "CSS", "skillrate": "90"},
            {"skill": "JavaScript", "skillrate": "75"}
        ]

    if not edu.exists():
        edu = [{"name": "University Name", "year": "20xx-20xx", "address": "University Address", "desc": "Description about your education"}]

    if not exp.exists():
        exp = [{"nameofposition": "Name of Position", "nameofcompany": "Name of Company", "years": "20xx-20xx", "address": "Address of university", "desc1": "Description 1", "desc2": "Description 2", "desc3": "Description 3"}]

    if not project1.exists():
        project1 = [{"name": "Name of Project", "description": "Description of Project", "link": "Link for project if any"}]
        
    # if profile1:
    #     hero.name=profile1["name"]
    #     hero.role1=profile1["role1"]
    #     hero.role2=profile1["role2"]
    #     hero.role3=profile1["role3"]
    #     hero.email=profile1["email"]
    #     hero.phone=profile1["phone"]
    #     hero.profile=profile1["profile"]
    #     hero.aboutme=profile1["aboutme"]
    #     hero.summary=profile1["summary"]
    #     hero.Address=profile1["Address"]
    # else:
    #     hero.name="Your name"
    #     hero.role1="Role1"
    #     hero.role2="Role2"
    #     hero.role3="Role3"
    #     hero.email="email"
    #     hero.phone="phone"
    #     hero.profile="profile"
    #     hero.aboutme="About you"
    #     hero.summary="Summary"
    #     hero.Address="Address"
    # if skill1:
    #     skill.skill=skill1['name']
    #     skill.skillrate=skill1['skillrate']
    # else:
    #     #default
    #     skill.skill="html"
    #     skill.skillrate=skill1['skillrate']
        

    return render(request, 'index.html', {'det': det, 'skill': skill, 'exp': exp, 'edu': edu, 'project1': project1})
def makemine(request):
    if (request.method=="POST"):
      
        form_type = request.POST.get("form_type")
        if(form_type=="profile"):
            # request.session['profile']={

            hero.objects.all().delete()
            hero(
                 
            name=request.POST.get("name"),
            role1=request.POST.get("role1"),
            role2=request.POST.get("role2"),
            image=request.FILES.get("image"),
            role3=request.POST.get("role3"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            profile=request.POST.get("profile"),
            aboutme=request.POST.get("aboutme"),
            summary=request.POST.get("summary")
            # "name":request.POST.get("name"),
            # "role1":request.POST.get("role1"),
            # "role2":request.POST.get("role2"),
            # "role3":request.POST.get("role3"),
            # "email":request.POST.get("email"),
            # "phone":request.POST.get("phone"),
            # "profile":request.POST.get("profile"),
            # "aboutme":request.POST.get("aboutme"),
            # "summary":request.POST.get("summary")
            # }
            ).save()
        elif form_type=="projects":
             project(
             name=request.POST.get("name"),
             description=request.POST.get("description"),
             link=request.POST.get("link")
             ).save()
            # request.session['project']={
            #     "name":request.POST.get("name"),
            #  "description":request.POST.get("description"),
            #  "link":request.POST.get("link")
            # }
        elif  form_type=="experience":
             experience(
                  
             nameofcompany=request.POST.get("nameofcompany"),
             nameofposition=request.POST.get("nameofposition"),
             years=request.POST.get("years"),
             desc1=request.POST.get("description1"),
             desc2=request.POST.get("description2"),
             desc3=request.POST.get("description3")
             ).save()
            # request.session['experience']={
            #     "nameofcompany":request.POST.get("nameofcompany"),
            #  'nameofposition':request.POST.get("nameofposition"),
            #  "years":request.POST.get("years"),
            #  "desc1":request.POST.get("description1"),
            #  "desc2":request.POST.get("description2"),
            #  "desc3":request.POST.get("description3")
            # }
        elif( form_type == "education"):
     
        
             education(
                  
             name=request.POST.get("name"),
             year=request.POST.get("year"),
             desc=request.POST.get("description"),
             address=request.POST.get("address")
             ).save()
            # request.session['education']={
            #  "name":request.POST.get("name"),
            #  "year":request.POST.get("year"),
            #  "desc":request.POST.get("description"),
            #  "address":request.POST.get("address")
            # }

        elif form_type== "skills":
             skills(
                  
             skill=request.POST.get("name"),
             skillrate=request.POST.get("skillrate"),
             ).save()
            # request.session['skills']={
            #     "skill":request.POST.get("name"),
            #     "skillrate":request.POST.get("skillrate")
            # }
        elif form_type=="done":
            return redirect("/?saved=true")
    return render(request,"makemine.html")

# def skills1(r):
#     # if not skill.exists():
#     #     skill=skills(
#     #     skill="Your skills",
#     #     skillrate='100'
#     #     )
#     return render(r,'index.html',{'skill':skill})
def submitmail(request):
    if request.method == "POST":
        return render(request, "open_mail.html", {
            "mailto": "mailto:gadiakash10gtrfr@gmail.com"
        })