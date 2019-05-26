from model_utils.models import TimeStampedModel
from safedelete.models import SafeDeleteModel


class BaseModel(SafeDeleteModel, TimeStampedModel):
    class Meta:
        abstract = True

    def get_str(self, *args):
        return ', '.join(map(str, args))
