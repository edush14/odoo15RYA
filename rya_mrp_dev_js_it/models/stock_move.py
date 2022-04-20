from odoo import fields, models , api , _
from odoo.tools import float_compare, float_round, float_is_zero, OrderedSet
class StockMove(models.Model):
    _inherit = 'stock.move'
    solicitud_production_line = fields.Many2one('solicitud.production.line',string="SM")
    solicitud_production = fields.Many2one('solicitud.production',related='solicitud_production_line.order_id')
    stage_id = fields.Many2one('stage.mrpline', string="Etapa")
    should_consume_qty_store = fields.Float('Quantity To Consume Store',
                                      digits='Product Unit of Measure')
    @api.onchange('should_consume_qty','raw_material_production_id.qty_producing')
    def change_store(self):
        for record in self:
            record._compute_should_consume_qty()
            record.should_consume_qty_store = record.should_consume_qty


