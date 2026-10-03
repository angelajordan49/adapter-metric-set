"""Adapter Metric Set — Show IPv4 interface metrics and set one adapter's metric."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='adapter_metric_set',
        description="Show IPv4 interface metrics and set one adapter's metric.",
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Adapter Metric Set')
    print('Which NIC wins, without the GUI.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
