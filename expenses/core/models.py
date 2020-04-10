from django_extensions.db import models as extension_models


class Currency(extension_models.TitleDescriptionModel):
    def __str__(self):
        return self.title

