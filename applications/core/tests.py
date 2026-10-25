from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from applications.core.models import Especialidad, TipoSangre
from proy_clinico.util import valida_cedula


class ValidaCedulaTests(TestCase):
    def test_cedula_valida(self):
        """Una cédula ecuatoriana correcta no lanza error"""
        valida_cedula("1710034065")

    def test_cedula_con_letras(self):
        with self.assertRaises(ValidationError):
            valida_cedula("17100340AB")

    def test_cedula_longitud_incorrecta(self):
        with self.assertRaises(ValidationError):
            valida_cedula("12345")

    def test_cedula_digito_verificador_incorrecto(self):
        with self.assertRaises(ValidationError):
            valida_cedula("1710034066")


class ModelosCoreTests(TestCase):
    def test_crear_tipo_sangre(self):
        tipo = TipoSangre.objects.create(tipo="O+", descripcion="O positivo")
        self.assertEqual(str(tipo), "O+")

    def test_especialidad_activa_por_defecto(self):
        especialidad = Especialidad.objects.create(nombre="Cardiología")
        self.assertTrue(especialidad.activo)
        self.assertEqual(str(especialidad), "Cardiología")


class AccesoTests(TestCase):
    def test_lista_pacientes_requiere_login(self):
        """Sin iniciar sesión la lista de pacientes redirige al login"""
        respuesta = self.client.get(reverse("core:paciente_list"))
        self.assertEqual(respuesta.status_code, 302)
