# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class users(osv.osv):
    _name = 'res.users'
    _inherit = 'res.users'
    
    _columns = {
        'account_ids': fields.many2many('account.account', 'account_security_account_users','user_id',
                                        'account_id', 'Restricted Accounts', help="This accounts and the information related to it will be only visible for users where you specify that they can see them setting this same field."),
    }
