from django.views.generic import TemplateView, CreateView
from applications.entry.models import Entry
from .models import Home
from .forms import SubscriberForm


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = Home.objects.filter(
            is_published=True).latest('created')
        context['home_cover'] = Entry.objects.get_home_cover()
        context['home_entries'] = Entry.objects.get_home_entries()
        context['recent_entries'] = Entry.objects.get_recent_entries()

        context['form'] = SubscriberForm()

        return context


class SubscriberCreateView(CreateView):
    form_class = SubscriberForm
    success_url = '/'
