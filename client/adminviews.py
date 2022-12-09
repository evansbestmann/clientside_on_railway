#import datetime
import json
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage,send_mail
from django.template.loader import render_to_string
from mailjet_rest import Client
from .models import *

def admin_home(request):
    return render (request,"admin_templates/home_content.html")

def addclient(request):
    return render (request,"admin_templates/addclient.html")

def addclient_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        username= request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        sentpassword = password
        # print(sentpassword)
        address = request.POST.get("address")
        client_name = username


        try:
            user=CustomUser.objects.create_user(username=username, password=password,email=email,sentpassword=sentpassword,user_type=2)
            user.client.address=address
            user.client.sentpassword=sentpassword
            user.client.client_name = client_name
            user.save()
            # print(user.client.sentpassword)
            messages.success(request,"client added successfully")
            return HttpResponseRedirect(reverse("manageclient"))
        except:
            messages.error(request, "Failed to add client")
            return HttpResponseRedirect(reverse("addclient"))

def manageclient(request):
    clients=Client.objects.all().order_by("-id")
    return render(request, "admin_templates/manageclient.html",{"clients":clients})

def editclient(request, client_id):#as passed in url
    clients=Client.objects.get(admin=client_id)
    #return HttpResponse("client id :" +client_id) to test if its returning correct user id
    return render(request, "admin_templates/editclient.html", {"clients": clients, "id":client_id})

def editclient_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        client_id= request.POST.get("client_id")
        if client_id==None:
            return HttpResponseRedirect(reverse("manageclient"))
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        client_name = username
        try:
            user = CustomUser.objects.get(id=client_id)
            user.username = username
            user.email = email
            user.save()

            client = Client.objects.get(admin=client_id)
            client.address = address
            user.client.client_name = client_name
            client.save()
            # print(user.password)
            messages.success(request, "client Edited successfully")
            return HttpResponseRedirect(reverse("manageclient"))
        except:
            messages.error(request, "Failed to edit client")
            return HttpResponseRedirect(reverse("editclient",kwargs={"client_id":client_id}))

def deleteclient(request):
    client_id = request.POST.get("client_id")
    if client_id == None:
        return HttpResponseRedirect(reverse("manageclient"))
    try:
        user = CustomUser.objects.get(id=client_id)
        client = Client.objects.get(admin=client_id)
        user.delete()
        client.delete()
        messages.success(request, "Client Deleted successfully")
        return HttpResponseRedirect(reverse("manageclient"))
    except:
        messages.error(request, "Client Failed to delete")
        return HttpResponseRedirect(reverse("manageclient"))


def addfield(request):
    clients= CustomUser.objects.filter(user_type=2)
    return render(request, "admin_templates/addfield.html",{"clients":clients})

def addfield_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        client_id=request.POST.get("client")
        field_name=request.POST.get("field_name")
        client = CustomUser.objects.get(id=client_id)
        try:
            field_model = Fields(client_id=client, field_name=field_name)
            field_model.save()
            messages.success(request, "Field added successfully")
            return HttpResponseRedirect(reverse("managefield"))
        except:
            messages.error(request, "Failed to edit client")
            return HttpResponseRedirect(reverse("addfield"))

def managefield(request):
    fields=Fields.objects.all().order_by("-id")
    return render(request, "admin_templates/managefield.html",{"fields":fields})

def editfield(request, field_id):#as passed in url
    fields=Fields.objects.get(id=field_id)
    clients = CustomUser.objects.filter(user_type=2)
    #return HttpResponse("client id :" +client_id) to test if its returning correct user id
    return render(request, "admin_templates/editfield.html", {"fields": fields,"clients":clients, "id":field_id})

def editfield_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        field_id=request.POST.get("field_id")
        if field_id==None:
            return HttpResponseRedirect(reverse("managefield"))
        client_id=request.POST.get("client")
        field_name=request.POST.get("field_name")

        try:
                client = CustomUser.objects.get(id=client_id)
                field_model = Fields(id=field_id)
                field_model.field_name = field_name
                field_model.client_id = client
                field_model.save()
                messages.success(request, "Field edited successfully")
                return HttpResponseRedirect(reverse("managefield"))
        except:
                messages.error(request, "Failed to edit client")
                return HttpResponseRedirect(reverse("editfield",kwargs={"field_id":field_id}))

def deletefield(request):
    field_id = request.POST.get("field_id")
    if field_id == None:
        return HttpResponseRedirect(reverse("managefield"))
    try:
        field = Fields.objects.get(id=field_id)
        field.delete()
        messages.success(request, "Field Deleted successfully")
        return HttpResponseRedirect(reverse("managefield"))
    except:
        messages.error(request, "Field Failed to delete")
        return HttpResponseRedirect(reverse("managefield"))

def addlaserrep(request):
    return render(request, "admin_templates/addlaserrep.html")

def addlaserrep_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        repname = request.POST.get("laserrep_name")
        repposition = request.POST.get("laserrep_position")

        try:
           rep_model = LaserRep(laserrep_name=repname, position=repposition)
           rep_model.save()
           messages.success(request, "Representative added successfully")
           return HttpResponseRedirect(reverse("addlaserrep"))
        except:
           messages.error(request, "Failed to add  Representative")
           return HttpResponseRedirect(reverse("addlaserrep"))


def managelaserrep(request):
    reps = LaserRep.objects.all().order_by("-id")
    return render(request, "admin_templates/managereps.html", {"reps": reps})

def editreps(request, rep_id):#as passed in url
    reps=LaserRep.objects.get(id=rep_id)
    #return HttpResponse("client id :" +client_id) to test if its returning correct user id
    return render(request, "admin_templates/editreps.html", {"reps": reps, "id":rep_id})


def editlaserrep_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        rep_id=request.POST.get("rep_id")
        repname = request.POST.get("laserrep_name")
        repposition = request.POST.get("laserrep_position")

        try:
           rep_model = LaserRep.objects.get(id=rep_id)
           rep_model.laserrep_name=repname
           rep_model.position=repposition
           rep_model.save()
           messages.success(request, "Representative edited successfully")
           return HttpResponseRedirect(reverse("managereps"))
        except:
           messages.error(request, "Failed to edit  Representative")
           return HttpResponseRedirect(reverse("editreps",kwargs={"rep_id":rep_id}))

def deletelaserrep(request):
    rep_id = request.POST.get("rep_id")
    if rep_id == None:
        return HttpResponseRedirect(reverse("managereps"))
    try:
        rep = LaserRep.objects.get(id=rep_id)
        rep.delete()
        messages.success(request, "Rep Deleted successfully")
        return HttpResponseRedirect(reverse("managereps"))
    except:
        messages.error(request, "Rep Failed to delete")
        return HttpResponseRedirect(reverse("managereps"))

def addjobstatus(request):
    fields = Fields.objects.all()
    clients = Client.objects.all()
    jobstatuses=JobStatus.objects.all()
    laserreps=LaserRep.objects.all()
    return render(request, "admin_templates/addjobstatus.html",{"fields":fields,"clients":clients,"jobstatuses":jobstatuses,"laserreps":laserreps})

def addjobstatus_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        status= request.POST.get("status_name")
        try:
            status_model=JobStatus(jobstatus=status)
            status_model.save()
            messages.success(request, "Status added successfully")
            return HttpResponseRedirect(reverse("addjobstatus"))
        except:
            messages.error(request, "Failed to add  Status")
            return HttpResponseRedirect(reverse("addjobstatus"))

def managejobstatus(request):
    statuses=JobStatus.objects.all().order_by("-id")
    return render(request, "admin_templates/managejobstatus.html", {"statuses": statuses})

def editjobstatus(request, status_id):#as passed in url
    statuses=JobStatus.objects.get(id=status_id)
    #return HttpResponse("client id :" +client_id) to test if its returning correct user id
    return render(request, "admin_templates/editjobstatus.html", {"statuses": statuses, "id":status_id})

def editjobstatus_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        status_id=request.POST.get("status_id")
        status = request.POST.get("status_name")
        try:
            status_model = JobStatus(id=status_id,jobstatus=status)
            status_model.save()
            messages.success(request, "Status edited successfully")
            return HttpResponseRedirect(reverse("managejobstatus"))
        except:
            messages.error(request, "Failed to edit  Status")
            return HttpResponseRedirect(reverse("editjobstatus",kwargs={"status_id":status_id}))

def deletestatus(request):
    status_id = request.POST.get("status_id")
    if status_id == None:
        return HttpResponseRedirect(reverse("managejobstatus"))
    try:
        status = JobStatus.objects.get(id=status_id)
        status.delete()
        messages.success(request, "Level Deleted successfully")
        return HttpResponseRedirect(reverse("managejobstatus"))
    except:
        messages.error(request, "Level Failed to delete")
        return HttpResponseRedirect(reverse("managejobstatus"))

def addjob(request):
    clients=CustomUser.objects.filter(user_type=2)
    statuses=JobStatus.objects.all()
    laserreps=LaserRep.objects.all()
    fields=Fields.objects.all()
    passwordsent=Client.objects.all()

    return render(request, "admin_templates/addjob.html", {"fields":fields,"clients":clients,"statuses":statuses,"laserreps":laserreps,"passwordsent":passwordsent})

def getfields(request):
    client = json.loads(request.body)#here we get the body from our fetch api that was already converted to string  with json.stringify
    client_id=client["id"]#'id' key of data passed to backend from id:clientval in our fetch api
    fields=Fields.objects.filter(client_id__id=client_id)#now filtering fields related to client id gotten from fetch api
    return JsonResponse(list(fields.values("id", "field_name")),safe=False)

def addjob_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        client = request.POST.get("client")
        field = request.POST.get("field_id")
        pvt_number = request.POST.get("pvt_number")
        clientrep = request.POST.get("clientrep")

        if request.POST.get('mails', False):
            clientrepmail = request.POST.get("mails")
        else:
             clientrepmail = None

        if request.POST.get('status', False):
            jobstatus = request.POST.get("status")
        else:
            jobstatus = JobStatus.objects.get(id=1).id

        if request.POST.get('status1', False):
            jobstatus1 = request.POST.get("status1")
        else:
            jobstatus1 = JobStatus.objects.get(id=1).id

        if request.POST.get('status2', False):
            jobstatus2 = request.POST.get("status2")
        else:
            jobstatus2 = JobStatus.objects.get(id=1).id

        if request.POST.get('status3', False):
            jobstatus3 = request.POST.get("status3")
        else:
            jobstatus3 = JobStatus.objects.get(id=1).id

        if request.POST.get('status4', False):
            jobstatus4 = request.POST.get("status4")
        else:
            jobstatus4 = JobStatus.objects.get(id=1).id

        laser_rep = request.POST.get("laser_rep")

        jobkey = request.POST.get("jobkey")

        file_title = request.POST.get("file_title")
        file_title2 = request.POST.get("file_title2")
        file_title3 = request.POST.get("file_title3")
        file_title4 = request.POST.get("file_title4")
        file_title5 = request.POST.get("file_title5")
        file_title6 = request.POST.get("file_title6")
        file_title7 = request.POST.get("file_title7")
        file_title8 = request.POST.get("file_title8")
        file_title9 = request.POST.get("file_title9")
        file_title10 = request.POST.get("file_title10")

        #jobfile = request.FILES['jobfile']
        if request.FILES.get('jobfile', False):
            jobfile = request.FILES.get("jobfile")
        else:
            jobfile = None
        if request.FILES.get('jobfile2', False):
            jobfile2 = request.FILES.get("jobfile2")
        else:
            jobfile2 = None
        if request.FILES.get('jobfile3', False):
            jobfile3 = request.FILES.get("jobfile3")
        else:
            jobfile3 = None
        if request.FILES.get('jobfile4', False):
            jobfile4 = request.FILES.get("jobfile4")
        else:
            jobfile4 = None
        if request.FILES.get('jobfile5', False):
            jobfile5 = request.FILES.get("jobfile5")
        else:
            jobfile5 = None
        if request.FILES.get('jobfile6', False):
            jobfile6 = request.FILES.get("jobfile6")
        else:
            jobfile6 = None
        if request.FILES.get('jobfile7', False):
            jobfile7 = request.FILES.get("jobfile7")
        else:
            jobfile7 = None
        if request.FILES.get('jobfile8', False):
            jobfile8 = request.FILES.get("jobfile8")
        else:
            jobfile8 = None
        if request.FILES.get('jobfile9', False):
            jobfile9 = request.FILES.get("jobfile9")
        else:
            jobfile9 = None
        if request.FILES.get('jobfile10', False):
            jobfile10 = request.FILES.get("jobfile10")
        else:
            jobfile10 = None
        print(clientrepmail)
        import shlex
        client_mails=clientrepmail
        print(client_mails)
        complete = request.POST.get("complete")
        anyotherid= request.POST.get("anyotherid")
        progressreport = request.POST.get("progressreport")
        
        client_id = CustomUser.objects.get(id=client)
        field_id = Fields.objects.get(id=field)
        jobstatus_id = JobStatus.objects.get(id=jobstatus)
        jobstatus_id1 = JobStatus.objects.get(id=jobstatus1)
        jobstatus_id2 = JobStatus.objects.get(id=jobstatus2)
        jobstatus_id3 = JobStatus.objects.get(id=jobstatus3)
        jobstatus_id4 = JobStatus.objects.get(id=jobstatus4)
        laser_rep_id = LaserRep.objects.get(id=laser_rep)
        clientemail = CustomUser.objects.get(id=client).email
        clientname = CustomUser.objects.get(id=client).username
        print(clientname)
        clientpassword = CustomUser.objects.get(id=client).password
        passwordsent = CustomUser.objects.get(id=client).sentpassword
        try:
            job_model = Dataset(pvt_number=pvt_number, clientrep=clientrep, jobkey=jobkey, anyotherid=anyotherid,
                                pdf=jobfile, pdf2=jobfile2, pdf3=jobfile3, pdf4=jobfile4, pdf5=jobfile5, pdf6=jobfile6,
                                pdf7=jobfile7, pdf8=jobfile8, pdf9=jobfile9, pdf10=jobfile10, client_id=client_id,
                                field_id=field_id, jobstatus=jobstatus_id, laserrep_id=laser_rep_id, completed=complete,
                                progressreport=progressreport, file_title=file_title,
                                file_title2=file_title2, file_title3=file_title3, file_title4=file_title4,
                                file_title5=file_title5, file_title6=file_title6,
                                file_title7=file_title7, file_title8=file_title8, file_title9=file_title9,
                                file_title10=file_title10, jobstatus1=jobstatus_id1,
                                jobstatus2=jobstatus_id2, jobstatus3=jobstatus_id3, jobstatus4=jobstatus_id4,
                                clientrep_email=clientrepmail,)
            job_model.save()
            try:
                context = {"pvt_number": pvt_number, "jobkey": jobkey, "clientrep": clientrep,
                           "jobstatus_id": jobstatus_id, "clientemail": clientemail, "passwordsent": passwordsent,
                           "file_title": file_title, "file_title2": file_title2, "file_title3": file_title3,
                           "file_title4": file_title4,
                           "file_title5": file_title5, "file_title6": file_title6, "file_title7": file_title7,
                           "file_title8": file_title8, "file_title9": file_title9, "file_title10": file_title10,
                           "clientname": clientname, }
                mail_temp = "admin_templates/email_template.html"
                mail_msg = render_to_string(mail_temp, context=context)
                mail_from = "labinfo@laser-ng.com"
                subject = "Laser Engineering posted a Report to you"
                mail = EmailMessage(subject, mail_msg, mail_from, [p for p in client_mails.split(",") if len(p) > 0])
                print(client_mails)
                mail.content_subtype = 'html'
                mail.send()
            except:
                messages.error(request, "Make sure your internet is connected")
                return HttpResponseRedirect(reverse("addjob"))
            messages.success(request, "Job added successfully")
            return HttpResponseRedirect(reverse("managejob"))
        except:
            messages.error(request, "Job add Failed, Make sure to all fields")
            return HttpResponseRedirect(reverse("addjob"))

def managejob(request):
    Active = Dataset.objects.filter(completed="Active").order_by("-id")
    Complete = Dataset.objects.filter(completed="Complete").order_by("-id")
    jobs = Dataset.objects.all().order_by("-id")
    jc = jobs.count()
    oc = Active.count()
    cc = Complete.count()

    return render(request, "admin_templates/managejob.html", {"jc":jc,"oc": oc,"cc":cc,"jobs": jobs,})

def editjob(request, job_id):
    clients = CustomUser.objects.filter(user_type=2)
    statuses = JobStatus.objects.all()
    laserreps = LaserRep.objects.all()
    jobs= Dataset.objects.get(id=job_id)
    fields = Fields.objects.all()
    return render(request, "admin_templates/editjob.html", {"fields": fields,"jobs": jobs, "id":job_id,"clients":clients,"statuses":statuses,"laserreps":laserreps})

def getfieldsedit(request):
    client = json.loads(request.body)#here we get the body from our fetch api that was already converted to string  with json.stringify
    client_id=client["id"]#'id' key of data passed to backend from id:clientval in our fetch api
    fields=Fields.objects.filter(client_id__id=client_id)#now filtering fields related to client id gotten from fetch api
    return JsonResponse(list(fields.values("id", "field_name")),safe=False)


def editjob_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        job_id = request.POST.get("job_id")
        slug= request.POST.get("slug")
        if job_id == None:
            return HttpResponseRedirect(reverse("managejob"))
        if request.POST.get('client', False):
            client = request.POST.get("client")
        else:
            client = Dataset.objects.get(id=job_id).client_id
        if request.POST.get('field_id', False):
            field = request.POST.get("field_id")
        else:
            field = Dataset.objects.get(id=job_id).field_id.id
        pvt_number = request.POST.get("pvt_number")
        clientrep = request.POST.get("clientrep")
        
        if request.POST.get('mails', False):
            clientrepmail = request.POST.get("mails")
        else:
            clientrepmail = Dataset.objects.get(id=job_id).clientrep_email

        client_mails = clientrepmail
        jobstatus = request.POST.get("status")
        jobstatus1 = request.POST.get("status1")
        jobstatus2 = request.POST.get("status2")
        jobstatus3 = request.POST.get("status3")
        jobstatus4 = request.POST.get("status4")
        laser_rep = request.POST.get("laser_rep")
        jobkey = request.POST.get("jobkey")
        if request.POST.get('complete',False):
            complete = request.POST.get("complete")
        else:
            complete = Dataset.objects.get(id=job_id).completed

        anyotherid = request.POST.get("anyotherid")
        progressreport = request.POST.get("progressreport")

        file_title = request.POST.get("file_title")
        file_title2 = request.POST.get("file_title2")
        file_title3 = request.POST.get("file_title3")
        file_title4 = request.POST.get("file_title4")
        file_title5 = request.POST.get("file_title5")
        file_title6 = request.POST.get("file_title6")
        file_title7 = request.POST.get("file_title7")
        file_title8 = request.POST.get("file_title8")
        file_title9 = request.POST.get("file_title9")
        file_title10 = request.POST.get("file_title10")

        if request.FILES.get('jobfile', False):
            jobfile = request.FILES['jobfile']
        else:
            jobfile = Dataset.objects.get(id=job_id).pdf  # AND IF NO NEW FILE IS SELECTED DO NONE
            
        if request.FILES.get('jobfile2', False):
            jobfile2 = request.FILES['jobfile2']
        else:
            jobfile2 = Dataset.objects.get(id=job_id).pdf2
            
        if request.FILES.get('jobfile3', False):
            jobfile3 = request.FILES['jobfile3']
        else:
            jobfile3 = Dataset.objects.get(id=job_id).pdf3
        
        if request.FILES.get('jobfile4', False):
            jobfile4 = request.FILES['jobfile4']
        else:
            jobfile4 = Dataset.objects.get(id=job_id).pdf4
            
        if request.FILES.get('jobfile5', False):
            jobfile5 = request.FILES['jobfile5']
        else:
            jobfile5 = Dataset.objects.get(id=job_id).pdf5

        if request.FILES.get('jobfile6', False):
            jobfile6 = request.FILES['jobfile6']
        else:
            jobfile6 = Dataset.objects.get(id=job_id).pdf6
            
        if request.FILES.get('jobfile7', False):
            jobfile7 = request.FILES['jobfile7']
        else:
            jobfile7 = Dataset.objects.get(id=job_id).pdf7
            
        if request.FILES.get('jobfile8', False):
            jobfile8 = request.FILES['jobfile8']
        else:
            jobfile8 = Dataset.objects.get(id=job_id).pdf8
            
        if request.FILES.get('jobfile9', False):
            jobfile9 = request.FILES['jobfile9']
        else:
            jobfile9 = Dataset.objects.get(id=job_id).pdf9
            
        if request.FILES.get('jobfile10', False):
            jobfile10 = request.FILES['jobfile10']
        else:
            jobfile10 = Dataset.objects.get(id=job_id).pdf10
            
        client_id = CustomUser.objects.get(id=client)
        field_id = Fields.objects.get(id=field)
        jobstatus_id = JobStatus.objects.get(id=jobstatus)
        jobstatus_id1 = JobStatus.objects.get(id=jobstatus1)
        jobstatus_id2 = JobStatus.objects.get(id=jobstatus2)
        jobstatus_id3 = JobStatus.objects.get(id=jobstatus3)
        jobstatus_id4 = JobStatus.objects.get(id=jobstatus4)
        laser_rep_id = LaserRep.objects.get(id=laser_rep)
        clientname = CustomUser.objects.get(id=client).username
        passwordsent = CustomUser.objects.get(id=client).sentpassword
        print(clientname)
        try:
            job_model = Dataset.objects.get(id=job_id)
            job_model.pvt_number = pvt_number
            job_model.slug=slug
            job_model.clientrep = clientrep
            job_model.clientrep_email = client_mails
            job_model.jobkey = jobkey
            job_model.pdf = jobfile
            job_model.pdf2 = jobfile2
            job_model.pdf3 = jobfile3
            job_model.pdf4 = jobfile4
            job_model.pdf5 = jobfile5
            job_model.pdf6 = jobfile6
            job_model.pdf7 = jobfile7
            job_model.pdf8 = jobfile8
            job_model.pdf9 = jobfile9
            job_model.pdf10 = jobfile10
            job_model.client_id = client_id
            job_model.field_id = field_id
            job_model.jobstatus = jobstatus_id
            job_model.jobstatus1 = jobstatus_id1
            job_model.jobstatus2 = jobstatus_id2
            job_model.jobstatus3 = jobstatus_id3
            job_model.jobstatus4 = jobstatus_id4
            job_model.laserrep_id = laser_rep_id
            job_model.completed = complete
            job_model.file_title=file_title
            job_model.file_title2=file_title2
            job_model.file_title3=file_title3
            job_model.file_title4=file_title4
            job_model.file_title5=file_title5
            job_model.file_title6=file_title6
            job_model.file_title7=file_title7
            job_model.file_title8=file_title8
            job_model.file_title9=file_title9
            job_model.file_title10=file_title10
            job_model.progressreport=progressreport
            job_model.anyotherid=anyotherid
            job_model.save()
            try:
                context = {"pvt_number": pvt_number, "jobkey": jobkey, "clientrep": clientrep,
                           "jobstatus_id": jobstatus_id,
                           "passwordsent": passwordsent, "file_title": file_title,
                           "file_title2": file_title2, "file_title3": file_title3, "file_title4": file_title4,
                           "file_title5": file_title5, "file_title6": file_title6, "file_title7": file_title7,
                           "file_title8": file_title8, "file_title9": file_title9, "file_title10": file_title10,
                           "clientname": clientname, }
                mail_temp = "admin_templates/editjobemail_template.html"
                mail_msg = render_to_string(mail_temp, context=context)
                mail_from = "labinfo@laser-ng.com"
                subject = "Laser Engineering Report posted to you was updated"
                mail = EmailMessage(subject, mail_msg, mail_from, [p for p in client_mails.split(",") if len(p) > 0])
                mail.content_subtype = 'html'
                mail.send()
            except:
                messages.error(request, "Make sure your internet is connected")
                return HttpResponseRedirect(reverse("editjob", kwargs={"job_id": job_id}))
            messages.success(request, "Job edited successfully")
            return HttpResponseRedirect(reverse("managejob"))
        except:
            messages.error(request, "Job edit Failed")
            return HttpResponseRedirect(reverse("editjob", kwargs={"job_id": job_id}))

def deletejob(request):
    job_id = request.POST.get("job_id")
    if job_id == None:
        return HttpResponseRedirect(reverse("managejob"))
    try:
        jobs = Dataset.objects.get(id=job_id)
        jobs.delete()
        messages.success(request, "Job Deleted successfully")
        return HttpResponseRedirect(reverse("managejob"))
    except:
        messages.error(request, "Job Failed to delete")
        return HttpResponseRedirect(reverse("managejob"))

def viewjobinfo(request, job_id):
    jobs = Dataset.objects.get(id=job_id)
    return render(request, "admin_templates/viewjobinfo.html",{"jobs": jobs, "id": job_id})


def viewfeedback(request):
    feedback = FeedBackClient.objects.all().order_by("-id")
    return render(request, "admin_templates/viewfeedback.html",{"fb": feedback})

def viewfeedbackdetail(request,job_id):
    feedback = FeedBackClient.objects.get(id = job_id)
    return render(request, "admin_templates/viewfeedbackdetail.html", {"fb": feedback, "id": job_id})

def completedjobs(request):
    Active = Dataset.objects.filter(completed="Active").order_by("-id")
    Complete = Dataset.objects.filter(completed="Complete").order_by("-id")
    jobs = Dataset.objects.all().order_by("-id")
    jc=jobs.count()
    oc=Active.count()
    cc=Complete.count()
    return render(request, "admin_templates/completedjobs.html",{"jc":jc,"oc": oc,"cc":cc,"Complete":Complete})

def ongoingjobs(request):
    Active = Dataset.objects.filter(completed="Active").order_by("-id")
    Complete = Dataset.objects.filter(completed="Complete").order_by("-id")
    jobs = Dataset.objects.all().order_by("-id")
    jc=jobs.count()
    oc=Active.count()
    cc=Complete.count()
    return render(request, "admin_templates/ongoingjobs.html",{"jc":jc,"oc": oc,"cc":cc,"Active":Active})