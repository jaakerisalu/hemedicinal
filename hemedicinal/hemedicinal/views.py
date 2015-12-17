import json
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import connection
from django.forms import model_to_dict
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from accounts.models import User
from hemedicinal.forms import DrugSelectionForm, DrugEditForm, dictfetchall
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
            # Get drug detailed info
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM f_anna_ravim(%s)" % form.cleaned_data['drug'])

            res = dictfetchall(cursor)

            drug = res[0]
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
        drug_id = request.GET.get('id', None)
        cursor = connection.cursor()

        # Get drug detailed info
        drug = None
        if drug_id is not None:

            cursor.execute("SELECT * FROM f_anna_ravim(%s)" % drug_id)

            res = dictfetchall(cursor)

            drug = res[0]

        form = DrugEditForm(request.POST if form_was_posted else None,)
        context.update({
            'drug': drug,
            'form': form
        })

        if form_was_posted:
            if form.is_valid():
                if int(form.cleaned_data['status']) == 1:
                    cursor.execute("SELECT f_aktiveeri_ravim('%s')" % drug['ravimi_nimetus'])
                else:
                    cursor.execute("SELECT f_deaktiveeri_ravim('%s')" % drug['ravimi_nimetus'])
                return redirect(reverse('success'))
            else:
                return HttpResponseBadRequest(json.dumps({
                                                         "success": False,
                                                         "errors": form.errors,
                                                     }, ensure_ascii=False), content_type='application/json')

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

