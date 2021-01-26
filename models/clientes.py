# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Clientes(models.Model):
    _name = 'examen3.clientes'
    _description = 'Clientes'

    dni = fields.Char(string="DNI", size=9)
    name = fields.Char(string="Nombre")
    surname = fields.Char(string="Apellidos")
    telefono = fields.Char(string="Telefono", size = 9)
    email = fields.Char(string="Email")
    foto = fields.Binary()
    facturas = fields.One2many("examen3.facturas","cliente", string="Facturas")

    @api.constrains("email")
    def check_email(self):
        if "@" and "." not in self.email:
            raise ValidationError("El campo Email tiene un formato incorrecto")
    @api.constrains("dni")
    def check_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = int(self.dni[:-1])
        if letras[num%23] != letra:
            raise ValidationError("Error. DNI invalido.")
    
