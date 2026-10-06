# Packaging Pallet Info

Adds pallet data to Odoo's product packagings and a list of pallet types.

## What it does

- **On the packaging** - Pallet type, layers per pallet, units per layer, pallet height and gross weight, stored where the packaging is defined.
- **Units per pallet** - Calculated for you: layers multiplied by units per layer.
- **Pallet types** - A small catalogue with the pallet's width and length. EUR/EPAL and the industrial pallet come ready.
- **In the list too** - All pallet columns can be switched on in the packaging list.
- **Standard Odoo** - Works with Odoo's own packagings. No new product screens to learn.
- **Ready for reports** - Plain fields on the packaging, easy to use in your own reports and labels.

## How to use it

1. Enable packagings: Inventory > Configuration > Settings > Product Packagings (once).
2. Optionally review or add pallet types in Inventory > Configuration > Pallet Types (name, width and length in mm).
3. Open a product, go to the Inventory tab, find the Packaging table and add a row (for example Pallet or Carton). The pallet columns are right in that table.
4. In the row (or in the Pallet section of the packaging form, Inventory > Configuration > Product Packagings) fill in the Pallet Type, Layers per Pallet, Units per Layer, Pallet Height [mm] and Pallet Gross Weight [kg].
5. Units per Pallet is filled in automatically.
6. The columns can be switched off with the column selector if you do not need them.

## Good to know

- The pallet data belongs to one packaging, so a product can have different pallet setups for different packagings.
- Pallet types are shared by all companies. Archive a type you no longer use instead of deleting it.
- Height is in millimetres and weight in kilograms; the app does not convert units.

## Technical

- `models/pallet_type.py` - model `product.pallet.type` (name, width, length, active).
- `models/product_packaging.py` - fields on `product.packaging` and the computed `units_per_pallet`.
- Views extend `product.product_packaging_form_view` and `product.product_packaging_tree_view`.
- Access: read for Inventory users, full access for Inventory administrators.
- Depends on: `stock`.

## Status

Source: client module (Odoo 18); only the pallet part was taken, the pallet type model was renamed and the 'length' spelling fixed. Odoo 17 build.
