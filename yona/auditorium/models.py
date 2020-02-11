from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.
class GitHubEye(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    prj_title = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)

    objects = models.Manager()

    class Meta:
        ordering = ['created']
