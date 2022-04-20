from odoo import fields, models , api , _
from odoo.tools import float_compare, float_round, float_is_zero, OrderedSet
class StockMove(models.Model):
    _inherit = 'stock.move'
    solicitud_production_line = fields.Many2one('solicitud.production.line',string="SM")
    solicitud_production = fields.Many2one('solicitud.production',related='solicitud_production_line.order_id')
    stage_id = fields.Many2one('stage.mrpline', string="Etapa")
    #should_consume_qty_js = fields.Float('Quantity To Consume', compute='_compute_should_consume_qty_js',
    #                                  digits='Product Unit of Measure')
    @api.depends('raw_material_production_id.qty_producing', 'product_uom_qty', 'product_uom')
    def _compute_should_consume_qty(self):
        for move in self:
            #mo = move.raw_material_production_id
            #if not mo or not move.product_uom:
            if not move.product_uom:
                move.should_consume_qty = 0
                continue
            move.should_consume_qty = float_round((mo.qty_producing - mo.qty_produced) * move.unit_factor,
                                                  precision_rounding=move.product_uom.rounding)

