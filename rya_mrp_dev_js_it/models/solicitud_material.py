from odoo import fields, models , api , _
class SolicitudProduction(models.Model):
    _name = 'solicitud.production'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()
    mrp_production = fields.Many2one('mrp.production',string="Orden de Produccion",ondelete='restrict')
    state = fields.Selection([('drat','Borrador'),('comfirm','Aprobada')])
    order_line = fields.One2many('solicitud.production.line', 'order_id', string='Order Lines', copy=True)
    date_order = fields.Datetime(string='Order Date', required=True, readonly=True, index=True,
                                 states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False,
                                 default=fields.Datetime.now,
                                 help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.")
    user_id = fields.Many2one(
        'res.users', string='Salesperson', index=True, tracking=2, default=lambda self: self.env.user,
    )
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True,
                                 default=lambda self: self.env.company)
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code(
                    'solicitud.production', sequence_date=seq_date) or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('solicitud.production', sequence_date=seq_date) or _('New')

        result = super(SolicitudProduction, self).create(vals)
        return result

    def fun_aprobar(self):
        self.state = 'comfirm'

class SolicitudProductionLine(models.Model):
    _name = 'solicitud.production.line'
    order_id = fields.Many2one('mrp_production',ondelete='restrict')
    product_id = fields.Many2one('product.product',string="Producto",ondelete='restrict')
    consumed = fields.Float()



