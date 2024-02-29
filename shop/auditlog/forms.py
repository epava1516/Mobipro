# forms.py
from django import forms

class AuditLogFilterForm(forms.Form):
    MODEL_CHOICES = [
        ('', 'Todos'),  # Opción para mostrar todos los modelos
        # Agrega opciones para cada modelo
    ]

    ACTION_CHOICES = [
        ('', 'Todas'),  # Opción para mostrar todas las acciones
        # Agrega opciones para cada tipo de acción
    ]

    # Define los campos del formulario para el filtrado y el ordenamiento
    model_name = forms.ChoiceField(choices=MODEL_CHOICES, required=False)
    action = forms.ChoiceField(choices=ACTION_CHOICES, required=False)
    user = forms.CharField(required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    order_by = forms.ChoiceField(choices=[('model_name', 'Modelo (A-Z)'),
                                          ('-model_name', 'Modelo (Z-A)'),
                                          ('action', 'Acción (A-Z)'),
                                          ('-action', 'Acción (Z-A)'),
                                          ('user', 'Usuario (A-Z)'),
                                          ('-user', 'Usuario (Z-A)'),
                                          ('timestamp', 'Fecha (Más reciente)'),
                                          ('-timestamp', 'Fecha (Menos reciente)')],
                                  required=False)
