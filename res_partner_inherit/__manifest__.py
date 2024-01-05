# Copyright 2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Res Partner Edit',
    'summary': 'res_partner_edit',
    'version': '0.1',
    'category': 'res_partner_edit',
    'website': 'https://github.com/OCA',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'base', 'sale', 'purchase', 'account',
    ],
    'data': [
        'views/res_partner_view_inherit.xml',

    ],
}
