# -*- coding: utf-8 -*-

from odoo import models, fields, api


class examen3(models.Model):
    _name = 'examen3.detalle'
    _description = 'Detalle de Facturas'

    id_factura = fields.Many2one("examen3.facturas", "factura")
    id_producto = fields.Many2one("examen.productos", "productos")
    cantidad = fields.Integer(string= "Cantidad", default = 1)