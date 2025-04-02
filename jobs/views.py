from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Job, JobApplication
from .forms import JobApplicationForm

def job_list(request):
    query = request.GET.get('q', '').strip()  # Get and clean search query
    jobs = Job.objects.all()

    if query:
        search_terms = query.split()  # Split into keywords
        filters = Q()
        
        for term in search_terms:
            filters |= (Q(title__icontains=term) | 
                        Q(description__icontains=term) | 
                        Q(location__icontains=term) |
                        Q(requirements__icontains=term))  # Added filtering for requirements

        jobs = jobs.filter(filters)

    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'query': query})

@login_required
def recruiter_dashboard(request):
    jobs = Job.objects.all()
    applications = JobApplication.objects.all()
    return render(request, "jobs/dashboard.html", {"jobs": jobs, "applications": applications})

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
