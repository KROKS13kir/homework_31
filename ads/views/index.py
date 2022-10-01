from django.http.response import JsonResponse


def index(request):
    response = {"status": "ok"}
    return JsonResponse(response, status=200)
