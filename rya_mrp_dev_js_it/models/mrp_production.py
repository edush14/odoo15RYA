from odoo import fields, models , api
class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    plantilla_ratio = fields.Many2one('plantilla.ratios',string="Plantilla",ondelete='restrict')
    ratios = fields.One2many('mrp.ratios.lines','order_id')
    total_amount_ratios = fields.Float(compute="get_total_amount_ratios",store=True)
    @api.depends('ratios','ratios.price_unit','ratios.quantity','ratios.price_total')
    def get_total_amount_ratios(self):
        for record in self:
            total = 0
            for r in record.ratios:
                total += r.price_total
            record.total_amount_ratios = total

    @api.onchange('qty_producing', 'lot_producing_id')
    def _onchange_producing(self):
        if self.state not in ['confirmed','progress','to_close']:
            self._set_qty_producing()

    def _get_move_raw_values(self, product_id, product_uom_qty, product_uom, operation_id=False, bom_line=False):
        res = super(MrpProduction, self)._get_move_raw_values(product_id, product_uom_qty, product_uom, operation_id, bom_line)
        if bom_line:
            res['stage_id'] = bom_line.stage_id.id
        return res

    @api.model
    def default_get(self, fields):
        res = super(MrpProduction, self).default_get(fields)
        plantilla_default = self.env['plantilla.ratios'].search([('is_default', '=', True)])
        if plantilla_default:
            res.update({'plantilla_ratio': plantilla_default[0].id})
        return res
    @api.onchange('plantilla_ratio')
    def change_plantilla(self):
        for record in self:
            if record.plantilla_ratio:
                record.ratios.unlink()
                lines = record.plantilla_ratio.order_line
                for l in lines:
                    record.ratios += self.env['mrp.ratios.lines'].new({
                        'name': l.name ,
                        'price_unit': l.price_unit
                    })


class PlantillaRatiosLine(models.Model):
    _name = 'mrp.ratios.lines'
    name = fields.Char(required=True)
    quantity = fields.Float(string="Cantidad")
    price_unit = fields.Float(string="Costo Unitario")
    price_total = fields.Float(string="Precio Total")
    order_id = fields.Many2one('mrp.production', ondelete='restrict')
    @api.depends('quantity','price_unit')
    def change_total(self):
        for record in self:
            record.price_total = record.quantity * record.price_unit