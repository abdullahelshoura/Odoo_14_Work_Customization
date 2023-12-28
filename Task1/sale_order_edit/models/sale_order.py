# -*- coding: utf-8 -*-
import datetime
import time
from odoo import api, fields, models,_
from datetime import date
from dateutil import relativedelta
from odoo.exceptions import UserError
class SaleOrder(models.Model):
    _inherit='sale.order'

    inv_date = fields.Date()
    center = fields.Selection(
        [
            ('jadda', "الفرع الرئيسى جدة"),
            ('reyad', "فرع الرياض"),
            ('khobaraa', "فرع الخبراء")
        ],
        store=True,
    )
    branch = fields.Selection(
        [
            ('1', "الامانه لجديده"),
            ('2', "برج تطوير 1 الدور 5"),
            ('3', "برج تطوير 1 الدور 6"),
            ('4', "برج تطوير 1 الدور 8"),
            ('5', " برج تطوير 2 الدور 8"),
            ('6', "برج تطوير 2 الدور 9"),
            ('7', "برج توازن 4 ادوار - تحكم"),
            ('8', "برج توارن الدور 8 - تحكم"),
            ('9', "برج توارن فيلا توارن - تحكم"),
            ('10', "عبداللطيف جميل مبني العروبه - تحكم"),
            ('11', "نموذج الاعمال"),
            ('12', "وزارة الطاقة سنتر ليسن فالي"),
            ('13', "سنتر الخبر - الرزيزا ")
        ],
        store=True,
    )

    def _prepare_invoice(self ):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        # order_invoice_date = self.env['order.invoice.data'].browse(self._context.get('active_ids', []))

        invoice_vals['center_invoice'] = self.center
        invoice_vals['branch_invoice'] = self.branch
        invoice_vals['invoice_date'] = self.inv_date
        # print(invoice_vals)

        return invoice_vals


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    orders = fields.One2many('order.invoice.data', 'advance_id', string='Orders')


    @api.model
    def default_get(self, fields):
        res = super(SaleAdvancePaymentInv, self).default_get(fields)
        # check if we are already standing in the multiple create invoices view
        if 'count' in res:
            if res['count'] > 0:
                # current_id = res['product_id']

                # delete all records from view
                orders_lines = [(5, 0, 0)]
                # print(attribute_lines)

                sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
                for order in sale_orders:
                    # print(order.name)
                    # delete_all_records = (5, 0, 0)
                    line = (0, 0, {
                        'order_id': order.id,
                        'customer_name': order.partner_id.name
                    })
                    # orders_lines.append(delete_all_records)
                    record_set = self.env['order.invoice.data'].search([])
                    record_set.unlink()

                    orders_lines.append(line)
                    # print(self.env['order.invoice.data'].search([]))
                res.update({
                    'orders': orders_lines
                })
        return res


class OrderInvoiceData(models.TransientModel):
    _name = 'order.invoice.data'

    advance_id = fields.Many2one('sale.advance.payment.inv')
    order_id = fields.Many2one('sale.order', string='Order', domain="[('id', '=', order_id)]", store=True)
    customer_name = fields.Char(string='Customer Name')
    invoice_date = fields.Date(string='Invoice Date')

    @api.onchange('invoice_date')
    def onchange_age(self):
        self.order_id.inv_date = self.invoice_date



