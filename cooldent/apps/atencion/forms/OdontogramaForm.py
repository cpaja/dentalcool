from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field
from django import forms

from apps.atencion.models import Odontograma


class OdontogramaForm(forms.ModelForm):
    class Meta:
        model = Odontograma
        exclude = ('estado', 'historia', 'fecha')

    def __init__(self, *args, **kwargs):
        super(OdontogramaForm, self).__init__(*args, **kwargs)

        ####### Modelos de estudio ######
        
        self.fields['de_aleta_mordida'] = forms.BooleanField(required=False,
            label='De aleta mordida')
        self.fields['periapical'] = forms.BooleanField(label='Periapical', required=False)
        self.fields['panoramica'] = forms.BooleanField(label='Panorámica',required=False)
        self.fields['oclusal'] = forms.BooleanField(label='oclusal', required=False)
        self.fields['examenes_radigrafia_otros'] = forms.CharField(
            label='Otros', required=False)
        self.fields['montados_asa'] = forms.BooleanField(required=False,
            label='Montados en ASA')
        self.fields['sin_montar'] = forms.BooleanField(label='Sin montar', required=False)
        self.fields['examenes_modelos_otros'] = forms.CharField(label='Otros', required=False)
        self.helper = FormHelper()

        self.helper.form_name = 'odontograma_form'
        self.helper.form_id = 'odontograma_form'
        self.helper.layout = Layout(
            Fieldset(
                'Diagnóstico',
                Div(Field('informe', rows=3), css_class='col-md-6'),
                Div(Field('plan_tratamiento', rows=3), css_class='col-md-6'
                    ),
            ),
            Div(
                Fieldset(
                    'Radiografías',
                    Div(Field('de_aleta_mordida',
                              'periapical', 'panoramica',
                              'oclusal', 'examenes_radigrafia_otros')), css_class='col-md-6'
                ),
                Fieldset(
                    'Modelo de Estudio',
                    Div(Field('montados_asa',
                              'sin_montar', 'examenes_modelos_otros',
                              )), css_class='col-md-6'
                ))
        )
