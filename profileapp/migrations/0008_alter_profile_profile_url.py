# Generated by Django 4.0.2 on 2022-06-02 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0007_alter_profile_profile_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_url',
            field=models.URLField(default='http://127.0.0.1:8000/get/ppp/<django.db.models.fields.related.OneToOneField>'),
        ),
    ]
