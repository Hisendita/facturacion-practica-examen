# -*- coding: utf-8 -*-

from odoo import models, fields, api


class examen3(models.Model):
    _name = 'examen3.Detalle'
    _description = 'Detalle de Facturas'

    id_factura = fields.Many2one("examen3.Facturas", "Factura")
    id_producto = fields.Many2one("examen.Productos", "Productos")
    cantidad = fields.Integer(string= "Cantidad", default = 1)