from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Field, Submit
from django import forms
from django.db import connection
from django.forms import FloatField
from hemedicinal.models import Drug

def dictfetchall(cursor):
    # Helper method to return all results as a dict
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class DrugSelectionForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ('drug',)

    drug = forms.ChoiceField(label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get drug info
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM ravimi_informatsioon")

        res = dictfetchall(cursor)

        self.fields['drug'].choices = [(drug['ravimi_kood'], drug['ravimi_nimetus'] + ",   Mõjuaine:     " + drug['ravimi_mojuaine'] + "   [" + drug['ravimi_mojuaine_atc_kood'] + "] ") for drug in res]

        self.helper = FormHelper()
        self.helper.add_input(Submit('save', "Edasi", css_class='btn btn-success btn-lg'))

        self.helper.layout = Layout(
            HTML('<h4>Vali ravim</h4>'),
            Div(Field('drug', css_class="js-drugs"), css_class='col-md-12'),
        )


class DrugEditForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ('status',)

    status = forms.ChoiceField(label="Ravimi seisund")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status'].choices = [(1, "Aktiivne"), (2, "Mitteaktiivne")]
        self.helper = FormHelper()
        self.helper.add_input(Submit('save', "Salvesta", css_class='btn btn-success btn-lg'))
        self.helper.action = "."
        self.helper.field_class = 'col-md-8 pull-right'