from django.contrib.auth.models import AbstractUser
from django.db import models
import secrets
from .paystack import *
from .utils import *
from django.utils import timezone
# Create your models here.
from django.db.models.signals import post_save,pre_save ###presave for slug url function
from django.dispatch import receiver

class CustomUser(AbstractUser):
    user_type_data = ((1, "admin"), (2, "client"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    sentpassword = models.CharField(max_length=500)

class AdminLaser(models.Model):
    id=  models.AutoField(primary_key=True)
    admin= models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    objects= models.Manager()
    def __str__(self):
        return self.id

class Client(models.Model):
    id=  models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    client_name= models.CharField(max_length=500)
    sentpassword = models.CharField(max_length=500)
    address = models.TextField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    objects= models.Manager()
    def __str__(self):
        return self.client_name

class Fields(models.Model):
    id=models.AutoField(primary_key=True)
    client_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    field_name= models.CharField(max_length=255)
    objects= models.Manager()
    def __str__(self):
        return self.field_name

class LaserRep(models.Model):
    id=models.AutoField(primary_key=True)
    laserrep_name= models.CharField(max_length=255, blank=True, null=True)
    position= models.CharField(max_length=20,blank=True, null=True)
    objects= models.Manager()
    def __str__(self):
        return self.laserrep_name

class JobStatus(models.Model):
    id=models.AutoField(primary_key=True)
    jobstatus= models.CharField(max_length=255,null=True,blank=True)
    objects= models.Manager()
    def __str__(self):
        return self.jobstatus

class Dataset(models.Model):
    choices = (("Complete", "Complete"), ("Active", "Active"))
    id=  models.AutoField(primary_key=True)
    slug= models.SlugField(max_length=255,null=True,blank=True)
    client_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    field_id= models.ForeignKey(Fields,on_delete=models.CASCADE,default=1)
    pvt_number = models.CharField(max_length=255,blank=True, null=True)
    clientrep= models.CharField(max_length=255,blank=True, null=True)
    clientrep_email= models.CharField(max_length=255,null=True,blank=True)
    clientrep_email1 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email2 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email3 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email4 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email5 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email6 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email7 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email8 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email9 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email10 = models.CharField(max_length=255, null=True, blank=True)
    clientrep_email11 = models.CharField(max_length=255, null=True, blank=True)
    jobstatus = models.ForeignKey(JobStatus,on_delete=models.CASCADE,null=True,blank=True)
    jobstatus1 = models.ForeignKey(JobStatus,related_name="jobstatus_1",on_delete=models.CASCADE,blank=True)
    jobstatus2 = models.ForeignKey(JobStatus,related_name="jobstatus_2",on_delete=models.CASCADE,blank=True)
    jobstatus3 = models.ForeignKey(JobStatus,related_name="jobstatus_3",on_delete=models.CASCADE,blank=True)
    jobstatus4 = models.ForeignKey(JobStatus,related_name="jobstatus_4",on_delete=models.CASCADE,blank=True)
    laserrep_id = models.ForeignKey(LaserRep,on_delete=models.CASCADE,default=1)
    jobkey= models.CharField(max_length=255,null=True,blank=True)
    copiedemails = models.CharField(max_length=255,null=True,blank=True)
    copiedemails1 = models.CharField(max_length=255, null=True, blank=True)
    copiedemails2 = models.CharField(max_length=255, null=True, blank=True)
    copiedemails3 = models.CharField(max_length=255, null=True, blank=True)
    copiedemails4 = models.CharField(max_length=255, null=True, blank=True)
    copiedemails5 = models.CharField(max_length=255, null=True, blank=True)
    file_title = models.CharField(max_length=255,null=True,blank=True)
    file_title2 = models.CharField(max_length=255,null=True,blank=True)
    file_title3 = models.CharField(max_length=255,null=True,blank=True)
    file_title4 = models.CharField(max_length=255,null=True,blank=True)
    file_title5 = models.CharField(max_length=255,null=True,blank=True)
    file_title6 = models.CharField(max_length=255,null=True,blank=True)
    file_title7 = models.CharField(max_length=255,null=True,blank=True)
    file_title8 = models.CharField(max_length=255,null=True,blank=True)
    file_title9 = models.CharField(max_length=255,null=True,blank=True)
    file_title10 = models.CharField(max_length=255,null=True,blank=True)
    pdf = models.FileField(upload_to='raw/',blank=True,null=True)
    pdf2 = models.FileField(upload_to='raw/', blank=True, null=True)
    pdf3 = models.FileField(upload_to='raw/', blank=True, null=True)
    pdf4 = models.FileField(upload_to='raw/', blank=True, null=True)
    pdf5 = models.FileField(upload_to='raw/', blank=True, null=True)
    pdf6 = models.FileField(upload_to='raw/', blank=True, null=True)
    pdf7 = models.FileField(upload_to='raw/', blank=True, null=True)
    pdf8 = models.FileField(upload_to='raw/', blank=True, null=True)
    pdf9 = models.FileField(upload_to='raw/', blank=True, null=True)
    pdf10 = models.FileField(upload_to='raw/', blank=True, null=True)
    anyotherid=models.CharField(max_length=255,blank=True, null=True)
    progressreport= models.CharField(max_length=30000,blank=True, null=True)
    completed = models.CharField(choices=choices, max_length=8, default="Active")
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    # class Meta:
    #     ordering = ('-created_at')
    def __str__(self):
        return self.pvt_number

def slug_generator(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator, sender=Dataset)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    job_id =  models.ForeignKey(Dataset,on_delete=models.CASCADE,default=1)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    email =  models.EmailField()
    verified = models.BooleanField(default=False)
    created_at= models.DateTimeField(default=timezone.now())
    objects = models.Manager()
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.job_id

    def save(self,*args,**kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_same_ref = Payment.objects.filter(ref=ref)
            if not object_with_same_ref:
                self.ref = ref
        super().save(*args, **kwargs)
    def amount_value(self) -> int:
        return self.amount
    def verifypayment(self):
        paystack = Paystack()
        status, result = paystack.verifypayment(self.ref,self.amount)
        if status:
            if result["amount"] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False





class FeedBackClient(models.Model):

    id = models.AutoField(primary_key=True)
    pvt_number = models.CharField(max_length=255,blank=True)
    job_id = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    client = models.CharField(max_length=255)
    address = models.TextField(null=True,blank=True)
    descrition_of_service = models.TextField(null=True,blank=True)
    analysis_and_report = models.IntegerField(default=0,null=True,blank=True)
    job_schedule = models.IntegerField(default=0,null=True,blank=True)
    staff_performance = models.IntegerField(default=0,null=True,blank=True)
    job_price = models.IntegerField(default=0,null=True,blank=True)
    recommend_us = models.IntegerField(default=0,null=True,blank=True)
    complaint_response = models.IntegerField(default=0,null=True,blank=True)
    rejected_services = models.CharField(max_length=3,null=True,blank=True)
    rejected_services_comment = models.TextField(null=True,blank=True)
    comment = models.TextField(null=True,blank=True)
    laser_rep = models.CharField(max_length=255)
    client_rep = models.CharField(max_length=255)

    score=models.IntegerField()
    client_rep_designation = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now())
    objects = models.Manager()
    def __str__(self):
        return self.job_id

class NotificationClient(models.Model):
    id=  models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    objects = models.Manager()
    def __str__(self):
        return self.message




@receiver(post_save, sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminLaser.objects.create(admin=instance)
        if instance.user_type==2:
            Client.objects.create(admin=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminlaser.save()
    if instance.user_type==2:
        instance.client.save()


