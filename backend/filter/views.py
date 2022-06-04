import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView

from .apps import (
    FilterConfig,
    FilterUserConfig,
)

from loguru import logger

# Create your views here.
def dataView(request):
    data = FilterConfig.VECTOR_FILTER_DATAFRAME
    return JsonResponse({
        'data':data.__repr__()
        })

class recommendFZ(APIView):

    def get(self, request, query):
        tfidf_mat = FilterConfig.tfidf_mat
        vectorizer = FilterConfig.vectorizer
        df = FilterConfig.VECTOR_FILTER_DATAFRAME

        prediction = FilterConfig.predict(query, tfidf_mat=tfidf_mat, df=df, vectorizer=vectorizer)

        results = []
        for index, row in prediction.iterrows():
            data = {
                'code': row['KOD_TNVED_SPR'],
                'description': row['OPISANIE_SPR']
            }
            results.append(data)

        logger.debug(prediction)

        return JsonResponse({
            'data': results
            })

    def post(self, request):
        body = json.loads(request.body)
        recommending_string = body['data']

        tfidf_mat = FilterConfig.tfidf_mat
        vectorizer = FilterConfig.vectorizer
        df = FilterConfig.VECTOR_FILTER_DATAFRAME

        prediction = FilterConfig.predict(recommending_string, tfidf_mat=tfidf_mat, df=df, vectorizer=vectorizer)

        logger.debug(prediction)

        results = []

        for index, row in prediction.iterrows():
            data = {
                'code': row['TNVED'],
                'description': row['OPISANIE_SPR']
            }
            results.append(data)

        results.append(data)

        return JsonResponse({
            'data': results
            })

class recommendUser(APIView):

    def get(self, request, query):
        logger.success(query)
        tfidf_mat = FilterUserConfig.tfidf_mat
        vectorizer = FilterUserConfig.vectorizer
        df = FilterUserConfig.VECTOR_USER_FILTER_DATAFRAME

        prediction = FilterUserConfig.predict(query, tfidf_mat=tfidf_mat, df=df, vectorizer=vectorizer)
        logger.debug(prediction)

        codes = []
        for index, row in prediction.iterrows():
            code =  row['TNVED']  
            if len(codes) < 3 and code not in codes:
                codes.append(int(code))
                
        smezh_df = FilterConfig.VECTOR_FILTER_DATAFRAME

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

        logger.debug(total_data)

        return JsonResponse({
            'data': total_data
            })

    def post(self, request):
        body = json.loads(request.body)
        recommending_string = body['data']

        tfidf_mat = FilterUserConfig.tfidf_mat
        vectorizer = FilterUserConfig.vectorizer
        df = FilterUserConfig.VECTOR_USER_FILTER_DATAFRAME

        prediction = FilterUserConfig.predict(recommending_string, tfidf_mat=tfidf_mat, df=df, vectorizer=vectorizer)

        results = []
        for index, row in prediction.iterrows():
            data = {
                'code': row['TNVED'],
                'description': row['OPISANIE_SPR']
            }
            results.append(data)

        logger.debug(prediction)

        return JsonResponse({
            'data': results
            })