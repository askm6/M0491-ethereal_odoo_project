# -*- coding: utf-8 -*-
{
    "name": "Personalización de joyas",
    "version": "17.0.1.0.0",
    "category": "Customizations",
    "summary": "Gestión de solicitudes de joyas personalizadas",
    "description": """
Personalización de joyas
========================

Módulo personalizado para registrar solicitudes de joyas únicas o
personalizadas dentro del flujo de trabajo de ETHEREAL.

Permite asociar cada solicitud a un cliente, producto base, tipo de
personalización, material, medida y estado del proceso.
    """,
    "author": "ERP Solutions",
    "depends": ["base", "product"],
    "data": [
        "security/ir.model.access.csv",
        "views/jewelry_customization_views.xml",
        "views/menu_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}