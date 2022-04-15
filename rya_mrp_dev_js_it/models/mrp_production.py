from odoo import fields, models , api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    
    @api.onchange('qty_producing', 'lot_producing_id')
    def _onchange_producing(self):
        if self.state not in ['confirmed','progress','to_close']:
            self._set_qty_producing()

