from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.


from .models import Job
from .forms import JobApplicationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import JobApplication 
from django.db.models import Q

from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def recruiter_dashboard(request):
    jobs = Job.objects.all()
    applications = JobApplication.objects.all()
    return render(request, "jobs/dashboard.html", {"jobs": jobs, "applications": applications})


# View for listing all jobs
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# View for job details
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})


def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('job_list')  # Redirect to job list page after applying
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/job_application.html', {'form': form, 'job': job})