from odoo import fields, models

class Game_Core(models.Model):
    _name: "gamecore.model"
    _description: "Aplicación que permite gestionar las aplicaciones desarrolladas por la empresa Game Core"

    #Campos básicos
    name = fields.Char('Nombre', required=True)
