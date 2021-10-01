from django.views.generic import CreateView

from postemail.forms import EmailModelForm
from postemail.models import EmailModel


class EmailCreateView(CreateView):
    template_name = 'layouts/footer.html'
    form_class = EmailModelForm
    model = EmailModel
    success_url = '/'
