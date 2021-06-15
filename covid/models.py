from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Genome(models.Model):
    ## By default, Django gives each model an auto-incrementing primary key with the type specified per app in AppConfig.default_auto_field
    ## or globally in the DEFAULT_AUTO_FIELD setting.
    Accession = models.CharField(max_length=8, unique=True, validators = [MinLengthValidator(8), MaxLengthValidator(8)])
    Country = models.CharField(max_length=32 ) ## other fields might be empty or null
    Host = models.CharField(max_length=32 )
    CollectionDate = models.DateField(verbose_name = "Collection Date")
    FastaSequence = models.TextField(verbose_name = "Fasta Sequence")

    def __str__(self):
        return self.Accession