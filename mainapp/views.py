from datetime import datetime

from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_title"] = "Громкий новостной заголовок"
        context[
            "news_preview"
        ] = "Предварительное описание, которое заинтересует каждого"
        context["range"] = range(5)
        context["datetime_obj"] = datetime.now()
        return context


class NewsWithPaginatorView(NewsView):

    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        print(self.request.GET.get('param1'))
        return context


