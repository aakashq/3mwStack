from django.db import models

# Create your models here.


class sitemodel(models.Model):
    name=models.CharField(max_length=20)
    ts=models.DateTimeField(auto_now_add=True)
    uts=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('ts',)

    def __str__(self):
        return u'%s' % self.id


class valuesmodel(models.Model):
    a=models.DecimalField(max_digits=5,decimal_places=2)
    b=models.DecimalField(max_digits=5,decimal_places=2)
    site=models.ForeignKey(sitemodel,on_delete=models.CASCADE)
    ts = models.DateTimeField(auto_now_add=True)
    uts = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('ts',)

    def __str__(self):
        return u'%s' % self.id