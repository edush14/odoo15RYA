from odoo import fields, models , api , _
class StockMove(models.Model):
    _inherit = 'stock.move'
    solicitud_production = fields.Many2one('solicitud.production',string="SM")