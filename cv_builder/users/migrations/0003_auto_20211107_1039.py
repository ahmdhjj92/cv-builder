# Generated by Django 3.2.6 on 2021-11-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211107_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvbuser',
            name='address',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cvbuser',
            name='phone_number',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cvbuser',
            name='professional_summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]