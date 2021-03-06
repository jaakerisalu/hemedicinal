from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from hemedicinal.views import DrugView, DrugEditView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('accounts.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^drug/$', DrugView.as_view(), name='drug'),
    url(r'^drug/edit/$', DrugEditView.as_view(), name='drug_edit'),
    url(r'^success/$', TemplateView.as_view(template_name='success.html'), name='success'),


    url(r'^tagauks/', include(admin.site.urls)),
)
