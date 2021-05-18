from django import template
from django.utils.safestring import mark_safe
from mainapp.models import Smartphone

register = template.Library()

TABLE_HEAD = """
                <table class="table">
                    <tbody>
             """
TABLE_TAIL = """
                    </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                        <td>{name}</td>
                        <td>{value}</td>
                    </tr>
                """
PRODUCT_SPEC = {
    'notebook': {
        'Дигональ': 'diagonal',
        'Дисплей': 'display',
        'Процессор': 'Processor_freq',
        'ОЗУ': 'ram',
        'Видеокарта': 'video',
        'время работы аккамулятора': 'time_without_charge'
    },
    'smartphone': {
        'Дигональ': 'diagonal',
        'Дисплей': 'display',
        'Разрешение экрана': 'resolution',
        'объем батареии': 'accum_volume',
        'ОЗУ': 'ram',
        'Наличие слота карты памяти': 'sd',
        'Макс объем встр памяти': 'sd_volume_max',
        'Главная камера': 'main_cam_np',
        'Фронтальная камера': 'frontal_cam_np'
    },
    'engines': {
        'Тип топлива': 'fuel_type',
        'Производитель': 'brand_name',
        'Модель': 'model',
        'Мощность': 'power',
        'Объем': 'volume',
        'Масса': 'weight'
    },
    'gearparts': {
        'Масса': 'weight'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Макс объем встр памяти')
        else:
            PRODUCT_SPEC['smartphone']['Макс объем встр памяти'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
