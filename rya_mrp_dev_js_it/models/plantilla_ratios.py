from odoo import fields, models , api , _
class PlantillaRatios(models.Model):
    _name = 'plantilla.ratios'
    name  = fields.Char()
    is_default = fields.Boolean()
    order_line = fields.One2many('plantilla.ratios.line', 'order_id', string='Order Lines', copy=True)

class PlantillaRatiosLine(models.Model):
    _name = 'plantilla.ratios.line'
    name = fields.Char()
    price_unit = fields.Float(string="Costo Unitario")
    order_id = fields.Many2one('plantilla.ratios', ondelete='restrict')
