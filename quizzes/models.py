from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta, timezone
from users.models import YourQUser
# Create your models here.


class Quiz(models.Model):

    name = models.CharField(_("name"), max_length=20)
    date_of_creation = models.DateTimeField(_("date of creation"))
    date_of_expiry = models.DateTimeField(_("date of expiry"))
    author = models.ForeignKey(YourQUser, on_delete=models.CASCADE)    
    likes = models.PositiveIntegerField(_('likes'), default=0)
    views = models.PositiveIntegerField(_('views'), default=0)
    execute = models.PositiveIntegerField(_('execute'), default=0)

    def save(self, *args, **kwargs):
        if not self.date_of_creation:
            self.date_of_creation = datetime.now().replace(tzinfo=timezone.utc)
        if not self.date_of_expiry:
            self.date_of_expiry = self.date_of_creation + timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.author}"
