# Copyright 2024 Graeme Gellatly
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class AccountReconcileModelLine(models.Model):

    _inherit = "account.reconcile.model"

    def _apply_lines_for_bank_widget(self, residual_amount_currency, partner, st_line):
        self = self.with_context(residual_amount_currency=residual_amount_currency)
        return super()._apply_lines_for_bank_widget(residual_amount_currency, partner, st_line)


class AccountReconcileModelLine(models.Model):
    _inherit = "account.reconcile.model.line"

    def _apply_in_bank_widget(self, residual_amount_currency, partner, st_line):
        """ Adjust residual_amount_currency to the st_line amount_residual so non Belgians
        can just assign simple percentages and have things allocate normally without
        need of university math.

        :param residual_amount_currency:    The current balance expressed in the statement line's currency.
        :param partner:                     The partner to be linked to the journal item.
        :param st_line:                     The statement line mounted inside the bank reconciliation widget.
        :return:                            A python dictionary.
        """
        self.ensure_one()
        if self.amount_type == 'percentage_st_line' and self._context.get('residual_amount_currency', 0.0):
            residual_amount_currency = self._context.get('residual_amount_currency', 0.0)
        return super()._apply_in_bank_widget(residual_amount_currency, partner, st_line)
