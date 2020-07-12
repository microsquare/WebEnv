from django.db import models

class Contactf(models.Model):
    full_name = models.CharField(max_length=191)
    emailid = models.CharField(max_length=191)
    desp = models.CharField(max_length=191)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.ordering