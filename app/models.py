from django.db import models


# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)
    yoe = models.IntegerField()

    def __str__(self):
        return self.name


class Job(models.Model):
    EMPLOYMENT_TYPE = [("FULL-TIME", "FULL TIME"),
                       ("PART-TIME", "PART TIME"),
                       ("SELF-EMPLOYED", "SELF-EMPLOYED"),
                       ("FREELANCE", "FREELANCE")]

    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    url_company = models.URLField(max_length=200, null=True)
    project = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50)
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE, max_length=70)
    image = models.ImageField(upload_to='images/', null=True)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title


class Certification(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    issuing_organization = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    finish_date = models.DateTimeField()
    url = models.URLField(max_length=200)
    certification_id = models.CharField(max_length=50)
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/')
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name
