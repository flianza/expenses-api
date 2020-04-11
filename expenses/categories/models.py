from django_extensions.db import models as extension_models


class Category(extension_models.TitleDescriptionModel):
    def __str__(self):
        return self.title

