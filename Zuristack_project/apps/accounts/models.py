#from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

from .managers import CustomUserManager
from . import utils

# Create your models here.

class customUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    slug = models.SlugField(blank=True, unique=True)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager()

    class Meta:
        ordering = ["email"]
        verbose_name = "User"

    def __str__(self):
        return self.email

    #Creating a default slug/username for users if blank.
    def gen_random_slug(self):
        random_slug = slugify(self.first_name + self.last_name +utils.generate_random_id())
        while customUser.objects.filter(slug=random_slug).exists():
                random_slug = slugify(self.first_name + self.last_name +utils.generate_random_id())
        self.slug = self.gen_random_slug()
        return random_slug

    def save(self, *args, **kwarggs):
        #check for a slug
        if not self.slug:
            #create default slug
            random_slug = slugify(self.first_name + self.last_name +utils.generate_random_id())

            while customUser.objects.filter(slug=random_slug).exists():
                random_slug = slugify(self.first_name + self.last_name +utils.generate_random_id())
            self.slug = random_slug
        #Finally save
        super().save(*args, **kwarggs)