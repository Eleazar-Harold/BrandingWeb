
from django.core.mail import send_mail
from .forms import ContactForm
import os
from django.conf import settings
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class AboutView(TemplateView):
    template_name = 'pages/about_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        context['title'] = 'About'
        return context


class ServiceView(TemplateView):
    template_name = 'pages/services_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ServiceView, self).get_context_data(*args, **kwargs)
        contentlist = []
        with open(os.path.join(settings.PROJECT_ROOT, 'listcnt.txt')) as inputfile:
            for line in inputfile:
                contentlist.append(line)
        context['title'] = 'Services'
        context['contentlist'] = contentlist
        return context


class PortfolioView(TemplateView):
    template_name = 'pages/portfolio_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PortfolioView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Portfolio'
        return context


class ContactView(TemplateView):
    template_name = 'pages/contact_page.html'
    form_class = ContactForm()

    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Contact'
        context['mini_title'] = "Contact Us"
        context['forms'] = ContactForm()
        return context

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        msg = form.cleaned_data['message']
        email = form.cleaned_data['email']
        send_mail(subject, msg, email, ['haroldyewa@gmail.com'], fail_silently=False)

        return super(ContactView, self).form_valid(form)
