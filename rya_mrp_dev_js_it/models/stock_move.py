from odoo import fields, models , api , _
from odoo.tools import float_compare, float_round, float_is_zero, OrderedSet
class StockMove(models.Model):
    _inherit = 'stock.move'
    solicitud_production_line = fields.Many2one('solicitud.production.line',string="SM")
    solicitud_production = fields.Many2one('solicitud.production',related='solicitud_production_line.order_id')
    stage_id = fields.Many2one('stage.mrpline', string="Etapa")
    should_consume_qty_store = fields.Float('Quantity To Consume Store',
                                      digits='Product Unit of Measure')
    @api.onchange('product_uom_qty')
    def change_qtyy(self):
        for record in self:
            qty = record.production_id.product_qty
            qty += record.product_uom_qty
            get_lines = self.env['report.mrp_account_enterprise.mrp_cost_structure'].get_lines(record.production_id)
            total_per = get_lines['total_cost'] / qty if qty != 0 else 0
            record.cost_share = total_per




