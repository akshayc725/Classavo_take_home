from django.db import models
from mediumeditor.widgets import MediumEditorTextarea

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return "/%s" % self.slug

    def get_edit_url(self):
        return "/post/%s/edit" % self.pk