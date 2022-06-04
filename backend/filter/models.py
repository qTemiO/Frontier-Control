from django.db import models

class UserDf(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField()
    preprocessed_description = models.TextField()

    def __repr__(self) -> str:
        return self.code

class FzDf(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField()
    preprocessed_description = models.TextField()

    def __repr__(self) -> str:
        return self.code
