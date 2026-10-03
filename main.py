"""Window Snap Grid — Snap windows to a custom grid on Windows without extra dock bloat."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='window_snap_grid',
        description='Snap windows to a custom grid on Windows without extra dock bloat.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Window Snap Grid')
    print('A small tiling helper for people who outgrew Win+Arrow.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
