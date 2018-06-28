from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field
from django import forms

from apps.atencion.models import Odontograma, HistoriaDetalle


class HistoriaDetalleForm(forms.ModelForm):
    class Meta:
        model = HistoriaDetalle
        exclude = ('historia', 'fecha')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_name = 'historia_form'
        self.helper.form_id = 'historia_form'
        self.helper.layout = Layout(
            Fieldset(
                'Registrar Historial',
                Div('doctor', css_class='col-md-6'),
                Div('precio', css_class='col-md-6'),
                Div(Field('tratamiento', rows=4), css_class='col-md-12'
                    ),
            )
        )
        super(HistoriaDetalleForm, self).__init__(*args, **kwargs)
