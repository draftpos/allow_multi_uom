from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    uom_id = fields.Many2one(
        'uom.uom',
        string='Unit of Measure',
        help="Specific UoM for this price rule. Leave empty for product's default UoM.",
    )
    uom_barcode = fields.Char(
        string='UoM Barcode',
        help="Barcode for this specific UoM.",
    )

    @api.constrains('uom_id', 'product_tmpl_id', 'product_id')
    def _check_uom_compatibility(self):
        for rule in self:
            if not rule.uom_id:
                continue

            product = rule.product_id or rule.product_tmpl_id.product_variant_id
            if not product:
                continue

            rule_ref_uom = rule.uom_id.relative_uom_id or rule.uom_id
            product_ref_uom = product.uom_id.relative_uom_id or product.uom_id
            if rule_ref_uom != product_ref_uom:
                raise ValidationError(_(
                    "The UoM '%(uom)s' is not compatible with this product. "
                    "Please select a UoM from the same category as '%(default_uom)s'.",
                    uom=rule.uom_id.display_name,
                    default_uom=product.uom_id.display_name,
                ))
