from django.db import models
from django.core.mail import send_mail

class Job(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    job = models.ForeignKey("Job", on_delete=models.CASCADE, related_name="applications")
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField(blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"{self.name} - {self.job.title}"

    def send_status_email(self):
        """Sends an email notification when the application status changes."""
        subject = f"Update on Your Job Application for {self.job.title}"
        
        if self.status == "Approved":
            message = f"""
            Dear {self.name},

            Congratulations! Your application for the position of {self.job.title} has been Approved.

            Our team will contact you soon with further details.

            Best Regards,  
            Hiring Team  
            """
        elif self.status == "Rejected":
            message = f"""
            Dear {self.name},

            Thank you for applying for the {self.job.title} position.  

            Unfortunately, your application has been Rejected at this time.  
            We appreciate your time and encourage you to apply for future openings.

            Best Regards,  
            Hiring Team  
            """

        send_mail(
            subject,
            message,
            "your_email@gmail.com",  # 🔹 Replace with your email
            [self.email],
            fail_silently=True
        )

    def save(self, *args, **kwargs):
        """Sends an email when the status of the application is updated."""
        if self.pk:  # Check if application already exists (update case)
            old_status = JobApplication.objects.get(pk=self.pk).status
            if old_status != self.status:  # If status changed
                self.send_status_email()
        super().save(*args, **kwargs)
