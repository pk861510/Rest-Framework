# Generated by Django 5.0.3 on 2024-11-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientTestimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_link', models.URLField()),
                ('post', models.TextField()),
                ('organization_name', models.CharField(max_length=150)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_link', models.URLField()),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=150)),
                ('linkedin_profile', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ManagementTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_link', models.URLField()),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=150)),
                ('linkedin_profile', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='NavbarContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='OurClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_link', models.URLField()),
                ('official_website', models.URLField()),
            ],
        ),
    ]
