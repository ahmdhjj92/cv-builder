# Generated by Django 3.2.5 on 2021-08-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('issued_by', models.CharField(max_length=100)),
                ('date_issued', models.DateField()),
                ('additional_info', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('phone_number', models.SlugField(max_length=100)),
                ('address', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=200)),
                ('starting_date', models.DateField()),
                ('end_date_or_projected_date', models.DateField()),
                ('gpa_or_grade', models.SlugField(blank=True, max_length=100)),
                ('additional_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('proficiency', models.CharField(choices=[('limited', 'Limited Professional Proficiency'), ('intermediate', 'Intermediate Professional Proficiency'), ('full', 'Full Professional Proficiency'), ('native', 'Mother Tongue')], max_length=100)),
                ('proof', models.TextField(blank=True)),
                ('score', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('label', models.CharField(blank=True, max_length=100)),
                ('starting_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('project_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Responsability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsability', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=200)),
                ('address', models.SlugField(max_length=200)),
                ('starting_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('current_position', models.BooleanField()),
                ('responsabilities', models.ManyToManyField(related_name='responsablities', to='cv_builder_app.Responsability')),
            ],
        ),
    ]