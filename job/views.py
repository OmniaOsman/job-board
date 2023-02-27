from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, PostJob

# Create your views here.
def job_list(request):
    jobs_list = Job.objects.all()
    # pagination
    paginator = Paginator(jobs_list, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)


def job_details(request, slug):
    job_details = Job.objects.get(slug=slug)
    
    # Apply job
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False) # don't save now
            myForm.job = job_details
            myForm.save()
    else:
        form = ApplyForm()
        
    context = {'job': job_details, 'form': form}
    return render(request, 'job/job_details.html', context)


def add_job(request):
    # Post new job
    if request.method == 'POST':
        form = PostJob(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.job_owner = request.user
            myForm.save()
            return redirect(reverse('jobs:job-list'))
    else:
        form = PostJob()
        
    context = {'form': form}
    return render(request, 'job/add_job.html', context)