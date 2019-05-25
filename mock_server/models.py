from model_utils.models import TimeStampedModel
from safedelete.models import SafeDeleteModel


class BaseModel(SafeDeleteModel, TimeStampedModel):
    class Meta:
        abstract = True


# TODO: https://django-rest-framework-serializer-extensions.readthedocs.io/en/latest/usage-hashids/
