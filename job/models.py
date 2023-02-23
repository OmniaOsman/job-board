from django.db import models

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
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=uploaded_image)
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name