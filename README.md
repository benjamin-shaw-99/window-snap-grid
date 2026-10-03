![Window Snap Grid](assets/hero.png)

# Window Snap Grid

*A small tiling helper for people who outgrew Win+Arrow.*

## About

**Window Snap Grid** is a Windows utility. Snap windows to a custom grid on Windows without extra dock bloat.

Fancy Zones is heavy when you only need 2x2 or 3x2 on one monitor.

The CLI in this repository is the documented interface; the desktop build is the same job in an installer.

## What's included

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Highlights

- Define rows and columns per monitor
- Hotkeys for each cell
- Saves layouts for desk and laptop
- Does not install a dock

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/benjamin-shaw-99/window-snap-grid

MIT license. See `LICENSE`.
