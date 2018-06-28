from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, Field, HTML
from django import forms

from ..models import Consulta


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        exclude = ('usuario', 'historia')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_name = 'cita_form'
        self.helper.form_id = 'cita_form'
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    'Datos del Paciente',
                    HTML("""
                        <p>
                            <b>Nombre:</b>
                            {{ persona.nombres }} {{ persona.apellido_paterno }} {{ persona.apellido_materno }}
                        </p>
                        <p>
                            <b>D.N.I.</b>
                            {{ persona.dni }}
                        </p>
                        """),
                    'motivo',
                    'estado',
                    css_class='col-md-6'
                ),
            ),
            Div(
                Fieldset(
                    'Datos de la Cita',
                    Div('trabajador', css_class='col-md-12'),
                    Div(
                        'fecha',
                        css_class='col-md-6'
                    ),
                    Div(
                        'horario',
                        css_class='col-md-6'
                    ),
                    Div(
                        Field('observaciones', rows=3),
                        css_class='col-md-12'
                    )
                ), css_class='col-md-6'
            )
        )
        super(ConsultaForm, self).__init__(*args, **kwargs)
