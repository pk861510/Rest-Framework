from django.db import models

# Create your models here.
class NavbarContent(models.Model):
    name = models.CharField(max_length = 100)
    url = models.URLField()

    def __str__(self):
        return self.name

class OurClient(models.Model):
    pic_link = models.URLField()
    official_website = models.URLField()

    def __str__(self):
        return self.official_website

class ClientTestimonials(models.Model):
    pic_link = models.URLField()
    post = models.TextField()
    organization_name = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.organization_name

class  ManagementTeam(models.Model):
    pic_link = models.URLField()
    name = models.CharField(max_length = 100)
    post = models.CharField(max_length = 150)
    linkedin_profile = models.URLField()

    def __str__(self):
        return self.name

class DeveloperTeam(models.Model):
    pic_link = models.URLField()
    name = models.CharField(max_length = 100)
    post = models.CharField(max_length = 150)
    linkedin_profile = models.URLField()

    def __str__(self):
        return self.name