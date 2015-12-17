import json
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms import model_to_dict
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from accounts.models import User
from hemedicinal.forms import DrugSelectionForm, DrugEditForm
from hemedicinal.models import Drug


class ProtectedMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProtectedMixin, self).dispatch(request, *args, **kwargs)


class DrugView(ProtectedMixin, TemplateView):
    template_name = 'drug.html'

    def get(self, request, *args, **kwargs):
        form_was_posted = request.POST.get('save') is not None
        form = DrugSelectionForm(request.POST if form_was_posted else None,)

        drug = None
        if form.is_valid():
            drug = Drug.objects.get(id=form.cleaned_data['drug'])
            form = None

        context = self.get_context_data(**kwargs)
        context.update({
            'form': form,
            'drug': drug,
        })
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class DrugEditView(ProtectedMixin, TemplateView):
    template_name = 'drugedit.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form_was_posted = request.POST.get('save') is not None

        drug = Drug.objects.get(id=request.GET.get('id', ''))
        form = DrugEditForm(request.POST if form_was_posted else None, instance=drug)
        context.update({
            'drug': drug,
            'form': form
        })

        if form_was_posted:
            if form.is_valid():
                drug = form.save()
                return redirect(reverse('success'))
            else:
                return HttpResponseBadRequest(json.dumps({
                                                         "success": False,
                                                         "errors": form.errors,
                                                     }, ensure_ascii=False), content_type='application/json')

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

