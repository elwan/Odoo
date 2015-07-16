# -*- coding: utf-8 -*-
#from openerp import models, fields, api
from openerp.http import request 
from openerp.osv import osv,fields 
# class users_adress_ip(models.Model):
#     _name = 'users_adress_ip.users_adress_ip'

#     name = fields.Char()
class users(osv.osv):
    _name = 'res.users'
    _inherit = 'res.users'

    _columns={ 
        'ip_address':fields.char('IP ADDRESS',default=' ',readonly=True),
      }
    @api.model
    def _get_ipaddress(self):
        users = self.pool.get('res.users')
        current_user = users.browse(cr, uid, uid, context=context) 
        if current_user :
            return request.httprequest.environ['REMOTE_ADDR']  
#    _defaults ={
    #'ip_address': _get_ipaddress,
#       }
