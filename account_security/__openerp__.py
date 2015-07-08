# -*- coding: utf-8 -*-
{
    'name': 'Account  Security',
    'version': '1.0',
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'description': """
Account Security
================
It creates a many2many field between account  and users. If you set users to accounts or viceversa, then this accounts and the related moves, will be only seen by selected users.
Usually used for payroll accounts.
This fields are only seen by users with "access right management"
    """,
    'author':  'Elwan',
    'website': 'elwan7.wordpress.com',
    'images': [
    ],
    'depends': [
        'account',
        'account_voucher',
    ],
    'data': [
            'res_users_view.xml',
            'account_view.xml',
            'security/account_security_security.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
