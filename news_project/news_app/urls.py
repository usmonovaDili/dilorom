from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_page'),
    path('news<int:id>/', news_detail, name='news_detail_page'),
    path('contact-us/', contactPageView, name='contact_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:news>/', news_single, name='single_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('locol-news/', MahalliyNewsViews.as_view(), name='locol_news_page'),
    path('xorij-news/', xorijNewsViews.as_view(), name='xorij_news_page'),
    path('sport-news/', sportNewsViews.as_view(), name='sport_news_page'),
    path('fan-news/', fanNewsViews.as_view(), name='fan_news_page'),
    path('nutq-news/', nutqNewsViews.as_view(), name='nutq_news_page'),
    path('iqt-news/', IqtNewsViews.as_view(), name='iqt_news_page')
]
