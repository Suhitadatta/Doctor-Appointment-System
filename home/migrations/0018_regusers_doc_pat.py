# Generated by Django 4.1 on 2022-12-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_patient_user_alter_nearby_doctor_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='regusers',
            name='Doc_pat',
            field=models.CharField(default=' ', max_length=122),
            preserve_default=False,
        ),
    ]
