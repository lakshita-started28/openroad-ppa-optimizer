# Parameter grid for PPA sweep
# Each config is: (CORE_UTILIZATION, PLACE_DENSITY, CTS_BUF_LIST, config_id)

PARAM_GRID = {
    1:  {'util': 40, 'density': 0.55, 'buf': 'BUF_X2'},
    2:  {'util': 40, 'density': 0.65, 'buf': 'BUF_X2'},
    3:  {'util': 50, 'density': 0.55, 'buf': 'BUF_X2'},
    4:  {'util': 50, 'density': 0.65, 'buf': 'BUF_X2'},
    5:  {'util': 50, 'density': 0.70, 'buf': 'BUF_X2'},
    6:  {'util': 60, 'density': 0.60, 'buf': 'BUF_X2'},
    7:  {'util': 60, 'density': 0.70, 'buf': 'BUF_X2'},
    8:  {'util': 60, 'density': 0.75, 'buf': 'BUF_X2'},
    9:  {'util': 70, 'density': 0.65, 'buf': 'BUF_X2'},
    10: {'util': 70, 'density': 0.75, 'buf': 'BUF_X2'},
    11: {'util': 70, 'density': 0.80, 'buf': 'BUF_X2'},
    12: {'util': 50, 'density': 0.65, 'buf': 'BUF_X4'},
    13: {'util': 60, 'density': 0.70, 'buf': 'BUF_X4'},
    14: {'util': 70, 'density': 0.75, 'buf': 'BUF_X4'},
    15: {'util': 45, 'density': 0.60, 'buf': 'BUF_X2'},
    16: {'util': 55, 'density': 0.65, 'buf': 'BUF_X2'},
    17: {'util': 65, 'density': 0.70, 'buf': 'BUF_X2'},
    18: {'util': 75, 'density': 0.75, 'buf': 'BUF_X2'},
    19: {'util': 35, 'density': 0.50, 'buf': 'BUF_X2'},
    20: {'util': 80, 'density': 0.85, 'buf': 'BUF_X2'},
    # Add up to 30 if you want
}