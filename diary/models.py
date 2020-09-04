from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

PRIVACY_STATUS = (
    ('private', 'Private'),
    ('public', 'Public')
)
class PrivacyManager (models.Manager):
    def get_queryset(self):
        return super (PrivacyManager, self).get_queryset()\
                                            .filter(Privacy = 'public')
class Day (models.Model):
    Profile = models.ForeignKey (User, on_delete = models.PROTECT, default = 1)
    Date = models.DateField(default=timezone.now)
    Name = models.CharField(max_length = 100, default = 'My Day')
    Happiness_Score = models.IntegerField(default = 5)
    Description = models.CharField (max_length = 10000, default = 'Just an average day.')
    Privacy = models.CharField (max_length = 20, choices = PRIVACY_STATUS, default = 'private')
    Last_Edit_Time = models.DateTimeField(default = timezone.now)
    Slug = models.SlugField (max_length = 100, unique_for_date = 'Last_Edit_Time')
    objects = models.Manager()
    Public = PrivacyManager()
    class Meta:
        ordering = ('-Last_Edit_Time',)
    def get_absolute_url (self):
        return reverse ('diary:day_detail',
                        args = [self.Last_Edit_Time.year,
                        self.Last_Edit_Time.month,
                        self.Last_Edit_Time.day, self.Slug])
    def __str__(self):
        return self.Name
