from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE,
                                related_name='profile', verbose_name=_('user'))

    username = models.CharField(max_length=150,
                                verbose_name=_('username'),
                                null=True, blank=True)
    image = models.ImageField(verbose_name=_('image'), null=True, blank=True)
    email = models.EmailField(verbose_name=_('email'), null=True, blank=True)
    fullname = models.CharField(max_length=150, verbose_name=_('fullname'), null=True, blank=True)
    phone = models.IntegerField(verbose_name=_('phone'), null=True, blank=True)
    position = models.CharField(max_length=100, verbose_name=_('position'), null=True, blank=True)
    address = models.CharField(max_length=250, verbose_name=_('address'), null=True, blank=True)

    twitter = models.CharField(max_length=250, verbose_name=_('twitter'), null=True, blank=True)
    instagram = models.CharField(max_length=250, verbose_name=_('instagram'), null=True, blank=True)
    facebook = models.CharField(max_length=250, verbose_name=_('facebook'), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'), null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = _('userprofile')
        verbose_name_plural = _('userprofile')