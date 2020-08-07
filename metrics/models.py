from django.db import models
from django.contrib.postgres.fields import ArrayField

class ScholarData(models.Model):
    scholarName = models.CharField(max_length=40)
    scholarImage = models.URLField(max_length=200)
    workplace = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pubCount = models.CharField(max_length=100, null=True)
    citCount = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    hIndex = models.CharField(max_length=100, null=True)
    gIndex = models.CharField(max_length=100, null=True)
    mIndex = models.CharField(max_length=100, null=True)
    oIndex = models.CharField(max_length=100, null=True)
    eIndex = models.CharField(max_length=100, null=True)
    hMedian = models.CharField(max_length=100, null=True)
    TNCc = models.CharField(max_length=100, null=True)
    sIndex = models.CharField(max_length=100, null=True)

    # Array of data
    titles = ArrayField(models.CharField(max_length=500))
    nCitations = ArrayField(models.CharField(max_length=50), null=True)
    citations = ArrayField(models.CharField(max_length=50), null=True)
    coauthors = ArrayField(models.CharField(max_length=50), null=True)
    years = ArrayField(models.CharField(max_length=100), null=True)

    def __str__(self):
        return self.scholarName
