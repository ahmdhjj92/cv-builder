# Generated by Django 3.2.6 on 2021-11-07 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv_builder_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Certification',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='responsabilities',
        ),
        migrations.DeleteModel(
            name='Responsability',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]
