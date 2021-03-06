"""
7. The lookup API

This demonstrates features of the database API.
"""

from django.db import models, DEFAULT_DB_ALIAS, connection
from django.conf import settings

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    class Meta:
        ordering = ('-pub_date', 'headline')

    def __unicode__(self):
        return self.headline
