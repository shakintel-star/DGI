# @DGI System Installer
# Lead: Shakti Singh | Version: 1.0.0

from setuptools import setup, find_packages

setup(
    name="dgi-sovereign-grid",
    version="1.0.0",
    author="Shakti Singh (Genesisgraphy)",
    description="Decentralized General Intelligence Operating System",
    packages=find_packages(),
    install_packages=[
        "requests",      # For Global API handshakes
        "cryptography",  # For S-256 Binary security
        "numpy"         # For CERN Quantum data processing
    ],
    entry_points={
        'console_scripts': [
            'dgi-start=kernel.xos_core:main',
            'dgi-vault=vault.dgi_vault_v1:main',
        ],
    },
    python_requires='>=3.8',
)
