from odoo import fields, models , api , _
class StockMove(models.Model):
    _inherit = 'stock.move'
    solicitud_production_line = fields.Many2one('solicitud.production.line',string="SM")
    solicitud_production = fields.Many2one('solicitud.production',related='solicitud_production_line.order_id')
    stage_id = fields.Many2one('stage.mrpline', string="Etapa")