# ComfyUI Random Number - File Structure Guide

This document explains what each file does and why it's included.

## 📁 Complete File Structure

```
ComfyUI-RandomNumber/
├── __init__.py              # Required: ComfyUI entry point
├── random_number_node.py    # Required: Node implementation
├── pyproject.toml           # Required: Registry compatibility
├── LICENSE                  # Required: MIT license
├── README.md                # Required: Documentation
├── requirements.txt         # Best Practice: Dependencies (empty for this node)
├── install.py              # Best Practice: Auto-installation script
├── install.sh              # Helper: Manual installation script
└── .gitignore              # Best Practice: Git configuration
```

## 🔍 File Purposes

### Core Files (Required)

**`__init__.py`** - ComfyUI Entry Point
- Exports NODE_CLASS_MAPPINGS and NODE_DISPLAY_NAME_MAPPINGS
- ComfyUI won't load the node without this file
- Imports from random_number_node.py

**`random_number_node.py`** - Node Implementation
- Contains the RandomNumber class with all node logic
- Defines inputs (min_value, max_value, seed)
- Defines outputs (int, float)
- Implements the generate() function
- Sets CATEGORY to "Logic/Math" so it appears in the right menu

### Registry & Manager Compatibility

**`pyproject.toml`** - Registry Metadata
- Required for ComfyUI Registry publishing
- Contains version info (semantic versioning)
- Specifies PublisherId and DisplayName
- Declares Python version requirements
- Makes your node discoverable in the Registry

**`requirements.txt`** - Dependency List
- Tells ComfyUI Manager what packages to install
- Empty for this node (uses only Python standard library)
- Best practice to include even if empty

**`install.py`** - Auto Installation Script
- Executed automatically by ComfyUI Manager after cloning
- Can install dependencies, download models, setup configs
- This one just confirms successful installation

### Documentation & Legal

**`README.md`** - Primary Documentation
- Installation instructions (Manager + Manual)
- Usage examples and parameter explanations
- Troubleshooting section
- Version history
- Critical for user adoption

**`LICENSE`** - MIT License
- Required by pyproject.toml
- Allows commercial and personal use
- MIT is the community standard for ComfyUI nodes
- Provides legal clarity

### Helper Files

**`install.sh`** - Manual Installation Helper
- Bash script for quick manual installation
- Copies files to correct ComfyUI directory
- Makes installation easier for beginners

**`.gitignore`** - Git Configuration
- Prevents committing Python cache files
- Excludes IDE and OS-specific files
- Keeps repository clean

## 🚀 Installation Instructions

### Method 1: Direct Installation (Easiest)

```bash
# Extract and run the installation script
unzip ComfyUI-RandomNumber.zip
cd ComfyUI-RandomNumber
bash install.sh
pm2 restart comfyui
```

### Method 2: Manual Copy

```bash
# Extract and copy to custom_nodes
unzip ComfyUI-RandomNumber.zip
cp -r ComfyUI-RandomNumber /home/localadmin/ComfyUI/custom_nodes/
pm2 restart comfyui
```

### Method 3: Via ComfyUI Manager (After Publishing)

1. Open ComfyUI Manager
2. Search "Random Number"
3. Click Install
4. Restart ComfyUI

## 📋 Checklist for Publishing

### For ComfyUI Manager
- ✅ Create GitHub repository
- ✅ Push all files to repository
- ✅ Submit PR to ComfyUI-Manager's custom-node-list.json

### For ComfyUI Registry
- ✅ Update PublisherId in pyproject.toml (get from registry.comfy.org)
- ✅ Update GitHub URLs in pyproject.toml and README.md
- ✅ Update copyright in LICENSE file
- ✅ Install comfy-cli: `pip install comfy-cli`
- ✅ Publish: `comfy node publish`

## 🎯 What Makes This Production-Ready

1. **Complete Documentation** - README with examples and troubleshooting
2. **Registry Compatible** - pyproject.toml with proper metadata
3. **Manager Compatible** - install.py and requirements.txt
4. **Legally Clear** - MIT License included
5. **Well Organized** - Logical category (Logic/Math)
6. **Error Handling** - Auto-swaps min/max if needed
7. **Reproducible** - Seed control for consistent results
8. **Professional Code** - Docstrings and comments

## 🔄 Version Management

Current version: 1.0.0

To update:
1. Modify code as needed
2. Update version in pyproject.toml (use semantic versioning)
3. Update README.md version history
4. Commit to GitHub
5. Publish to Registry: `comfy node publish`

## 🆘 Troubleshooting

**Node doesn't appear:**
- Check files are in /home/user/ComfyUI/custom_nodes/ComfyUI-RandomNumber/
- Verify __init__.py and random_number_node.py are present
- Check ComfyUI logs: `pm2 logs comfyui`
- Restart ComfyUI completely

**Import errors:**
- Check Python version: `python --version` (needs 3.8+)
- Verify file names match import statements

## 📝 Customization Notes

To customize for your own node:
1. Replace "yourusername" with your GitHub username in:
   - pyproject.toml (2 places)
   - README.md (3 places)
2. Update PublisherId in pyproject.toml after creating Registry account
3. Update LICENSE copyright with your name
4. Update node logic in random_number_node.py
5. Update documentation in README.md

---

This structure follows ComfyUI best practices and ensures compatibility with both ComfyUI Manager and the official Registry.
