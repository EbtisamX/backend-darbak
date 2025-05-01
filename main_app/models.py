from django.db import models

# Create your models here.

APPLICATION_STATUS_CHOICES = (
    ('waiting', 'Waiting'),
    ('interview', 'Interview Scheduled'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
)

class JobApplication(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    application_date = models.DateField()
    application_status = models.CharField(
        max_length=20,
        choices=APPLICATION_STATUS_CHOICES,
        default='waiting'
    )

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    
class Note(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically sets the current date/time when the note is created, from https://www.geeksforgeeks.org/datetimefield-django-models/
    job = models.ForeignKey(JobApplication, on_delete=models.CASCADE)

    def __str__(self):
        return f"Note for {self.job.job_title} - {self.created_at.date()}"
    