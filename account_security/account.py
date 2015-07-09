# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class account_account(osv.osv):
    _name = 'account.account'
    _inherit = 'account.account'
    
    _columns = {
        'user_x_ids': fields.many2many('res.users', 'account_security_account_users', 'account_id', 
    		'user_id', string='Restricted to Users', help='If choose some users, then this account and the information related to it will be only visible for those users.'),
    }
