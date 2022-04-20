# -*- encoding: utf-8 -*-
{
    'name': 'RYA DESARROLLO',
    'category': 'uncategorize',
    'author': 'ITGRUPO',
    'depends': ['mrp_account_enterprise'],
    'version': '1.0',
    'description':"""
     Descripcion
    """,
    'auto_install': False,
    'demo': [],
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/mrp_production.xml',
        'views/solicitud_material.xml',
        'views/mrp_bom_line.xml',
        'views/plantilla_ratios.xml',
        'views/cost_structure_report.xml'
        ],
    'installable': True
}