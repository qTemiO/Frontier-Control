from django.apps import AppConfig

from filter.apps import FilterUserConfig
from classificator.apps import ClassificatorConfig

from loguru import logger

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def predict(query):
        df_res = ClassificatorConfig.df_res
        logreg = ClassificatorConfig.logreg

        logger.debug(df_res)

        clf_prediction = ClassificatorConfig.predict(query, df_res, logreg)
        vectorize_prediction = FilterUserConfig.predict(query, FilterUserConfig.tfidf_mat, FilterUserConfig.df, FilterUserConfig.vectorizer)

        logger.debug(clf_prediction)
        logger.debug(vectorize_prediction)

    logger.success('Main is ready!')