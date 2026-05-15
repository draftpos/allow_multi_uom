from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    allow_multi_uom = fields.Boolean(
        string='Enable Multi UoM Pricing',
        default=True,
        help="Enable to set different prices for different Units of Measure in pricelist rules.",
    )
    strict_uom_tracking = fields.Boolean(
        string='Allow Strict UoM Tracking on Sales Lines',
        default=False,
        help="If enabled, users must explicitly select the Unit of Measure on sales order lines for this product.",
    )
