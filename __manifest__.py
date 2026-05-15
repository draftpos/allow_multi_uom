{
    'name': 'Multi UoM Pricing',
    'version': '19.0.2.0.0',
    'category': 'Sales',
    'summary': 'Multiple UoMs with different prices per product',
    'description': """
        This module extends Odoo to support multiple Units of Measure (UoM) per product
        with different prices for each UoM integrated directly into pricelist rules.
        
        Features:
        - Enable multiple UoMs per product via pricelist rules
        - Set different sale prices per UoM using standard pricelist system
        - Select any compatible UoM when creating a pricelist rule
        - Barcode support per UoM
        - Auto-update prices in sales orders when UoM changes
    """,
    'author': 'Havano',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'product',
        'uom',
        'sale',
        'sale_management'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_pricelist_item_views.xml',
        'views/product_template_views.xml',
        'views/sale_order_line_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {},
}