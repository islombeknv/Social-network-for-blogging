from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from blogs import settings
from postemail.models import EmailModel
from posts.models import PostModel


@receiver(post_save, sender=PostModel)
def send_email(sender, instance, *args, **kwargs):
    email = EmailModel.objects.order_by('-pk')
    if email:
        for users in email:
            text = f'{instance.title}\n{instance.postinfo}\n' \
                   f'link: http://127.0.0.1:8000/post/detail/{instance.id}/'
            send_mail(
                'Notification',
                text,
                settings.EMAIL_HOST_USER,
                [users],
            )
