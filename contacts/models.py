from datetime import datetime

import pytz
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    company = models.CharField(max_length=50, verbose_name=_('company'))
    select = models.CharField(max_length=50, verbose_name=_('select'))
    comment = models.TextField()

    view = models.BooleanField(default=False, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
