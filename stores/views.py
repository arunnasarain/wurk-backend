from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Store
from .serializers import StoreSerializer



@api_view(['GET'])
def get_one_store(request):
    try:
        store = Store.objects.first()
        if not store:
            return JsonResponse({'error': 'No store records found.'}, status=404)

        serializer = StoreSerializer(store)
        return JsonResponse(serializer.data, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
