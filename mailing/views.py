
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from mailing.serializer import MailingSerializer


class Mailing(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        exit()
        is_valid = Validate(request.data).validate_body()
        if is_valid[0]:
            text = """
                    Nombre y apellidos: {0}\n
                    Número de teléfono: {1}\n
                    Dirección de correo: {2}\n\n
                    Texto:\n
                    {3}
                    """.format(
                request.data["name"], request.data["number"], request.data["address"], request.data["text"])
            try:
                send_mail(
                    'Contacto web emiliadiaz.com',
                    text,
                    'info@emiliadiaz.com',
                    ['emiliadiaz@emiliadiaz.com'],
                    fail_silently=False,
                )
                serializer = MailingSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return JsonResponse({"Success": is_valid[1]}, safe=False, status=status.HTTP_200_OK)
            except Exception as e:
                return JsonResponse(
                    {"Error en el mail": "{0}".format(e)},
                    safe=False,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return JsonResponse({"Error": is_valid[1]}, safe=False, status=status.HTTP_400_BAD_REQUEST)


class Validate:
    def __init__(self, data):
        self.body = data
        self.keys_list = ["name", "number", "address", "text", "lopd_check"]

    def validate_body(self):
        for key in self.keys_list:
            if key not in self.body:
                return False, "Missing key in form, {0}".format(key)
            if self.body[key] is None or self.body[key] == "":
                return False, "El campo {0}, no puede ir vacío".format(key)
            if key == "lopd_check":
                if self.body[key] is False or self.body[key] is None:
                    return False, "Acepta la política de privacidad y condiciones de uso"
        return True, "Success"
