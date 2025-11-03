#!/usr/bin/env python3
"""
Installation script for ComfyUI Random Number Generator
This script is automatically executed by ComfyUI Manager after cloning the repository.
"""

import sys
import os


def install():
    """
    Install dependencies for the Random Number node.
    
    This node has no external dependencies (uses only Python standard library),
    so this script just confirms successful installation.
    """
    print("=" * 60)
    print("ComfyUI Random Number Generator - Installation")
    print("=" * 60)
    print("")
    print("✓ No external dependencies required")
    print("✓ Installation complete!")
    print("")
    print("The node will appear in: Logic → Math → Random Number")
    print("Or search for 'Random Number' in the node menu")
    print("")
    print("Please restart ComfyUI to load the node.")
    print("=" * 60)
    
    return True


if __name__ == "__main__":
    try:
        success = install()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Installation failed: {e}")
        sys.exit(1)
