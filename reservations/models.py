from django.db import models


class BookingRequest(models.Model):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"

    STATUS_CHOICES = [
        (NEW, "New"),
        (IN_PROGRESS, "In progress"),
        (CONFIRMED, "Confirmed"),
        (REJECTED, "Rejected"),
    ]

    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)

    service_type = models.CharField(max_length=120)  # mariage, corporate, event...
    event_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=160, blank=True)

    message = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.full_name} - {self.service_type} ({self.status})"
