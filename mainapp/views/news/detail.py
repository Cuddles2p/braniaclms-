__all__ = ['NewsDetailView']
from django.views.generic import DetailView
from mainapp.models import News


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(News, pk=pk)
        return context