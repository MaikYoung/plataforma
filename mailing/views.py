
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class Mailing(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
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
            send_mail(
                'Contacto web emiliadiaz.com',
                text,
                'info@emiliadiaz.com',
                ['emiliadiaz@emiliadiaz.com'],
                fail_silently=False,
            )
            return JsonResponse({"Success": is_valid[1]}, safe=True, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"Error": is_valid[1]}, safe=True, status=status.HTTP_400_BAD_REQUEST)


class Validate:
    def __init__(self, data):
        self.body = data
        self.keys_list = ["name", "number", "address", "text"]

    def validate_body(self):
        for key in self.keys_list:
            if key not in self.body:
                return False, "Missing key in form, {0}".format(key)
            if self.body[key] is None or self.body[key] == "":
                return False, "El campo {0}, no puede ir vacío".format(key)
        return True, "Success"
