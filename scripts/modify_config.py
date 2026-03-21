#!/usr/bin/env python3
import sys
import os

# Parameter grid with SYNTHESIS-LEVEL variations
PARAM_GRID = {
    # Original configs (placement-level params - will show identical synthesis)
    1:  {'util': 40, 'density': 0.55, 'buf': 'BUF_X2', 'abc_script': 'area'},
    2:  {'util': 40, 'density': 0.65, 'buf': 'BUF_X2', 'abc_script': 'area'},
    3:  {'util': 50, 'density': 0.55, 'buf': 'BUF_X2', 'abc_script': 'area'},
    4:  {'util': 50, 'density': 0.65, 'buf': 'BUF_X2', 'abc_script': 'area'},
    5:  {'util': 50, 'density': 0.70, 'buf': 'BUF_X2', 'abc_script': 'area'},
    
    # NEW: Synthesis-level variations (ABC optimization strategy)
    11: {'util': 50, 'density': 0.65, 'buf': 'BUF_X2', 'abc_script': 'area'},   # Area-optimized
    12: {'util': 50, 'density': 0.65, 'buf': 'BUF_X2', 'abc_script': 'delay'},  # Delay-optimized
    13: {'util': 50, 'density': 0.65, 'buf': 'BUF_X2', 'abc_script': 'default'}, # Balanced
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
        elif 'export ABC_AREA' in line and params['abc_script'] != 'area':
            # Comment out area optimization if not area mode
            modified.append(f'# {line}')
        else:
            modified.append(line)
    
    # Add ABC script selection
    if params['abc_script'] == 'delay':
        modified.append('\nexport SYNTH_HIERARCHICAL = 0\n')
        modified.append('export ABC_SPEED = 1\n')
    
    with open(run_config, 'w') as f:
        f.writelines(modified)
    
    print(f"Created config: {run_config}")
    print(f"  CORE_UTIL={params['util']}, DENSITY={params['density']}, ABC={params['abc_script']}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python modify_config.py <design> <config_id> <orfs_path>")
        sys.exit(1)
    
    design = sys.argv[1]
    config_id = int(sys.argv[2])
    orfs_path = sys.argv[3]
    
    modify_config(design, config_id, orfs_path)
