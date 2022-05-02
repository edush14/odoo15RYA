from odoo import http
import json

class CustomWebsiteController(http.Controller):
    @http.route('/shf_angular', auth='public', website=True)
    def index(self, **kw):
        data = []
        return http.request.render('shf_angular.index',data)

    @http.route('/shf_angular2', auth='public', website=True)
    def indexss(self, **kw):
        data = []
        return http.request.render('shf_angular.index2', data)

    @http.route(['/get_ventas_shf'], type='http', auth="public", methods=['GET'], website=True, csrf=False)
    def index2(self,**kw):

        #a = http.tu_funcion()
        products = http.request.env['product.product'].sudo().search([])
        products_array = []
        for p in products:
            products_array.append({
                'id': p.id ,
                'parent_id': None,
                "data": {
                    "type": "ARTICLE",
                    "description": p.name,
                    "item": 0,
                    "reference": "",
                    "brand": "",
                    "amount": 0,
                    "measure": 0,
                     "taxes": 0,
                     "unit_value": 0,
                     "partial_value": 0,
                     "list_price": p.lst_price,
                     "discount": 0,
                     "gain": 0,
                     "gain_unit": 0,
                     "gain_total": 0,
                     "real_price": 0,
                     "cost": 0,
                     "stock": p.qty_available
                },
                "children": []
            }
            )

        return json.dumps(products_array)


    #arreglar de la traduccion
    #link de ventas a la pagina
