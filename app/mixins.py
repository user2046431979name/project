from django.db.models import *
class TimeStampMixin(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)
    class Meta:
        abstract  = True

