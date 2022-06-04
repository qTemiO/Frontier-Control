from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView

from loguru import logger

from .apps import ClassificatorConfig

class ClassificatorView(APIView):

    def get(self, request, query):
        logger.success(query)
        if not query: return HttpResponse(status=404)

        df_res = ClassificatorConfig.df_res
        logreg = ClassificatorConfig.logreg

        prediction = ClassificatorConfig.predict(query, df_res, logreg)

        logger.debug(prediction)

        results = []
        autochecker = False
        for index, row in prediction.iterrows():
            if not autochecker:
                if row['predict'] > 0.99: 
                    autochecker=True
                if row['predict'] > 0.01:
                    results.append({'class':str(int(row['class'])), 'probility':row['predict']})

        return JsonResponse({
            'data': results
        })
