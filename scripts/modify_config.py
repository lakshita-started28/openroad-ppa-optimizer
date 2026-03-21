#!/usr/bin/env python3
import sys
import os

# Parameter grid defined here
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
}

def modify_config(design, config_id, orfs_path):
    """Modify OpenROAD config.mk with parameters from PARAM_GRID"""
    
    if config_id not in PARAM_GRID:
        print(f"ERROR: Config ID {config_id} not in PARAM_GRID")
        sys.exit(1)
    
    params = PARAM_GRID[config_id]
    
    base_config = f'{orfs_path}/flow/designs/nangate45/{design}/config.mk'
    run_config = f'{orfs_path}/flow/designs/nangate45/{design}/config_run{config_id}.mk'
    
    if not os.path.exists(base_config):
        print(f"ERROR: Base config not found: {base_config}")
        sys.exit(1)
    
    with open(base_config, 'r') as f:
        lines = f.readlines()
    
    modified = []
    for line in lines:
        if 'export CORE_UTILIZATION' in line:
            modified.append(f'export CORE_UTILIZATION = {params["util"]}\n')
        elif 'export PLACE_DENSITY' in line:
            modified.append(f'export PLACE_DENSITY = {params["density"]}\n')
        elif 'export CTS_BUF_LIST' in line:
            modified.append(f'export CTS_BUF_LIST = {params["buf"]}\n')
        else:
            modified.append(line)
    
    with open(run_config, 'w') as f:
        f.writelines(modified)
    
    print(f"Created config: {run_config}")
    print(f"  CORE_UTIL={params['util']}, PLACE_DENSITY={params['density']}, CTS_BUF={params['buf']}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python modify_config.py <design> <config_id> <orfs_path>")
        sys.exit(1)
    
    design = sys.argv[1]
    config_id = int(sys.argv[2])
    orfs_path = sys.argv[3]
    
    modify_config(design, config_id, orfs_path)
