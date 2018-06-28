from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Row, HTML, Submit, Reset
from crispy_forms.bootstrap import FormActions, TabHolder, Tab
from django.utils.translation import ugettext_lazy as _
from apps.utils.forms import smtSave, btnCancel, btnReset
from django.utils.text import capfirst, get_text_list
from unicodedata import normalize
from ..models import Persona


class PersonaForm(forms.ModelForm):
    """Class PersonaForm."""

    class Meta:
        model = Persona
        exclude = ('estado_civil','estado')

        # 'nombres': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese nombres'}),
        # 'apellido_paterno': forms.TextInput(
        #     attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese Apellido Paterno'}),
        # 'apellido_materno': forms.TextInput(
        #     attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese Apellido Materno'}),
        # 'dni': forms.NumberInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese dni'}),
        # 'codigo': forms.NumberInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese Código'}),
        # 'fecha_nacimiento': forms.DateInput(
        #     attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese Fecha de Nacimiento'}),
        # 'edad': forms.NumberInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese edad'}),
        # 'estado_civil': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
        # 'sexo': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
        # 'telefono': forms.TextInput(
        #     attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese Telefono/Celular'}),
        # 'ocupacion': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
        # 'direccion_actual': forms.TextInput(
        #     attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese Direccion Actual'}),
        # 'departamento': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
        # 'provincia': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
        # 'distrito': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
        # 'contacto': forms.TextInput(
        #     attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Ingrese Numero de Contacto'}),

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['dni'] = forms.CharField(
            label=u'DNI', required=False,
            help_text=u'<small class="help-error"></small> %s' % u' ',
        )
        self.fields['fecha_nacimiento'].widget.format = '%d/%m/%Y'

        self.helper = FormHelper()
        self.helper.form_id = 'persona_form'
        self.helper.form_name = 'persona_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('nombres', 'apellido_paterno', 'apellido_materno', 'dni', 'sexo',
                    'fecha_nacimiento',
                    css_class='col-md-6'),
                Div('departamento', 'provincia', 'distrito', 'direccion_actual', 'ocupacion', 'telefono',
                    css_class='col-md-6'),
                css_class='row'
            )
        )
