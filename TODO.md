# TODO - allow_multi_uom

- [x] Clean and finalize `models/product_template.py`
- [x] Clean and finalize `models/product_pricelist_item.py`
- [x] Rework `models/sale_order_line.py` for safe UoM-based pricing
- [x] Update `views/product_template_views.xml` (General Info + Prices list columns)
- [x] Update `views/product_pricelist_item_views.xml` (form and tree)
- [x] Update `views/sale_order_line_views.xml` (editable product_uom_id)
- [x] Validate `security/ir.model.access.csv` format
- [x] Mark all tasks complete

## New requested enhancements
- [x] Add `strict_uom_tracking` on `product.template`
- [x] Make `allow_multi_uom` enabled by default
- [x] Improve product form UI with a dedicated "Multi UoM Settings" section
- [x] Update SO line onchange behavior for strict tracking mode
- [ ] Upgrade module and verify strict/non-strict behavior
