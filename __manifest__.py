{
    'name': "Game Core",
    'author': "Samuel Amat, Javier Vicedo",
    'version': '1.0',
    'summary': 'Módulo que permite gestionar las aplicaciones desarrolladas por la empresa Game Core.',
    'Description': 'Módulo que permite gestionar las aplicaciones desarrolladas por la empresa Game Core. ',

    'category': 'Generic/Modules/Others',
    'website': 'https://gamecoreapp.wordpress.com',
    'depends': ['base'],
    'application': True,
    'installable': True,

    # data files always loaded at installation
    'data': ['security/ir.model.access.csv',
			 'views/game_core_view.xml',
			],
}
