from contacts.models import ContactModel


def get_profile(request):
    return {
        'contacts': ContactModel.objects.filter(view=False).order_by('-pk')
    }
