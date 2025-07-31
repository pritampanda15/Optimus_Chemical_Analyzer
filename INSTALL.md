# Installation Guide for Optimus Chem

## Quick Installation

```bash
cd Optimus_Chemical_Analyzer
pip install -e .
```

## Requirements

- Python 3.7+
- RDKit (installed automatically via `rdkit-pypi`)
- NumPy, Pandas, Matplotlib

## Installation Options

### Option 1: Development Installation (Recommended)

```bash
# Clone or navigate to the Optimus Chemical Analyzer directory
cd Optimus_Chemical_Analyzer

# Install in development mode
pip install -e .

# This allows you to modify the code and see changes immediately
```

### Option 2: Standard Installation

```bash
cd Optimus_Chemical_Analyzer
pip install .
```

### Option 3: Install from Wheel

```bash
# Build the package first
cd Optimus_Chemical_Analyzer
python setup.py bdist_wheel

# Install the wheel
pip install dist/optimus_chem-1.0.0-py3-none-any.whl
```

## Verify Installation

```python
from optimus import ChemicalAnalyzer

analyzer = ChemicalAnalyzer()
result = analyzer.analyze_smiles("CCO")  # Ethanol
print(f"Molecular Weight: {result.molecular_weight:.2f}")
print(f"Lipinski Violations: {result.lipinski_violations}")
```

## Test the Package

```bash
cd Optimus_Chemical_Analyzer
python test/test_optimus.py
```

## Command Line Usage

After installation, you can use the `optimus` command:

```bash
# Analyze single compound
optimus analyze "CCO"

# Analyze batch from file
optimus batch compounds.smi --output results.csv

# Generate HTML report
optimus report compounds.smi --output report.html

# Validate SMILES
optimus validate "CC(=O)OC1=CC=CC=C1C(=O)O"
```

## Troubleshooting

### RDKit Installation Issues

If RDKit installation fails:

```bash
# Try conda instead
conda install -c conda-forge rdkit

# Or use mamba for faster installation
mamba install -c conda-forge rdkit
```

### Import Errors

If you get import errors:

```bash
# Check if optimus-chem is installed correctly
pip list | grep optimus

# Reinstall in development mode
pip uninstall optimus-chem
pip install -e .
```

### Permission Issues

On some systems, you may need to use `--user`:

```bash
pip install --user -e .
```

## Development Setup

For development work:

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Code formatting
black optimus/

# Type checking
mypy optimus/
```

## Creating Distribution

To create a distributable package:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to PyPI (if you have access)
twine upload dist/*
```

## Docker Installation

For containerized deployment:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY optimus/ /app/optimus/
COPY setup.py /app/

RUN pip install -e .

CMD ["optimus", "--help"]
```

## Integration with Jupyter

For Jupyter notebook integration:

```python
# Install in Jupyter environment
!pip install -e .

# Use in notebook
from optimus import ChemicalAnalyzer
import pandas as pd

analyzer = ChemicalAnalyzer()
result = analyzer.analyze_smiles("your_smiles_here")

# Display results
result.to_json()
```

## Performance Optimization

For large-scale analysis:

```python
# Use batch processing
analyzer = ChemicalAnalyzer(use_cached_descriptors=True)

# Process in chunks for memory efficiency
def process_large_file(filename, chunk_size=1000):
    # Implementation for chunked processing
    pass
```