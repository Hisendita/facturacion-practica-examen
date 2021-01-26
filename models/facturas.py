# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Facturas(models.Model):
    _name = 'examen3.facturas'
    _description = 'Facturas'

    referencia = fields.Integer(string="Referencia")
    fecha = fields.Datetime(string="Fecha", default=datetime.now())
    cliente = fields.Many2one("examen3.clientes", string="Cliente")
    detalle = fields.One2many("examen3.detalle", "id_factura", string="Factura")
    base = fields.Float(string="Base",store=True)
    iva = fields.Selection(selection=[("0","0"),("7","7"),("15","15"),("21","21")], default="21", string="IVA")
    total = fields.Float(string="Total",store=True)

    @api.depends("iva", "base")
    def calcular_iva(self):
        self.ensure_one()
        self.total = ((self.base * int(self.iva)/100) + self.base)
