# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Clientes(models.Model):
    _name = 'examen3.Clientes'
    _description = 'Clientes'

    dni = fields.Integer(string="DNI",size = 9)
    name = fields.Char(string="Nombre")
    surname = fields.Char(string="Apellidos")
    telefono = fields.Integer(string="Telefono", size=9)
    email = fields.Char(string="Email")

    @api.constrains("telefono")
    def check_phone_length(self):
        if len(self.telefono) < 9 or len(self.telefono) > 9:
            raise ValidationError("El campo Telefono tiene un formato incorrecto")
    @api.constrains("email")
    def check_email(self):
        if "@" not in self.email:
            raise ValidationError("El campo Email tiene un formato incorrecto")
    @api.constrains("dni")
    def check_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = int(self.dni[:-1])
        if letras[num%23] != letra:
            raise ValidationError("El DNI no es correcto.")
    
