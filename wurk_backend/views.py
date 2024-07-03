from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError


def health_check(request):
    db_conn = connections['default']
    try:
        db_conn.cursor()
    except OperationalError:
        return JsonResponse({'status': 'healthy', 'database': 'unreachable'}, status=500)

    return JsonResponse({'status': 'healthy', 'database': 'reachable'}, status=200)
