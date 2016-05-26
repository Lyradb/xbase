# -*- coding: utf-8 -*-
from datetime import timedelta, time, date, datetime
from dateutil import parser
from openerp import models, fields, api, exceptions


class config_province(models.Model):
    _name = 'config.province'

    province_code = fields.Integer(string='Code', required=True)
    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active')


class config_city(models.Model):
    _name = 'config.city'

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='City/Municipality', required=True)
    province_id = fields.Many2one('config.province', string='Province')
    active = fields.Boolean(string='Active')


class config_barangay(models.Model):
    _name = 'config.barangay'

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Barangay', required=True)
    city_id = fields.Many2one('config.city', string='City/Municipality', ondelete="cascade", onwrite="cascade",
                              required=True)
    zip_code = fields.Char(string='Zip Code', required=True, size=4)
    province_name = fields.Char(related='city_id.province_id.name')
    active = fields.Boolean(string='Active')
