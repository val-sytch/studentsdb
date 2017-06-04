# from .settings import PORTAL_URL


def students_proc(request):
    URL = request.scheme + '://' + request.get_host()
    return {'PORTAL_URL': URL}
