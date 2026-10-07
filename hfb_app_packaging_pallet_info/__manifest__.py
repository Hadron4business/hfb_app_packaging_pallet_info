# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=0 shiftwidth=4 smarttab expandtab fileformat=unix
#################################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2017-2026 Hadron for Business sp. z o.o. (http://hadronforbusiness.com)
#
# This program is proprietary software, licensed under the Odoo Proprietary
# License v1.0 (OPL-1). Its use is governed by the Odoo Apps terms available
# at https://www.odoo.com/documentation/user/legal/licenses.html and the
# license agreement accepted at purchase / installation.
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the
# Software or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in
# all copies or substantial portions of the Software.
#
#################################################################################
{
    'name': "Packaging Pallet Info",
    'summary': "Pallet data on product packagings: pallet type, layers, units per layer, height and gross weight",
    'description': """
Packaging Pallet Info
=====================

Warehouses, carriers and customers ask the same questions about every
product: how does it sit on a pallet, how many layers, how many units per
layer, how tall and how heavy is the full pallet?

This app adds the answers to Odoo's product packagings. For any packaging
(for example "Pallet" or "Carton") you can record the pallet type (with its
dimensions), the number of layers, the units per layer, the pallet height
and the gross pallet weight. The units on a full pallet are calculated for
you. Pallet types are kept in a small list under Inventory > Configuration.
""",
    'version': "18.0.1.0.1",
    'author': "Hadron for Business sp. z o.o.",
    'website': "http://hadronforbusiness.com",
    'license': "OPL-1",
    'category': "Inventory/Inventory",
    'depends': [
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/pallet_type_data.xml',
        'views/pallet_type_views.xml',
        'views/product_packaging_views.xml',
    ],
    'images': [
        'static/description/banner_screenshot.png',
    ],
    'installable': True,
    'application': False,
}
