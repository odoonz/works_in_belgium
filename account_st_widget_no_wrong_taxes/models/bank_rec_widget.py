# Copyright 2024 Graeme Gellatly
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class BankRecWidgetLine(models.Model):

    _inherit = "bank.rec.widget"

    form_tax_ids = fields.Many2many(
        comodel_name='account.tax',
        domain="[('company_id', '=', company_id)]",
    )
