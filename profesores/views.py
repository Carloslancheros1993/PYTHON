from django.http import HttpResponse


def vista_profesores(request):
    html = '<html><body>Hola desde profesores</body></html>'
    return HttpResponse(html)


