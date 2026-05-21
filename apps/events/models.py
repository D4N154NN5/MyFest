from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="led_teams",
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="teams",
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_events",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-start_date"]


class Shift(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="shifts")
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name="shifts")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.PositiveIntegerField(default=1)

    def confirmed_count(self):
        return self.assignments.filter(status=ShiftAssignment.Status.CONFIRMED).count()

    def waitlist_count(self):
        return self.assignments.filter(status=ShiftAssignment.Status.WAITLIST).count()

    def is_full(self):
        return self.confirmed_count() >= self.capacity

    def free_spots(self):
        return max(0, self.capacity - self.confirmed_count())

    def __str__(self):
        return f"{self.title} ({self.event.name})"

    class Meta:
        ordering = ["start_time"]


class ShiftAssignment(models.Model):
    class Status(models.TextChoices):
        CONFIRMED = "confirmed", "Bestätigt"
        WAITLIST = "waitlist", "Warteliste"
        CANCELLED = "cancelled", "Abgesagt"

    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name="assignments")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assignments",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CONFIRMED,
    )
    registered_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("shift", "user")
        ordering = ["registered_at"]

    def __str__(self):
        return f"{self.user} → {self.shift} [{self.get_status_display()}]"
