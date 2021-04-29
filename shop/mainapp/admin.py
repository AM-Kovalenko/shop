from PIL import Image
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from .models import *

from django.utils.safestring import mark_safe

class NotebookAdminForm(ModelForm):

    def __init__(self, * args, **kwargs):
        super().__init__(* args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """ <span style="color:red; font-size:14px;"> При загрузке изображения с разрешением больше {}х{} оно 
            будет обрезано </span'
            """.format(
                *Product.MAX_RESOLUTION
            )
        )

# Проверка соответствия минимального рпзмера изображения
#     def clean_image(self):
#         image = self.cleaned_data['image']
#         img = Image.open(image)
#         min_height, min_width = Product.MIN_RESOLUTION
#         max_height, max_width = Product.MAX_RESOLUTION
#         if image.size > Product.MAX_IMAGE_SIZE:
#             raise ValidationError('Размер изображения не должен превышать 3МБ')
#         if img.height < min_height or min_width<min_width:
#             raise ValidationError('Разрешение изображение меньше минимального!')
#         if img.height > max_height or min_width > max_width:
#             raise ValidationError('Разрешение изображение больше максимального!')
#         return image

# Жесткое ограничение привязки к категории . Для выбора только одной каткгории в админке (урок5)
class NotebookAdmin(admin.ModelAdmin):

    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



# Регистрация

admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Engines)
