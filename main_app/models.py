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

    def str(self):
        return f"{self.job_title} at {self.company_name}"
    