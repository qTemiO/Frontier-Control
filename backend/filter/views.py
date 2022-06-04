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

        codes = []
        descriptions = []

        for index, row in prediction.iterrows():
            code =  row['KOD_TNVED_SPR']
            decription = row['OPISANIE_SPR']
            
            codes.append(code)
            descriptions.append(decription)

        top_codes = []
        top_descriptions = []

        

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