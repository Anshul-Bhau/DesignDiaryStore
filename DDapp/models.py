from django.db import models

class Articles(models.Model):
    type_choices = [('jewellery', 'jewellery'),
                    ('potrait', 'potrait'),
                    ('crochet', 'crochet')]
    name = models.CharField('Article Name', max_length=250, blank= False, null=False)
    img = models.ImageField('Article Image', null=True, blank=True, upload_to='images/')
    type = models.CharField(choices=type_choices, max_length=100, null=False, blank=False)
    description = models.TextField('About the article', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
