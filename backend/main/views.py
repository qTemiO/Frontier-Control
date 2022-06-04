from django.http import HttpResponse, JsonResponse

from loguru import logger

from rest_framework.views import APIView

from .apps import MainConfig

class ComplexView(APIView):

    def get(self, request, query):
        logger.success(query)
        if not query: return HttpResponse(status=404)
        predict = MainConfig.predict(query)

        results = []

        return JsonResponse({'data': results})