# myapp/context_processors.py

from django.urls import resolve, reverse

def breadcrumb(request):
    # Construir el breadcrumb
    breadcrumb = []

    # Obtener la ruta de la URL actual
    path = request.path

    # Obtener la lista de partes de la ruta
    path_parts = path.strip('/').split('/')

    # Iterar sobre las partes de la ruta y agregarlas al breadcrumb
    current_path = ''
    for part in path_parts:
        if part == 'admin':
            current_path += '/' + part
            breadcrumb.append(('Home', current_path))
        else:
            current_path += '/' + part
            breadcrumb.append((part, current_path))

    return {'breadcrumb': breadcrumb}
