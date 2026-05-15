# -*- coding: utf-8 -*-
{
    'name': 'Contactos - Redes Sociales (LinkedIn e Instagram)',
    'version': '17.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Añade campos de LinkedIn e Instagram a la ficha de contactos',
    'description': """
Módulo Contactos - Redes Sociales
==================================
Añade dos campos nuevos a la ficha de contactos (res.partner):
    * Dirección de LinkedIn
    * Dirección de Instagram

Los campos aparecen en una nueva pestaña "Redes Sociales" dentro
del formulario del contacto, e incluyen un botón para abrir el
perfil directamente en el navegador.
    """,
    'author': 'HalfMoon',
    'depends': ['contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
