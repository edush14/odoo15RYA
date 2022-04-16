from odoo import fields, models , api , _
class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'
    stage_id = fields.Many2one('stage.mrpline',string="Etapa")

class StageMrpBomLine(models.Model):
    _name = 'stage.mrpline'
    name = fields.Char()