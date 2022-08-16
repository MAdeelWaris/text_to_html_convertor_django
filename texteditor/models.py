from contextlib import nullcontext
from tokenize import blank_re
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Editor(models.Model):
    body=RichTextField(blank = True,null = True)
