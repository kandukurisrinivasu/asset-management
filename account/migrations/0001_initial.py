# Generated by Django 3.1.7 on 2021-04-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assetOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sID', models.IntegerField()),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Mob', models.IntegerField()),
                ('age', models.IntegerField()),
                ('upload_photo', models.FileField(upload_to='')),
                ('group', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'AssetMember',
            },
        ),
    ]
