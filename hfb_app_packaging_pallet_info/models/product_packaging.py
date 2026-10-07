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
"""	@version	17.0.1.0.0
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.06

	Pallet data on product packaging
	Adds pallet type, layers per pallet, units per layer, pallet height and
	gross weight to product.packaging, plus the computed number of units on a
	full pallet.
"""
from odoo import api, fields, models


class ProductPackaging(models.Model):
    _inherit = 'product.packaging'

    pallet_type_id = fields.Many2one('product.pallet.type', string="Pallet Type")
    layers_per_pallet = fields.Integer(string="Layers per Pallet")
    units_per_layer = fields.Integer(
        string="Units per Layer",
        help="Number of units of this packaging in one layer of the pallet.",
    )
    units_per_pallet = fields.Integer(
        string="Units per Pallet", compute='_compute_units_per_pallet',
        help="Layers per pallet multiplied by units per layer.",
    )
    pallet_height = fields.Float(string="Pallet Height [mm]")
    pallet_weight_gross = fields.Float(string="Pallet Gross Weight [kg]")

    @api.depends('layers_per_pallet', 'units_per_layer')
    def _compute_units_per_pallet(self):
        for packaging in self:
            packaging.units_per_pallet = packaging.layers_per_pallet * packaging.units_per_layer

#EoF
