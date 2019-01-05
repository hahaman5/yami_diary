from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Division(models.Model):
    division = models.CharField('분류',max_length=100,primary_key=True)
    def __str__(self):
        return self.division

class Idea(models.Model):
    auto_inc_id = models.AutoField(primary_key=True)
    subject = models.CharField('주제', max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    image = models.ImageField(null=True,upload_to='',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateField('인스타 발행일',null=True,blank=True,unique=True)
    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs={'idea_id': self.pk})
        return url

    def get_edit_url(self):
        url = reverse_lazy('edit', kwargs={'idea_id': self.pk})
        return url

    def get_div_name(self):
        return format(self.division.division)

