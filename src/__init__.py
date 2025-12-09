"""
Training Data Curation Bot
Enterprise - grade training data curation bot for LLM fine - tuning
using Decodo + Python automation .
"""

__version__ = " 0.1.0 "
__author__ = " Atharva"
__email__ = " atharvak18052004@gmail.com "
__description__ = " Enterprise - grade training data curation bot for LLM fine - tuning "

# Core imports for easy access
from .core.config import settings
from .core.logging import get_logger
from .core.exceptions import TrainingDataBotError

# Main bot class
from .bot import TrainingDataBot

from .sources import (
    PDFLoader,            # Worker who reads PDF files
    WebLoader,            # Worker who reads websites
    DocumentLoader,       # Worker who reads text files
    UnifiedLoader         # Boss who decides which worker to use
)

from .tasks import (
    QAGenerator,              # Worker who makes questions and answers
    ClassificationGenerator,  # Worker who sorts things into categories
    SummarizationGenerator,   # Worker who makes short summaries
    TaskTemplate              # The instruction sheets for workers
)

from .decodo import DecodoClient            # The internet scraper
from .preprocessing import TextPreprocessor # The text cleaner
from .evaluation import QualityEvaluator    # The quality checker
from .storage import DatasetExporter        # The packager

__all__ = [
    # Core
    "TrainingDataBot",
    "settings",
    "get_logger",
    "TrainingDataBotError",

    # Sources
    "PDFLoader",
    "WebLoader",
    "DocumentLoader",
    "UnifiedLoader",

    # Tasks
    "QAGenerator",
    "ClassificationGenerator",
    "SummarizationGenerator",
    "TaskTemplate",

    # Services
    "DecodoClient",
    "TextPreprocessor",
    "QualityEvaluator",
    "DatasetExporter",
]
