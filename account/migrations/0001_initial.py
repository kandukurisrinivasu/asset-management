# Generated by Django 2.2.10 on 2021-05-12 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asset_no', models.CharField(max_length=50)),
                ('Owner', models.CharField(max_length=50)),
                ('Asset_type', models.CharField(max_length=50)),
                ('Group', models.CharField(max_length=50)),
                ('Team_name', models.CharField(max_length=50)),
                ('working_status', models.CharField(default='working', max_length=50)),
                ('Remark', models.CharField(max_length=50)),
                ('Product_line', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Setup_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Host_name', models.CharField(max_length=30)),
                ('FQDN', models.CharField(default='si-z0z15.st.de.bosch.com', max_length=20)),
                ('OS', models.CharField(max_length=20)),
                ('COM_port_details', models.CharField(max_length=50)),
                ('Other_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group', models.CharField(default='EBB', max_length=30)),
                ('Team_name', models.CharField(default='EBB', max_length=30)),
                ('Location', models.CharField(default='BAN', max_length=30)),
                ('Phone', models.CharField(default='0000000000', max_length=30)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lab_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Setup_name', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=200, unique=True)),
                ('Description', models.TextField()),
                ('Start_date', models.DateTimeField(blank=True)),
                ('End_date', models.DateTimeField(blank=True)),
                ('Start_time', models.TimeField(blank=True)),
                ('End_time', models.TimeField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Lab_event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('event', 'user')},
            },
        ),
    ]
