import re
from re import match

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    reg_no = fields.Char(string="الرقم التسجيلي")
    tax_file = fields.Char(string="الملف الضريبي")
    deal_type = fields.Char(string="طبيعة التعامل", required=True)
    miss_code = fields.Char(string="كود المأمورية المختص" )

    id_id = fields.Char(string="الرقم القومي")

    customer_vendor = fields.Selection([('customer', 'Customer'), ('vendor', 'Vendor')])

    account_number = fields.Char(string="رقم الحساب")
    bank_address = fields.Char(string="عنوان بنك المورد")
    bank_name = fields.Char(string="اسم بنك المورد")
    ibn_number = fields.Char(string="IBN Number")
    swift_number = fields.Char(string="Swift Number")

    # Patient Model SQL Constrants
    # Check that ID is Unique
    _sql_constraints = [
        ('uniq_id_id',
         'UNIQUE (id_id)',
         'This Personal ID Is Already Exist')]

    # --------------Patient Model Constraints---------------=
    # Check that ID is only numeric and its length is not less or more than 14 numbers
    @api.constrains('id_id')
    def id_constrains(self):
        if self.id_id:
            if not self.id_id.isdigit() or not len(self.id_id) == 14:
                raise ValidationError('The Personal ID must be not less or more than 14 Numbers')




