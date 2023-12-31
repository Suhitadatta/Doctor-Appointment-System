# Generated by Django 4.1 on 2022-12-07 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_patient_alter_nearby_doctor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.regusers'),
        ),
        migrations.AlterField(
            model_name='nearby_doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pat_image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
