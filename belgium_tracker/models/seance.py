# coding: utf-8
from odoo import models, fields


class Seance(models.Model):
    _name = 'belgium_tracker.seance'
    _order = 'date DESC, moment DESC, id DESC'

    name = fields.Char(required=True)
    legislature_id = fields.Many2one('belgium_tracker.legislature', required=True, index=True, default=lambda self: self.env['belgium_tracker.legislature'].search([('fin', '=', False)], order='numero DESC', limit=1).id)
    date = fields.Date(required=True, default=fields.Date.context_today)
    moment = fields.Selection([('am', 'Matin'), ('pm', 'Après-midi'), ('soir', 'Soir')], required=True)
    approuve = fields.Boolean()