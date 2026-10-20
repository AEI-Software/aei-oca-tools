# © 2023 ooops404
# Copyright 2023 Simone Rubino - Aion Tech
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends("invoice_line_ids.agent_ids.amount", "line_ids.agent_ids.amount")
    def _compute_commission_total(self):
        for record in self:
            record.commission_total = sum(
                record.invoice_line_ids.mapped("agent_ids.amount")
            )


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.depends("move_id.partner_id", "display_type")
    def _compute_agent_ids(self):
        non_product_lines = self.filtered(lambda l: l.display_type != "product")
        non_product_lines.agent_ids = False
        product_lines = self - non_product_lines
        if product_lines:
            super(AccountMoveLine, product_lines)._compute_agent_ids()


class AccountInvoiceLineAgent(models.Model):
    _inherit = "account.invoice.line.agent"

    applied_commission_item_id = fields.Many2one("commission.item")

    @api.depends(
        "object_id.price_subtotal",
        "object_id.product_id.commission_free",
        "object_id.display_type",
        "commission_id",
    )
    def _compute_amount(self):  # pylint: disable=W8110 # Computes don't return
        for line in self:
            inv_line = line.object_id
            if inv_line.display_type != "product":
                line.amount = 0.0
                continue
            if line.commission_id and line.commission_id.commission_type == "product":
                line.amount = line._get_single_commission_amount(
                    line.commission_id,
                    inv_line.price_subtotal,
                    inv_line.product_id,
                    inv_line.quantity,
                )
                # Refunds commissions are negative
                if line.invoice_id.move_type and "refund" in line.invoice_id.move_type:
                    line.amount = -line.amount
            else:
                super(AccountInvoiceLineAgent, line)._compute_amount()
