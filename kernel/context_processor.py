# myapp/context_processors.py

from django.urls import resolve, reverse

def breadcrumb(request):
    # Construir el breadcrumb
    breadcrumb = []

    # Agregar el enlace de inicio
    breadcrumb.append(('Home', reverse('admin_main_page')))

    # Obtener la ruta de la URL actual
    path = request.path

    # Obtener la lista de partes de la ruta
    path_parts = path.strip('/').split('/')

    # Iterar sobre las partes de la ruta y agregarlas al breadcrumb
    current_path = ''
    for part in path_parts:
        current_path += '/' + part
        # Resolver la ruta actual para obtener el nombre de la vista y el argumento
        try:
            resolved = resolve(current_path)
            view_name = resolved.view_name
            breadcrumb.append((view_name, current_path))
        except:
            print(f"Error: No se pudo resolver la ruta: {current_path}")

    return {'breadcrumb_dict': breadcrumb}
