from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
JOB_TYPE = (
    ('Full-Time', 'Full-Time'),
    ('Part-Time', 'Part-Time')
)

def uploaded_image(instance, filename):
    """
        function to save image which uploaded from user in form (id.extension)
    """
    imageTitle, extension = filename.split('.')
    return 'jobs/%s.%s' %(instance.id, extension)


class Job(models.Model):
    title        = models.CharField(max_length=100)
    job_type     = models.CharField(max_length=15, choices=JOB_TYPE)
    description  = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy      = models.IntegerField(default=1)
    salary       = models.IntegerField(default=0)
    experience   = models.IntegerField(default=1)
    category     = models.ForeignKey("Category", on_delete=models.CASCADE)
    slug         = models.SlugField(blank=True, null=True)
    job_owner    = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)   
    
    # override on save an object
    def save(self, *args, **kwargs):
        """make auto slug using slugify to replace space with '-' """
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    

class Apply(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=254)
    website      = models.URLField()
    cv           = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    applied_at   = models.DateTimeField(auto_now=True, auto_now_add=False)
    job          = models.ForeignKey("Job", related_name='apply_job' ,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name