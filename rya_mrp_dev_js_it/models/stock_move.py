from odoo import fields, models , api , _
class StockMove(models.Model):
    _inherit = 'stock.move'
    solicitud_production = fields.Many2one('solicitud.production',string="SM")
    stage_id = fields.Many2one('stage.mrpline', string="Etapa")