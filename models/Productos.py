# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Productos(models.Model):
    _name = 'examen3.productos'
    _description = 'Productos'
    
    name = fields.Char(string="Nombre del producto")
    desc = fields.Html(string="Descripcion del producto")
    pvp = fields.Float(string="Precio de venta")
    cantidad = fields.Integer(string="Cantidad", default=1)
    detalle = fields.One2many("examen3.Detalle", "id_productos", "Facturas")
    
    
