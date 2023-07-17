from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView

# import news_project.news_app.models
from .models import *
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()

    context = {
        'news_list': news_list
    }

    return render(request, "news/news_list.html", context)


def news_single(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news

    }
    return render(request, 'news/single_page.html', context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        'news': news

    }
    return render(request, 'news/news_detail.html', context)


# def homepageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:5]
#     locol_one = News.published.filter(category__name='Jamiyat').order_by('-publish_time')[:1]
#     locol_news = News.published.all().filter(category__name='Jamiyat')[1:5]
#
#     context = {
#         'news_list': news_list,
#         'categories': categories,
#         'locol_news': locol_news,
#         'locol_one': locol_one
#     }
#     return render(request, 'news/home.html', context)


class HomePage(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        context['locol_one'] = News.published.filter(category__name='Jamiyat').order_by('-publish_time')[:1]
        context['locol_news'] = News.published.all().filter(category__name='Jamiyat')[1:5]
        context['eco_news'] = News.published.all().filter(category__name='Iqtisodiyot')
        context['sport_one'] = News.published.filter(category__name='Sport').order_by('-publish_time')[:1]
        context['sport_news'] = News.published.all().filter(category__name='Sport')[1:5]
        context['fan_one'] = News.published.filter(category__name='Fan-Texnika').order_by('-publish_time')[:1]
        context['fan_news'] = News.published.all().filter(category__name='Fan-Texnika')[1:5]
        context['xorij_one'] = News.published.filter(category__name='Xorij').order_by('-publish_time')[:1]
        context['Xorij_news'] = News.published.all().filter(category__name='Xorij')[1:5]

        return context


class ContactPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request,'news/contact.html', context)

    def post(self, request,*args,**kwargs):
        form = ContactForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            form.save()

            return HttpResponse("<h2> Biz bilan bog'langaniz uchun rahmat:"
                                "Biz sizni har doim qo'lab quvvatlaymiz 😊:</h2>")
        context = {
            'form': form

        }
        return render(request, 'news/contact.html', context)


def contactPageView(request):
    print(request.POST)
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()

        return HttpResponse("<h2> Biz bilan bog'langaniz uchun rahmat:"
                            "Biz sizni har doim qo'lab quvvatlaymiz 😊:</h2>")
    context = {
        'form': form

    }
    return render(request, 'news/contact.html', context)


class MahalliyNewsViews(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Jamiyat')
        return news


class IqtNewsViews(ListView):
    model = News
    template_name = 'news/iqtisodiy.html'
    context_object_name = 'iqtisodiy_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Iqtisodiyot')
        return news


class fanNewsViews(ListView):
    model = News
    template_name = 'news/fan.html'
    context_object_name = 'fan_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Fan-Texnika')
        return news


class xorijNewsViews(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorij')
        return news


class sportNewsViews(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news


class nutqNewsViews(ListView):
    model = News
    template_name = 'news/nutq.html'
    context_object_name = 'nutq_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Nuqtayi-Nazar')
        return news


class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')


class NewsCreateView(CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')
