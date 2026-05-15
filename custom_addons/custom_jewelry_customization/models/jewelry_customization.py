# -*- coding: utf-8 -*-
from odoo import fields, models


class CustomJewelryCustomization(models.Model):
    _name = "custom.jewelry.customization"
    _description = "Solicitud de personalización de joya"
    _order = "request_date desc"

    name = fields.Char(
        string="Referencia",
        required=True,
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Cliente",
        required=True,
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto base",
    )
    request_date = fields.Date(
        string="Fecha de solicitud",
        default=fields.Date.context_today,
        required=True,
    )
    customization_type = fields.Selection(
        [
            ("engraving", "Grabado"),
            ("size_adjustment", "Ajuste de talla"),
            ("material_change", "Cambio de material"),
            ("stone_selection", "Selección de piedra"),
            ("unique_design", "Diseño único"),
            ("other", "Otro"),
        ],
        string="Tipo de personalización",
        default="unique_design",
        required=True,
    )
    material = fields.Selection(
        [
            ("gold", "Oro"),
            ("silver", "Plata"),
            ("steel", "Acero"),
            ("gemstone", "Piedra preciosa"),
            ("other", "Otro"),
        ],
        string="Material",
    )
    size_or_measure = fields.Char(
        string="Talla o medida",
    )
    state = fields.Selection(
        [
            ("draft", "Borrador"),
            ("review", "En revisión"),
            ("approved", "Aprobada"),
            ("in_production", "En producción"),
            ("done", "Finalizada"),
            ("cancelled", "Cancelada"),
        ],
        string="Estado",
        default="draft",
        required=True,
    )
    description = fields.Text(
        string="Descripción",
    )