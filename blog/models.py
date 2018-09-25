from django.db import models

class blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()
    
    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title

class rating(models.Model):
    image = models.ImageField(upload_to='images/ratings')
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title

class review(models.Model):
    image = models.ImageField(upload_to='images/reviews')
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title

class blogposts(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()
    
    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title