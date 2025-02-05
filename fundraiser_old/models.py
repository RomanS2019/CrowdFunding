from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _


# validators
from django.core.validators import FileExtensionValidator

# django signal
from django.db.models.signals import post_save
from django.dispatch import receiver

# datetime
from datetime import datetime, timedelta


# choices
from fundraiser.choices import *


# random
import string
import random

#---------------- import models ------------------#
from django.db.models import Sum
from django.db.models import Q
from django.db.models import FloatField


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'Admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):

    username = None
    name = models.CharField(_('name'), max_length=250, null=True)
    email = models.EmailField(_('email'), unique=True)
    is_indian = models.BooleanField(default=True)
    mobile_no = models.CharField(max_length=20, null=True, unique=True)
    address = models.CharField(max_length=250, null=True)
    pincode = models.CharField(max_length=25, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    email_confirm = models.BooleanField(default=False)
    mobile_confirm = models.BooleanField(default=False)
    i_agree = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=User_Type, default="End User")
    profile = models.ImageField(upload_to='profile', default='profile/avtar.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    objects = UserManager()

    def __str__(self):
        return "%s" %(self.name)


    def save(self, *args, **kwargs):
        
        if not self.name:
            if self.first_name and self.last_name:
                self.name = "%s %s" %(self.first_name, self.last_name)

            elif self.first_name:
                self.name = self.first_name

            elif self.last_name:
                self.name = name + self.last_name

        return super(User, self).save(*args, **kwargs)


class UserUniqueToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_token = models.CharField(max_length=30)

    def __str__(self):
        return "%s" %(self.user.name)


class Beneficiary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    mobile_no = models.CharField(max_length=100, null=True)
    bank_account = models.CharField(max_length=100, null=True)
    account_holder = models.CharField(max_length=100, null=True)
    ifsc = models.CharField(max_length=50, null=True)
    primary_address = models.CharField(max_length=250, null=True)
    secondry_address = models.CharField(max_length=350, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    pan_card_no = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "%s" %(self.email)


class GenericEmails(models.Model):
    name = models.CharField(max_length=50)
    departments = models.CharField(max_length=50, choices=generic_emails_departments)
    email = models.EmailField()
    role = models.CharField(max_length=50, choices=generic_emails_role)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



#---------------------- Media ----------------------#

class MediaArtical(models.Model):
    title = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='MediaArtical')
    created_at = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField(max_length=100)
    link = models.URLField(null=True)
    short_text = models.TextField()

    def __str__(self):
        return self.title


class CrowdNewsing(models.Model):
    profile = models.ImageField(upload_to='CrowdNewsing')
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    about_crowd_newsing = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ServicesEnquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactUS(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name

#---------------------- Media ----------------------#


#---------------------- Campaign ----------------------#

class CampaignCategory(models.Model):
    category = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category


class CauseCategory(models.Model):
    cause = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cause


class CampaignFundRaiser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(CampaignCategory, on_delete=models.CASCADE, null=True)
    goal = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    short_description = models.CharField(max_length=250)
    about = models.TextField()
    picture = models.ImageField(upload_to='CampaignFundRaiser')
    cause = models.ForeignKey(CauseCategory, on_delete=models.SET_NULL, null=True)
    sensitivity = models.CharField(max_length=40, choices=sensitivity_choices)
    commission = models.FloatField(default=2.0)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True, editable=False)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            today = datetime.now().date()
            self.end_date = today + timedelta(days=self.day)

        return super(CampaignFundRaiser, self).save(*args, **kwargs)

    def available_days(self):
        today = datetime.now().date()
        return (self.end_date - today).days

    def totalfund_in_percentage(self):
        goal = self.goal
        fund = self.campaigntotalamount.total_amount
        return int((100 * fund)/goal)

    def available_withdrawl_fund(self):
        total_fund = self.campaigntotalamount.total_amount
        commission = self.commission
        total_withdrawl = WithdrawalRequest.objects.filter(campaign__id=self.id, status='Approved').aggregate(Sum('amount'))['amount__sum']
        try:
            total_withdrawl = float(total_withdrawl)
        except:
            total_withdrawl = 0

        available_amount = (total_fund -(( total_fund * commission )/100)) - total_withdrawl
        return available_amount

    def total_withdrawl_fund(self):
        total_withdrawl = WithdrawalRequest.objects.filter(campaign__id=self.id, status='Approved').aggregate(Sum('amount'))['amount__sum']
        try:
            total_withdrawl = float(total_withdrawl)
        except:
            total_withdrawl = 0
        return total_withdrawl

    def commission_in_rs(self):
        total_fund = self.campaigntotalamount.total_amount
        commission = self.commission
        return ( total_fund * commission )/100

class CampaignDoners(models.Model):
    campaign_fund_raiser = models.ForeignKey(CampaignFundRaiser, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField()
    doner_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    pincode = models.CharField(max_length=20)
    facbook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    indian_citizen = models.BooleanField(default=True)
    is_hide_me = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, choices=Payment_Status, default='created')
    refund_status = models.CharField(max_length=20, choices=Refund_Status, default='not requested')
    payment_id = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_request_refund = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def amount_in_paisa(self):
        return (self.amount * 100)

    def short_name(self):
        if self.is_hide_me:
            return "A"
        else:
            short_name = ""
            short_name_list = (self.name).split()
            for i in short_name_list:
                try:
                    short_name += i[0]
                except:
                    pass
            return short_name.upper()

class CampaignTotalAmount(models.Model):
    campaign_fund_raiser = models.OneToOneField(CampaignFundRaiser, on_delete=models.CASCADE, null=True)
    total_amount = models.PositiveIntegerField()
    total_supporters = models.PositiveIntegerField()

    def __str__(self):
        return self.campaign_fund_raiser.title


class WithdrawalRequest(models.Model):
    campaign = models.ForeignKey(CampaignFundRaiser, on_delete=models.CASCADE)
    amount = models.FloatField()
    document = models.FileField(upload_to='WithdrawalRequest')
    summary = models.CharField(max_length=250)
    status = models.CharField(max_length=40, default='New', choices=Withdrawal_Status)
    payment_date = models.DateField(null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign.title



class CampaignComments(models.Model):
    campaign_fund_raiser = models.ForeignKey(CampaignFundRaiser, on_delete=models.CASCADE, null=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign_fund_raiser.title

    def created_date(self):
        return (self.created_at).date()

        


class CampaignEnqiry(models.Model):
    campaign_fund_raiser = models.ForeignKey(CampaignFundRaiser, on_delete=models.CASCADE, null=True)
    enqiry_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    
    def __str__(self):
        return self.campaign_fund_raiser.title

class CampaignUpdates(models.Model):
    campaign_fund_raiser = models.ForeignKey(CampaignFundRaiser, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=250)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign_fund_raiser.title


class CampaignBuzz(models.Model):
    campaign_fund_raiser = models.ForeignKey(CampaignFundRaiser, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=250)
    buzz = models.TextField()
    article_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='CampaignBuzz')
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.campaign_fund_raiser.title


#---------------------- Campaign ----------------------#


#---------------------- Support Group ----------------------#


class SupportGroup(models.Model):
    group_leader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, unique=True)
    goal = models.PositiveIntegerField()
    short_description = models.CharField(max_length=250)
    about = models.TextField()
    picture = models.ImageField(upload_to='SupportGroup')
    cause = models.ForeignKey(CauseCategory, on_delete=models.SET_NULL, null=True)
    sensitivity = models.CharField(max_length=40, choices=sensitivity_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def group_member_count(self):
        return SupportGroupMembers.objects.filter(support_group__id=self.id).count()

    def group_member_percentage(self):
        join_member = SupportGroupMembers.objects.filter(support_group__id=self.id).count()
        total_member = self.goal
        return int((100 * join_member)/total_member)



class SupportGroupMembers(models.Model):
    support_group = models.ForeignKey(SupportGroup, on_delete=models.CASCADE, null=True)
    group_member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    pincode = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    facbook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    is_share = models.BooleanField(default=True)
    is_show_name = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.support_group.title

    def joining_date(self):
        return (self.created_at).date()

    def short_name(self):
        if self.is_show_name:
            short_name = ""
            short_name_list = (self.name).split()
            for i in short_name_list:
                try:
                    short_name += i[0]
                except:
                    pass
            return short_name.upper()
        else:
            return "A"


class SupportComments(models.Model):
    support_group = models.ForeignKey(SupportGroup, on_delete=models.CASCADE, null=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.support_group.title

    def created_date(self):
        return (self.created_at).date()


class SupportEnqiry(models.Model):
    support_group = models.ForeignKey(SupportGroup, on_delete=models.CASCADE, null=True)
    enqiry_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    
    def __str__(self):
        return self.support_group.title

class SupportUpdates(models.Model):
    support_group = models.ForeignKey(SupportGroup, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=250)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.support_group.title


class SupportBuzz(models.Model):
    support_group = models.ForeignKey(SupportGroup, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=250)
    buzz = models.TextField()
    article_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='SupportBuzz')
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.support_group.title

#---------------------- Support Group ----------------------#


#---------------------- Event ----------------------#
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250, unique=True)
    about = models.TextField()
    place = models.CharField(max_length=250)
    date = models.DateTimeField()
    ticket = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='Event')
    cause = models.ForeignKey(CauseCategory, on_delete=models.SET_NULL, null=True)
    sensitivity = models.CharField(max_length=40, choices=sensitivity_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def group_member_count(self):
        return EventGroupMembers.objects.filter(event__id=self.id).count()


class EventGroupMembers(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    group_member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    pincode = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    facbook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    is_share = models.BooleanField(default=True)
    is_show_name = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.name

    def joining_date(self):
        return (self.created_at).date()

    def short_name(self):
        if self.is_show_name:
            short_name = ""
            short_name_list = (self.name).split()
            for i in short_name_list:
                try:
                    short_name += i[0]
                except:
                    pass
            return short_name.upper()
        else:
            return "A"


class EventComments(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.name


    def created_date(self):
        return (self.created_at).date()


class EventEnqiry(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    enqiry_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    
    def __str__(self):
        return self.event.name

class EventUpdates(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=250)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.name


class EventBuzz(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=250)
    buzz = models.TextField()
    article_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='EventBuzz')
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.event.name
#---------------------- Event ----------------------#



#--------------------- signal --------------------------------------#
@receiver(post_save,sender=CampaignFundRaiser)
def create_campaign_total_amount(sender,**kwargs):
    if kwargs['created']:
        instance_CampaignFundRaiser = kwargs['instance']

        CampaignTotalAmount.objects.create(campaign_fund_raiser=instance_CampaignFundRaiser, total_amount=0, total_supporters=0)


@receiver(post_save,sender=User)
def create_Beneficiary(sender,**kwargs):
    if kwargs['created']:
        instance_user = kwargs['instance']

        Beneficiary.objects.create(user=instance_user)

        User_Unique_Token_save = True
        while User_Unique_Token_save:
            try:
                lettersAndDigits = string.ascii_letters + string.digits
                Unique_Token = ''.join(random.choice(lettersAndDigits) for i in range(12))

                UserUniqueToken.objects.create(user=instance_user, unique_token=Unique_Token)
                User_Unique_Token_save = False
            except:
                pass













