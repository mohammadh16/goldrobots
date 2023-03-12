from modeltranslation.translator import TranslationOptions,register
from .models import Contract

@register(Contract)
class ContractTranslationOptions(TranslationOptions):
    fields =['name','minimum_duration','minimum_deposit']
