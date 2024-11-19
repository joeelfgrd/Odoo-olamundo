# -*- coding: utf-8 -*-

from odoo import models,fields,api



class olamundo(models.Model):
    _name='odoo_olamundo.olamundo'
    _description = "Exemplo de olamundo"

    name = fields.Char(string="Ola mundo")
    outroCampo = fields.Char(string="Outro:")


