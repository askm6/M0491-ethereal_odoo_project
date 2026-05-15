# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re


class ResPartner(models.Model):
    _inherit = 'res.partner'

    linkedin_url = fields.Char(
        string='LinkedIn',
        help='URL del perfil de LinkedIn del contacto. '
             'Ej: https://www.linkedin.com/in/nombre-usuario'
    )
    instagram_url = fields.Char(
        string='Instagram',
        help='URL del perfil de Instagram del contacto. '
             'Ej: https://www.instagram.com/nombre_usuario'
    )

    @api.constrains('linkedin_url')
    def _check_linkedin_url(self):
        for record in self:
            if record.linkedin_url:
                url = record.linkedin_url.strip()
                if not re.match(r'^https?://([\w-]+\.)?linkedin\.com/.+', url, re.IGNORECASE):
                    raise ValidationError(
                        "La dirección de LinkedIn no es válida.\n"
                        "Debe empezar por http:// o https:// y contener 'linkedin.com'.\n"
                        "Ejemplo: https://www.linkedin.com/in/nombre-usuario"
                    )

    @api.constrains('instagram_url')
    def _check_instagram_url(self):
        for record in self:
            if record.instagram_url:
                url = record.instagram_url.strip()
                if not re.match(r'^https?://([\w-]+\.)?instagram\.com/.+', url, re.IGNORECASE):
                    raise ValidationError(
                        "La dirección de Instagram no es válida.\n"
                        "Debe empezar por http:// o https:// y contener 'instagram.com'.\n"
                        "Ejemplo: https://www.instagram.com/nombre_usuario"
                    )
