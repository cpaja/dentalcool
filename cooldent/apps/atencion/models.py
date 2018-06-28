"""Models lslsl."""
from django.db import models

estado_civil = (
    ('Soltero', 'Soltero'),
    ('Casado', 'Casado'),
    ('Divorciado', 'Divorciado'),
    ('Viudo', 'Viudo'),
    ('Conviviente', 'Conviviente'),
)

examen_atm = (
    ('------', '------'),
    ('SAE', 'SAE'),
    ('Conservado', 'Conservado'),
    ('Especificar', 'Especificar'),
)
examen_ganglios = (
    ('------', '------'),
    ('SAE', 'SAE'),
    ('Conservado', 'Conservado'),
    ('Especificar', 'Especificar'),
)

estado_cita = (
    ('REGISTRADO', 'Registrado'),
    ('CONFIRMADO', 'Confirmado'),
    ('CANCELADO', 'Cancelado'),
)

motivos_cita = (
    # ('Seleccione Motivo de Consulta', 'Seleccione Motivo de Consulta'),
    ('Control de tratamiento', 'Control de tratamiento'),
    ('Limpieza', 'Limpieza'),
    ('Primera Consulta', 'Primera COnsulta'),
    ('Urgencia', 'Urgencia'),

)

horarios = (
    ('08:00', '08:00'), ('08:15', '08:15'), ('08:30', '08:30'), ('08:45', '08:45'),
    ('09:00', '09:00'), ('09:15', '09:15'), ('09:30', '09:30'), ('09:45', '09:45'),
    ('10:00', '10:00'), ('10:15', '10:15'), ('10:30', '10:30'), ('10:45', '10:45'),
    ('11:00', '11:00'), ('11:15', '11:15'), ('11:30', '11:30'), ('11:45', '11:45'),
    ('12:00', '12:00'), ('12:15', '12:15'), ('12:30', '12:30'), ('12:45', '12:45'),
    ('15:00', '15:00'), ('15:15', '15:15'), ('15:30', '15:30'), ('15:45', '15:45'),
    ('16:00', '16:00'), ('16:15', '16:15'), ('16:30', '16:30'), ('16:45', '16:45'),
    ('17:00', '17:00'), ('17:15', '17:15'), ('17:30', '17:30'), ('17:45', '17:45'),
    ('18:00', '18:00'), ('18:15', '18:15'), ('18:30', '18:30'), ('18:45', '18:45'),
)

sexo = (
    ('Femenino', 'Femenino'),
    ('Masculino', 'Masculino'),
)

ocupacion = (
    ('Medico', 'Medico'),
    ('Estudiante', 'Estudiante'),
    ('Docente', 'Docente'),
    ('TrabajadorIndependiente', 'Trabajador Independiente'),
)
IMC = (
    ('PesoBajo', 'Peso Bajo'),
    ('PesoNormal', 'Peso Normal'),
    ('Sobrepeso', 'Sobre peso'),
    ('Obesidad', 'Obesidad'),
    ('ObesidadSevera', 'Obesidad Severa')
)

tipo_pieza = (
    ('Permanente', 'Permanente'),
    ('Temporal', 'Temporal')
)

cuadrantes = (
    (1, 'Superior Derecho'),
    (2, 'Superior Izquierdo'),
    (3, 'Inferior Derecho'),
    (4, 'Inferior Izquierdo')
)


class Usuario(models.Model):
    """Class Model Usuario. """
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=10)
    # image=models.ImageField(upload_to="", blank=True, null=True)
    sexo = models.CharField(max_length=20, choices=sexo)
    ocupacion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamento"

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincia"

    def __str__(self):
        return self.nombre


class Distrito(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia)

    class Meta:
        verbose_name = "Distrito"
        verbose_name_plural = "Distrito"

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombres = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    departamento = models.ForeignKey(Departamento, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, blank=True, null=True)
    distrito = models.ForeignKey(Distrito, blank=True, null=True)
    dni = models.CharField(max_length=8, unique=True, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField(blank=True, null=True)
    estado_civil = models.CharField(max_length=20, choices=estado_civil, blank=True, null=True)
    sexo = models.CharField(max_length=19, choices=sexo)
    telefono = models.IntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=35, choices=ocupacion, null=True, blank=True)
    direccion_actual = models.CharField(max_length=100)
    contacto = models.CharField(max_length=10, null=True, blank=True)
    nro_historia = models.CharField(max_length=100, default='', null=True, blank=True)
    con_historia = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return "%s %s %s" % (self.nombres, self.apellido_paterno, self.apellido_materno)


class Historia(models.Model):
    persona = models.OneToOneField(Persona)
    # procedencia = models.CharField(max_length=150, null=True)
    numero = models.IntegerField(unique=True)
    fecha_apertura = models.DateTimeField(auto_now_add=True)

    motivo_consulta = models.TextField(null=True)
    riesgo = models.TextField(null=True)
    anamnesis_atencion_medica = models.BooleanField(default=False,
                                                    verbose_name='¿Ha estado bajo atención médica en los últimos años?')
    anamnesis_alergia = models.BooleanField(default=False,
                                            verbose_name='¿Es alérgico a la penicilina u otros medicamentos?')
    anamnesis_enfermedad = models.BooleanField(default=False, verbose_name='¿Padece alguna enfermedad?')
    anamnesis_embarazo = models.BooleanField(default=False, verbose_name='¿Se encuentra embarazada?')
    anamnesis_otros = models.TextField(null=True, blank=True, verbose_name='Ectoscopía')
    antecedentes_diabetes = models.BooleanField(default=False, verbose_name='Diabetes')
    antecedentes_tuberculosis = models.BooleanField(default=False, verbose_name='Tuberculosis')
    antecedentes_enf_renal = models.BooleanField(default=False, verbose_name='Enf. Renal')
    antecedentes_anemia = models.BooleanField(default=False, verbose_name='Anemia')
    antecedentes_fiebre_reumatica = models.BooleanField(default=False, verbose_name='Fiebre Reumatica')
    antecedentes_hemorragias = models.BooleanField(default=False, verbose_name='Hemorragias')
    antecedentes_infecciones = models.BooleanField(default=False, verbose_name='Infecciones')
    antecedentes_enf_cardio = models.BooleanField(default=False, verbose_name='Enf. Cardiovascular')
    antecedentes_alerg_penicilina = models.BooleanField(default=False, verbose_name='Alergia a la Penicilina')
    antecedentes_enf_hepaticas = models.BooleanField(default=False, verbose_name='Enf.Hepaticas')

    # estado_civil = models.CharField(max_length=20, choices=estado_civil)
    examen_atm = models.CharField(max_length=100)
    examen_atm_ganglios = models.CharField(max_length=100)
    examen_labios = models.CharField(max_length=100)
    examen_vestibulo = models.CharField(max_length=100)
    examen_lengua = models.CharField(max_length=100)
    examen_paladar = models.CharField(max_length=100)
    examen_piso_boca = models.CharField(max_length=100)
    examen_periodonto = models.CharField(max_length=100)
    # examen_ampliacion = models.CharField(max_length=100, null=True, blank=True, verbose_name='Otros')
    examen_otros = models.TextField(max_length=150, null=True, blank=True)

    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Historia"
        verbose_name_plural = "Historias"

    def __str__(self):
        return "%s" % self.numero


class Trabajador(models.Model):
    persona = models.ForeignKey(Persona)
    nro_colegio = models.CharField(max_length=10, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.persona.nombres


class HistoriaDetalle(models.Model):
    historia = models.ForeignKey(Historia)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    doctor = models.ForeignKey(Trabajador, verbose_name='Doctor')
    fecha = models.DateField(auto_now_add=True)
    tratamiento = models.TextField()


class Consulta(models.Model):
    usuario = models.ForeignKey(Usuario)
    fecha = models.DateField()
    trabajador = models.ForeignKey(Trabajador, verbose_name='Doctor')
    horario = models.CharField(max_length=5, choices=horarios)
    historia = models.ForeignKey(Historia)
    estado = models.CharField(max_length=20, choices=estado_cita, default='REGISTRADO')
    observaciones = models.TextField(null=True, blank=True)
    motivo = models.CharField(max_length=255, choices=motivos_cita, null=True, blank=True,
                              verbose_name='Motivo de la consulta')

    class Meta:
        unique_together = (("horario", "fecha", "trabajador"),)
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return "%s" % self.historia.persona.nombres


######################### Odontograma ######################################


class CaraDental(models.Model):
    nombre = models.CharField(max_length=20)
    abrev = models.CharField(max_length=1)
    css_class = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.nombre, self.abrev)


class TratamientoDental(models.Model):
    nombre = models.CharField(max_length=100)
    css_class = models.CharField(max_length=50)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden', ]

    def __str__(self):
        return self.nombre


class PiezaDental(models.Model):
    nombre = models.CharField(max_length=100)
    abrev = models.CharField(max_length=5, unique=True)
    orden = models.IntegerField()
    imagen = models.ImageField(upload_to='piezas')
    tipo = models.CharField(max_length=100, choices=tipo_pieza, default='Permanente')
    cuadrante = models.IntegerField(choices=cuadrantes, default=1)
    cara_1 = models.ForeignKey(CaraDental, related_name='cara_1')
    cara_2 = models.ForeignKey(CaraDental, related_name='cara_2')
    cara_3 = models.ForeignKey(CaraDental, related_name='cara_3')
    cara_4 = models.ForeignKey(CaraDental, related_name='cara_4')
    cara_5 = models.ForeignKey(CaraDental, related_name='cara_5')

    def __str__(self):
        return "%s - %s" % (self.nombre, self.abrev)


class Odontograma(models.Model):
    historia = models.ForeignKey(Historia)
    estado = models.BooleanField(default=False)
    informe = models.TextField(null=True, blank=True)
    plan_tratamiento = models.TextField(null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)


class OdontogramaPieza(models.Model):
    odontograma = models.ForeignKey(Odontograma)
    pieza = models.ForeignKey(PiezaDental)
    cuadrante = models.IntegerField(choices=cuadrantes, default=1)
    tratamiento = models.ForeignKey(TratamientoDental, related_name='tratamiento_pieza', null=True, blank=True)
    orden = models.IntegerField()
    cara_0_tratamiento = models.ForeignKey(TratamientoDental, related_name='pieza_usente', null=True,
                                           blank=True)  # para verificar pieza ausente
    cara_1_tratamiento = models.ForeignKey(TratamientoDental, related_name='tratamiento_cara_1', null=True, blank=True)
    cara_2_tratamiento = models.ForeignKey(TratamientoDental, related_name='tratamiento_cara_2', null=True, blank=True)
    cara_3_tratamiento = models.ForeignKey(TratamientoDental, related_name='tratamiento_cara_3', null=True, blank=True)
    cara_4_tratamiento = models.ForeignKey(TratamientoDental, related_name='tratamiento_cara_4', null=True, blank=True)
    cara_5_tratamiento = models.ForeignKey(TratamientoDental, related_name='tratamiento_cara_5', null=True, blank=True)

    class Meta:
        ordering = ['orden', ]


class ExamenesAuxiliares(models.Model):
    odontograma = models.ForeignKey(Odontograma)
    ####### Radiografías #######
    de_aleta_mordida = models.BooleanField(default=False, verbose_name='De aleta mordida')
    periapical = models.BooleanField(default=False, verbose_name='Periapical')
    panoramica = models.BooleanField(default=False, verbose_name='Panorámica')
    oclusal = models.BooleanField(default=False, verbose_name='Oclusal')
    examenes_radigrafia_otros = models.TextField(null=True, blank=True, verbose_name='Otros')
    ####### Modelos de estudio ######
    montados_asa = models.BooleanField(default=False, verbose_name='Montados en ASA')
    sin_montar = models.BooleanField(default=False, verbose_name='Sin montar')
    examenes_modelos_otros = models.TextField(null=True, blank=True, verbose_name='Otros')


############################# Other project ########################################################

class AntecedenteMedico(models.Model):
    historia = models.ForeignKey(Historia)
    antecedente_morbidos = models.TextField(blank=True, null=True, verbose_name='Antecedentes mórbidos')
    antecedente_ginecoobstetrico = models.TextField(blank=True, null=True,
                                                    verbose_name='Antecedentes ginecoobstétricos')
    habito = models.TextField(blank=True, null=True, verbose_name='Hábitos')
    antecedente_medicamento = models.TextField(blank=True, null=True,
                                               verbose_name='Antecedentes sobre uso de medicamentos.')
    alergia = models.TextField(blank=True, null=True, verbose_name='Alergias')
    antecedente_personal_social = models.TextField(blank=True, null=True,
                                                   verbose_name='Antecedentes sociales y personales.')
    atecedente_familiar = models.TextField(blank=True, null=True, verbose_name='Antecedentes familiares')
    inmunizacion = models.TextField(blank=True, null=True, verbose_name='Inmunizaciones')

    class Meta:
        verbose_name = "AntecedenteMedico"
        verbose_name_plural = "AntecedenteMedicos"

    def __str__(self):
        return self.alergia


class FuncionesVitales(models.Model):
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    presion_arterial = models.IntegerField()
    temperatura = models.IntegerField()
    peso = models.IntegerField()
    talla = models.IntegerField()
    masa_corporal = models.IntegerField()
    diagnostico_mc = models.CharField(max_length=15, choices=IMC, default='PesoNormal')
    consulta = models.ForeignKey(Consulta)

    class Meta:
        verbose_name = "Funciones Vitales"
        verbose_name_plural = "Funciones Vitales"

    def __str__(self):
        return self.diagnostico_mc


class Diagnostico(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Diagnostico"
        verbose_name_plural = "Diagnosticos"

    def __str__(self):
        return self.nombre


class DiagnosticoConsulta(models.Model):
    diagnostico = models.ForeignKey(Diagnostico)
    consulta = models.ForeignKey(Consulta)

    class Meta:
        verbose_name = "Diagnostico por Consulta"
        verbose_name_plural = "Diagnostico Consultas"

    def __str__(self):
        return "%s - %s" % (self.diagnostico, self.consulta)


class Producto(models.Model):
    codigo = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio_compra = models.FloatField()

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.descripcion


class UnidadMedida(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"

    def __str__(self):
        return self.nombre


class Tratamiento(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    recomendacion = models.TextField()
    consulta = models.ForeignKey(Consulta)

    class Meta:
        verbose_name = "Tratamiento"
        verbose_name_plural = "Tratamientos"

    def __str__(self):
        return "%s" % self.fecha


class DetalleReceta(models.Model):
    precio_venta = models.FloatField(blank=True, null=True)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField(blank=True, null=True)
    presentacion = models.ForeignKey(UnidadMedida)
    importe = models.FloatField(blank=True, null=True)
    dosis = models.IntegerField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    tratamiento = models.ForeignKey(Tratamiento)

    class Meta:
        verbose_name = "Detalle de Receta"
        verbose_name_plural = "Detalles de Receta"

    def __str__(self):
        return self.producto.descripcion


class Periodo(models.Model):
    ciclo = models.CharField(unique=True, max_length=10)
    fecha = models.DateField()

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

    def __str__(self):
        return "%s" % self.ciclo


class Laboratorio(models.Model):
    hemoglobina = models.IntegerField()
    endocritos = models.IntegerField()
    globulos_rojos = models.IntegerField()
    globulos_blancos = models.IntegerField()
    tipo_sangre = models.CharField(max_length=10)
    periodo = models.ForeignKey(Periodo)
    historia = models.ForeignKey(Historia)

    class Meta:
        verbose_name = "Prueba de Laboratorio"
        verbose_name_plural = "Pruebas de Laboratorio"

    def __unicode__(self):
        return self.hemoglobina


class ConsultaEmergencia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    historia = models.ForeignKey(Historia)

    class Meta:
        verbose_name = "Consulta por Emergencia"
        verbose_name_plural = "Consultas por Emergencia"

    def __str__(self):
        return self.historia.nombres


class ReporteAtencion(models.Model):
    pacientes = models.ForeignKey(Consulta)
    mes = models.IntegerField()
    dia = models.IntegerField()
