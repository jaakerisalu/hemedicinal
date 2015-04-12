from django.views.generic import TemplateView
from hemedicinal.models import Drug


class DrugView(TemplateView):
    template_name = 'drug.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        drugs = Drug.objects.filter(name__iexact="paratsetamool")
        print(drugs.query)
        context.update({
            'drugs': drugs,
        })
        return context


