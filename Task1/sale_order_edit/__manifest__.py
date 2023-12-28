# Copyright 2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Sale Order Edit',
    'summary': 'sale_order_edit',
    'version': '0.1',
    'category': 'sale_order_edit',
    'website': 'https://github.com/OCA/sale-workflow',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'base', 'sale', 'account', 'sale_renting',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/accont_move.xml',
        'views/create_invoice_wizzard_inherit.xml',
        'views/inherit_sale_order_view.xml',

    ],
}
