from django.apps import AppConfig

from filter.apps import FilterUserConfig, FilterConfig
from classificator.apps import ClassificatorConfig

from loguru import logger

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def predict(query):
        df_res = ClassificatorConfig.df_res
        logreg = ClassificatorConfig.logreg

        clf_prediction = ClassificatorConfig.predict(query, df_res, logreg)
        vectorize_prediction = FilterUserConfig.predict(query, FilterUserConfig.tfidf_mat, FilterUserConfig.VECTOR_USER_FILTER_DATAFRAME, FilterUserConfig.vectorizer)

        classes = []
        autochecker = False
        for index, row in clf_prediction.iterrows():
            if not autochecker:
                if row['predict'] > 0.99: 
                    autochecker=True
                if row['predict'] > 0.01:
                    classes.append(row['class'])
        
        classes_clf = list(set(classes))
        classes_vectors = []
        
        for index, row in vectorize_prediction.iterrows():
            if row['TNVED'] not in classes_vectors:
                classes_vectors.append(row['TNVED'])
        
        codes = []
        for class_ in classes_vectors:
            if class_ in classes_clf:
                codes.append(class_)

        return codes

    logger.success('Main is ready!')