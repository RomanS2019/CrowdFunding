# Generated by Django 2.0.4 on 2019-07-25 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import fundraiser.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('is_indian', models.BooleanField(default=True)),
                ('mobile_no', models.CharField(max_length=20, null=True, unique=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('pincode', models.CharField(max_length=25, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('email_confirm', models.BooleanField(default=False)),
                ('mobile_confirm', models.BooleanField(default=False)),
                ('i_agree', models.BooleanField(default=True)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Backend User', 'Backend User'), ('End User', 'End User')], default='End User', max_length=20)),
                ('profile', models.ImageField(default='profile/avtar.png', upload_to='profile')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', fundraiser.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile_no', models.CharField(max_length=100, null=True)),
                ('bank_account', models.CharField(max_length=100, null=True)),
                ('account_holder', models.CharField(max_length=100, null=True)),
                ('ifsc', models.CharField(max_length=50, null=True)),
                ('primary_address', models.CharField(max_length=250, null=True)),
                ('secondry_address', models.CharField(blank=True, max_length=350, null=True)),
                ('pincode', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('pan_card_no', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignBuzz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('buzz', models.TextField()),
                ('article_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(upload_to='CampaignBuzz')),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignDoners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('pincode', models.CharField(max_length=20)),
                ('facbook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('indian_citizen', models.BooleanField(default=True)),
                ('is_hide_me', models.BooleanField(default=False)),
                ('payment_status', models.CharField(choices=[('created', 'created'), ('captured', 'captured'), ('failed', 'failed'), ('refund', 'refund')], default='created', max_length=20)),
                ('refund_status', models.CharField(choices=[('not requested', 'not requested'), ('request refund', 'request refund'), ('refund approved', 'refund approved'), ('refund decline', 'refund decline')], default='not requested', max_length=20)),
                ('payment_id', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_request_refund', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignEnqiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignFundRaiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('goal', models.PositiveIntegerField()),
                ('day', models.PositiveIntegerField()),
                ('short_description', models.CharField(max_length=250)),
                ('about', models.TextField()),
                ('picture', models.ImageField(upload_to='CampaignFundRaiser')),
                ('sensitivity', models.CharField(choices=[('high sensitive', 'high sensitive'), ('moderate', 'moderate'), ('charity', 'charity')], max_length=40)),
                ('commission', models.FloatField(default=2.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, editable=False, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.CampaignCategory')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignTotalAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.PositiveIntegerField()),
                ('total_supporters', models.PositiveIntegerField()),
                ('campaign_fund_raiser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.CampaignFundRaiser')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignUpdates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('about', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('campaign_fund_raiser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.CampaignFundRaiser')),
            ],
        ),
        migrations.CreateModel(
            name='CauseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CrowdNewsing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='CrowdNewsing')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('about_crowd_newsing', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('about', models.TextField()),
                ('place', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('ticket', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='Event')),
                ('sensitivity', models.CharField(choices=[('high sensitive', 'high sensitive'), ('moderate', 'moderate'), ('charity', 'charity')], max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('cause', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fundraiser.CauseCategory')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventBuzz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('buzz', models.TextField()),
                ('article_link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(upload_to='EventBuzz')),
                ('publisher', models.CharField(max_length=100)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventEnqiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=20)),
                ('enqiry_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventGroupMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('facbook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('is_share', models.BooleanField(default=True)),
                ('is_show_name', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.Event')),
                ('group_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventUpdates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('about', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.Event')),
            ],
        ),
        migrations.CreateModel(
            name='GenericEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('departments', models.CharField(choices=[('Defence', 'Defence'), ('Home Affairs', 'Home Affairs'), ('Chemicals', 'Chemicals')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('Minister of Defence', 'Minister of Defence'), ('Minister of Home Affairs', 'Minister of Home Affairs'), ('Minister of Chemicals', 'Minister of Chemicals')], max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaArtical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='MediaArtical')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publisher', models.CharField(max_length=100)),
                ('link', models.URLField(null=True)),
                ('short_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicesEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SupportBuzz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('buzz', models.TextField()),
                ('article_link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(upload_to='SupportBuzz')),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SupportComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupportEnqiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=20)),
                ('enqiry_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupportGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('goal', models.PositiveIntegerField()),
                ('short_description', models.CharField(max_length=250)),
                ('about', models.TextField()),
                ('picture', models.ImageField(upload_to='SupportGroup')),
                ('sensitivity', models.CharField(choices=[('high sensitive', 'high sensitive'), ('moderate', 'moderate'), ('charity', 'charity')], max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('cause', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fundraiser.CauseCategory')),
                ('group_leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupportGroupMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('facbook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('is_share', models.BooleanField(default=True)),
                ('is_show_name', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('group_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('support_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.SupportGroup')),
            ],
        ),
        migrations.CreateModel(
            name='SupportUpdates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('about', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('support_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.SupportGroup')),
            ],
        ),
        migrations.CreateModel(
            name='UserUniqueToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_token', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('document', models.FileField(upload_to='WithdrawalRequest')),
                ('summary', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('New', 'New'), ('Approved', 'Approved'), ('Decline', 'Decline')], default='New', max_length=40)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraiser.CampaignFundRaiser')),
            ],
        ),
        migrations.AddField(
            model_name='supportenqiry',
            name='support_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.SupportGroup'),
        ),
        migrations.AddField(
            model_name='supportcomments',
            name='support_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.SupportGroup'),
        ),
        migrations.AddField(
            model_name='supportbuzz',
            name='support_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.SupportGroup'),
        ),
        migrations.AddField(
            model_name='campaignfundraiser',
            name='cause',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fundraiser.CauseCategory'),
        ),
        migrations.AddField(
            model_name='campaignfundraiser',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='campaignenqiry',
            name='campaign_fund_raiser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.CampaignFundRaiser'),
        ),
        migrations.AddField(
            model_name='campaignenqiry',
            name='enqiry_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='campaigndoners',
            name='campaign_fund_raiser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.CampaignFundRaiser'),
        ),
        migrations.AddField(
            model_name='campaigndoners',
            name='doner_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='campaigncomments',
            name='campaign_fund_raiser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.CampaignFundRaiser'),
        ),
        migrations.AddField(
            model_name='campaigncomments',
            name='comment_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='campaignbuzz',
            name='campaign_fund_raiser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.CampaignFundRaiser'),
        ),
    ]