# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:16:38 2024

@author: Gebruiker
"""

colors_config= {
    'colors' : {
        'bg_figs': '#1D2322',
   #     'bg_figs': '#433F3B',
        "surround_figs": '#5B706F',
        'text': '#6C0F73',
        'font': 'Verdana',
        'palet': ['#52121F', '#B41D3B', '#7B1529', '#E61942', '#C0C0C0']
        }    
    }

# card style
card_config = {
    'cardstyle' : {
#        'width': '13rem',
#        'height': '4.5rem',
        'border-radius': '15px',
        'border':'1px solid #C0C0C0',
        'background-color':colors_config['colors']['surround_figs']
        },
    'cardtitle' : {
        'color': colors_config['colors']['text'],
        'font-size':'16px',
        'font-weight':'bold'
        },
    'cardtext' : {
        'color': '#FFFFFF',
        'font-size':'16px',
        'font-weight':'bold'
        },
    }      