from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Field, Submit
from django import forms
from hemedicinal.models import Drug


class DrugSelectionForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ('drug',)

    drug = forms.ChoiceField(label="")

    def __init__(self, *args, **kwargs):
        # self.drug = kwargs.pop('drug')
        super().__init__(*args, **kwargs)

        self.fields['drug'].choices = [(c.id, c.name) for c in Drug.objects.filter(status=Drug.STATUS_ACTIVE)]

        self.helper = FormHelper()
        self.helper.add_input(Submit('save', "Edasi", css_class='btn btn-success btn-lg'))

        self.helper.layout = Layout(
            HTML('<h4>Vali ravim</h4>'),
            Div(Field('drug', css_class="js-drugs"), css_class='col-md-12'),
        )


class DrugEditForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ('description', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('save', "Salvesta", css_class='btn btn-success btn-lg'))
        self.helper.action = "."