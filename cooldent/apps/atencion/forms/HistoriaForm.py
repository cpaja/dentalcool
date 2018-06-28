from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field
from django import forms

from ..models import Historia

EXAMEN_CHOICE = (
    ('------', '------'),
    ('SAE', 'SAE'),
    ('Conservado', 'Conservado'),   
    ('Especificar', 'Especificar'),
)


class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        exclude = ('numero', 'estado', 'persona')

    def __init__(self, *args, **kwargs):
        super(HistoriaForm, self).__init__(*args, **kwargs)
        self.fields['examen_atm'] = forms.ChoiceField(
            choices=EXAMEN_CHOICE, required=True)
        self.fields['examen_atm_ganglios'] = forms.ChoiceField(
            required=True,  choices=EXAMEN_CHOICE)
        self.fields['examen_labios'] = forms.ChoiceField(
            choices=EXAMEN_CHOICE, required=True)
        self.fields['examen_vestibulo'] = forms.ChoiceField(
            choices=EXAMEN_CHOICE, required=True)
        self.fields['examen_lengua'] = forms.ChoiceField(
            choices=EXAMEN_CHOICE, required=True)
        self.fields['examen_paladar'] = forms.ChoiceField(
            choices=EXAMEN_CHOICE, required=True)
        self.fields['examen_piso_boca'] = forms.ChoiceField(
            choices=EXAMEN_CHOICE, required=True)
        self.fields['examen_periodonto'] = forms.ChoiceField(
            choices=EXAMEN_CHOICE, required=True)

        self.fields['examen_atm_s'] = forms.CharField(
            required=False, help_text=u'<small class="help-error"></small> %s' % u' '
        )
        self.fields['examen_atm_ganglios_s'] = forms.CharField(
            required=False, help_text=u'<small class="help-error"></small> %s' % u' '
        )
        self.fields['examen_labios_s'] = forms.CharField(
            required=False, help_text=u'<small class="help-error"></small> %s' % u' '
        )
        self.fields['examen_vestibulo_s'] = forms.CharField(
            required=False, help_text=u'<small class="help-error"></small> %s' % u' '
        )
        self.fields['examen_lengua_s'] = forms.CharField(
            required=False, help_text=u'<small class="help-error"></small> %s' % u' '
        )
        self.fields['examen_paladar_s'] = forms.CharField(
            required=False, help_text=u'<small class="help-error"></small> %s' % u' '
        )
        self.fields['examen_piso_boca_s'] = forms.CharField(
            required=False, help_text=u'<small class="help-error"></small> %s' % u' '
        )
        self.fields['examen_periodonto_s'] = forms.CharField(
            required=False, help_text=u'<small class="help-error"></small> %s' % u' '
        )

        self.helper = FormHelper()
        self.helper.form_name = 'historia_form'
        self.helper.form_id = 'historia_form'
        self.helper.layout = Layout(
            Div(
                Div(
                    Fieldset(
                        'Consulta',
                        Div('procedencia', css_class='col-md-12'),
                        Div(
                            'motivo_consulta',
                            css_class='col-md-6'
                        ),
                        Div(
                            'riesgo',
                            css_class='col-md-6'
                        ),
                    ), css_class='col-md-6'
                ),
                Div(
                    Fieldset(
                        'Anamnesis',
                        Div(
                            'anamnesis_atencion_medica',
                            'anamnesis_alergia',
                            'anamnesis_enfermedad',
                            'anamnesis_embarazo',
                            Field('anamnesis_otros', rows=6),
                            css_class='col-md-12'
                        )
                    ), css_class='col-md-6'
                ),
                Div(
                    Fieldset(
                        'Antecedentes Patologicos y Quirurgicos',
                        Div(
                            'antecedentes_diabetes',
                            'antecedentes_tuberculosis',
                            'antecedentes_enf_renal',
                            'antecedentes_anemia',
                            'antecedentes_fiebre_reumatica',
                            css_class='col-md-6'
                        ),
                        Div(
                            'antecedentes_hemorragias',
                            'antecedentes_infecciones',
                            'antecedentes_enf_cardio',
                            'antecedentes_alerg_penicilina',
                            'antecedentes_enf_hepaticas',
                            css_class='col-md-6'
                        )
                    ), css_class='col-md-6'
                ),

                Div(
                    Fieldset(
                        'Examen Clinico Estomatologico',
                        Div(
                            'examen_atm',

                            Field('examen_atm_s', type='hidden',
                                  css_class='form-control', placeholder='Especifique Examen ATM'),
                            'examen_atm_ganglios',
                            Field('examen_atm_ganglios_s', type='hidden',
                                  css_class='form-control', placeholder='Especifique Examen Atm Ganglios'),
                            'examen_labios',
                            Field('examen_labios_s', type='hidden',
                                  css_class='form-control', placeholder='Especifique Examen Labios'),
                            'examen_vestibulo',
                            Field('examen_vestibulo_s', type='hidden',
                                  css_class='form-control', placeholder='Especifique Examen vetibulo'),
                            'examen_lengua',
                            Field('examen_lengua_s', type='hidden',
                                  css_class='form-control', placeholder='Especifique Examen Lengua'),
                            'examen_paladar',
                            Field('examen_paladar_s', type='hidden',
                                  css_class='form-control', placeholder='Especifique Examen Paladar'),
                            css_class='col-md-6'
                        ),
                        Div(
                            'examen_piso_boca',
                            Field('examen_piso_boca_s', type='hidden',
                                  css_class='form-control', placeholder='Especifique Examen piso Boca'),
                            'examen_periodonto',
                            Field('examen_periodonto_s', type='hidden',
                                  css_class='form-control', placeholder='Especifique Examen Periodonto'),
                            # 'examen_ampliacion',
                            Field('examen_otros', rows=7),
                            css_class='col-md-6'
                        )
                    ), css_class='col-md-6'
                ),
                css_class='row')
        )
