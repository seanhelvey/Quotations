from django.db import models

class Author(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200, blank=False, default='')
    last_name = models.CharField(max_length=200, blank=True, default='')    
 
    class Meta:
        ordering = ('created',)        

class Quote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500, blank=False, default='')
    author = models.ForeignKey(Author)
 
    class Meta:
        ordering = ('created',)

class Subject(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False, default='')    
    quotes = models.ManyToManyField(Quote)

    class Meta:
        ordering = ('created',)                
