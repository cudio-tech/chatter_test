{
    'name': 'Configurable Chatter Position',
    'summary': 'Allows users to configure chatter position on forms',
    'version': '1.1.0',
    'category': 'Productivity',
    'author': 'Odoobeing',
    'depends': [
        'base',
        'web'
    ],
    'data': [
        'views/res_users.xml',
        'views/web.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'ob_chatter_position/static/src/views/form/form_chatter_position.js',
            'ob_chatter_position/static/src/scss/chatter_position.scss'
        ],
        'web.assets_qweb': [
            'ob_chatter_position/static/src/views/form/form_buttons.xml'
        ]
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False
}