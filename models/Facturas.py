# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Facturas(models.Model):
    _name = 'examen3.facturas'
    _description = 'Facturas'

    referencia = fields.Integer(string="Referencia")
    fecha = fields.Datetime(string="Fecha", default=datetime.now())
    cliente = fields.Many2many(string="Cliente")
    base = fields.Float(string="Base", compute="total_productos",store=True)
    iva = fields.Selection([("1","0%"),("2","7%"),("3","15%"),("4","21%")],default="21%")
    total = fields.Float(string="Total",compute="precio_total",store=True)