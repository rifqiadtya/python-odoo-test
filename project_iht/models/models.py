from odoo import _, api, fields, models
from odoo.exceptions import UserError

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    lokasi_proyek = fields.Text('Lokasi Proyek')
    source_aplikasi_pendukung = fields.Char('Source Aplikasi Pendukung')
    daftar_pekerja_remote = fields.Json('Daftar Pekerja Remote')

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def action_confirm(self):
        for order in self:
            if order.amount_total < 500000:
                raise UserError("Minimal order value adalah 500.000")

        return super(SaleOrder, self).action_confirm()
