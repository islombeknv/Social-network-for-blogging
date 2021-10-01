from django.db import models


class EmailModel(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'email'
