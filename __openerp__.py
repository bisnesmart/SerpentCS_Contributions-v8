# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#    Copyright (C) 2011-2015 Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>).
#    Copyright (C)  20015 bisnesmart (<http://www.bisnesmart.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Digital Signature",
    "version" : "1.0",
    "author" : "Bisnesmart, Serpent Consulting Services Pvt. Ltd.",
    "category": '',
    'complexity': "easy",
    'depends': ['web','project'],
    "description": """
        This module provides the functionality to store digital signature image for a record.
        The example can be seen into the projects form view where we have added three images under signature.
        This module is based in web_digital_sign from "Serpent Consulting Services Pvt. Ltd."
    """,
    'data': [
        'views/we_digital_sign_view.xml',
        'projects_view.xml'
    ],
    'website': 'http://www.bisnesmart.com',
    'qweb': ['static/src/xml/digital_sign.xml'],
    'js': ['static/src/js/digital_sign.js'],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
