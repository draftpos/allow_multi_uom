# Multi UoM Pricing for Odoo 19

[![Version](https://img.shields.io/badge/version-19.0.1.0.0-blue.svg)](https://github.com/draftpos/allow_multi_uom)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Odoo](https://img.shields.io/badge/Odoo-19-purple.svg)](https://www.odoo.com)

## 📋 Overview

**Multi UoM Pricing** is a powerful Odoo 19 module that extends the standard pricing system to support multiple Units of Measure (UoM) per product with unique pricing and barcodes for each UoM. This module integrates seamlessly with Odoo's native pricelist system, allowing you to define different prices for different units of measure directly in the pricelist rules.

### 🎯 Key Features

- ✅ **Multiple UoM per Product** - Define different units of measure for the same product
- ✅ **UoM-Specific Pricing** - Set unique sale prices for each unit of measure using pricelist rules
- ✅ **Multiple Barcodes** - Assign different barcodes to different UoMs (GS1 compatible)
- ✅ **Strict UoM Tracking** - Enforce UoM selection on sales orders
- ✅ **Automatic Price Updates** - Prices update instantly when UoM changes in sales orders
- ✅ **No Popup Warnings** - Clean, seamless user experience without annoying popups
- ✅ **Full Pricelist Integration** - Works with existing pricelist rules, discounts, and formulas

## 🚀 Installation

### Prerequisites
- Odoo 19 (Community or Enterprise)
- Python 3.12+
- PostgreSQL 15+

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/draftpos/allow_multi_uom.git
cd allow_multi_uom
git checkout dev
