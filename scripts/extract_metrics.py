#!/usr/bin/env python3
import sys
import json
import re
import os

def extract_metrics(report_file, config_id):
    """Extract PPA metrics from OpenROAD report"""
    
    if not os.path.exists(report_file):
        print(f"ERROR: Report file not found: {report_file}")
        return None
    
    metrics = {
        'config_id': config_id,
        'area_um2': None,
        'wns_ns': None,
        'tns_ns': None,
        'cell_count': None,
        'net_count': None
    }
    
    with open(report_file, 'r') as f:
        content = f.read()
    
    # Extract area
    area_match = re.search(r'Design area:\s+([\d.]+)\s+u\^2', content)
    if area_match:
        metrics['area_um2'] = float(area_match.group(1))
    
    # Extract WNS
    wns_match = re.search(r'wns\s+([-\d.]+)', content, re.IGNORECASE)
    if wns_match:
        metrics['wns_ns'] = float(wns_match.group(1))
    
    # Extract TNS
    tns_match = re.search(r'tns\s+([-\d.]+)', content, re.IGNORECASE)
    if tns_match:
        metrics['tns_ns'] = float(tns_match.group(1))
    
    # Extract cell count
    cell_match = re.search(r'Number of cells:\s+(\d+)', content)
    if cell_match:
        metrics['cell_count'] = int(cell_match.group(1))
    
    # Extract net count
    net_match = re.search(r'Number of nets:\s+(\d+)', content)
    if net_match:
        metrics['net_count'] = int(net_match.group(1))
    
    return metrics

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_metrics.py <report_file> <config_id> <output_json>")
        sys.exit(1)
    
    report_file = sys.argv[1]
    config_id = int(sys.argv[2])
    output_file = sys.argv[3]
    
    metrics = extract_metrics(report_file, config_id)
    
    if metrics:
        with open(output_file, 'w') as f:
            json.dump(metrics, f, indent=2)
        print(f"Metrics extracted successfully: {output_file}")
        print(json.dumps(metrics, indent=2))
    else:
        print("Failed to extract metrics")
        sys.exit(1)