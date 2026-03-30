"""
Agent Genome Mapping™ — Setup Script
Упаковка пакета для публикации на PyPI

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Методология: Agent Genome Mapping™ (AGM)
"""

from setuptools import setup, find_packages
from pathlib import Path

# Чтение README для long_description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Метаданные пакета
setup(
    # Основная информация
    name="agent-genome-mapping",
    version="0.1.0",
    description="Agent Genome Mapping™ — Evolutionary Architecture for Autonomous AI Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # Автор
    author="Dm.Andreyanov",
    author_email="imperiapmk@gmail.com",
    url="https://github.com/GIBDD-DPS/agent-genome-mapping",
    project_urls={
        "Documentation": "https://github.com/GIBDD-DPS/agent-genome-mapping",
        "Source": "https://github.com/GIBDD-DPS/agent-genome-mapping",
        "Tracker": "https://github.com/GIBDD-DPS/agent-genome-mapping/issues",
        "LinkedIn": "https://www.linkedin.com/in/dmitry-andreyanov-b587b44b/",
        "Medium": "https://medium.com/@dima100575_70241"
    },
    
    # Лицензия
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    
    # Ключевые слова
    keywords="ai agents genome mapping autonomous systems machine learning architecture",
    
    # Пакет
    packages=find_packages(exclude=["tests", "examples"]),
    python_requires=">=3.8",
    
    # Зависимости
    install_requires=[
        "pyyaml>=6.0",
        "numpy>=1.24.0",
    ],
    
    # Дополнительные зависимости
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=6.0.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
    },
    
    # Входные точки (опционально)
    entry_points={
        "console_scripts": [
            "agm=agm.cli:main",  # Если будет CLI
        ],
    },
    
    # Включение дополнительных файлов
    package_data={
        "agm": ["py.typed"],
    },
    include_package_data=True,
    
    # Метки
    zip_safe=False,
)
