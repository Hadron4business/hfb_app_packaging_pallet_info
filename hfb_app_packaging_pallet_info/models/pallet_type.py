# -*- coding: utf-8 -*-
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
"""	@version	18.0.1.0.1
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.06

	Pallet Type
	Catalogue of pallet types (name and base dimensions) that can be chosen on a
	product packaging.
"""
from odoo import fields, models


class ProductPalletType(models.Model):
    _name = 'product.pallet.type'
    _description = "Pallet Type"
    _order = 'name'

    name = fields.Char(string="Pallet Type", required=True, translate=True)
    width = fields.Integer(string="Width [mm]")
    length = fields.Integer(string="Length [mm]")
    active = fields.Boolean(default=True)

#EoF
