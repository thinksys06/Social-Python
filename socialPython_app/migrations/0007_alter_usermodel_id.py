# Generated by Django 4.0.2 on 2022-03-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialPython_app', '0006_userprofilemodel_user_alter_usermodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
