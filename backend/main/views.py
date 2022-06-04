from django.http import HttpResponse, JsonResponse

from loguru import logger

from rest_framework.views import APIView

from .apps import MainConfig
from filter.apps import FilterConfig

class ComplexView(APIView):

    def get(self, request, query):
        logger.success(query)
        if not query: return HttpResponse(status=404)
        codes = MainConfig.predict(query)

        smezh_df = FilterConfig.VECTOR_FILTER_DATAFRAME.copy(deep=True)

        total_recommends = []
        for text in smezh_df['KOD_TNVED_SPR'].apply(lambda x: str(x)):
            for code in codes:
                if str(code) in text[:len(str(code))]:
                    total_recommends.append(str(text))

        total_data = []
        for recommend in total_recommends:
            if not smezh_df[smezh_df['KOD_TNVED_SPR'] == int(recommend)].empty:
                description = smezh_df[smezh_df['KOD_TNVED_SPR'] == int(recommend)]['OPISANIE_SPR'].values[0]
                total_data.append({
                    'code': recommend,
                    'description': description
                })

        return JsonResponse({'data': total_data})