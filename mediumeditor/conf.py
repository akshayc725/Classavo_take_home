from django.conf import settings  # noqa
from appconf import AppConf


class MediumEditorConf(AppConf):
    THEME = 'mani'
    OPTIONS = {
        'toolbar': {
            'static': True,
            'buttons': [
                'bold',
                'italic',
                'underline',
                'strikethrough',
                'subscript',
                'superscript',
                'anchor',
                'quote',
                'pre',
                'orderedlist',
                'unorderedlist',
                'indent',
                'outdent',
                'justifyLeft',
                'justifyCenter',
                'justifyRight',
                'justifyFull',
                'h1',
                'h2',
                'h3',
                
            ]
        }
    }

    class Meta:
        prefix = 'medium_editor'
