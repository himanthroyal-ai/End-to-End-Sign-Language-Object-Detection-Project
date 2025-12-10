from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys



try:
    a=7/"9"
except SignException(e, sys) from e