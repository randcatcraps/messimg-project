# SPDX-License-Identifier: GPL-3.0-or-later OR MIT

import os.path
import sys
from PySide6.QtCore import (QLocale, QTranslator)
from PySide6.QtWidgets import QApplication

from .home import GuiWindowHome


TOP = os.path.dirname(sys.argv[0])
LOCALES_DIR = os.path.join(TOP, '_locales')


def load_locale(qt: QApplication,
                tr: QTranslator) -> bool:
  if tr.load(QLocale.system(),
             '', '', LOCALES_DIR):
    print('l10n loaded')
    return True

  print('l10n data missing?')


def main():
  qt = QApplication(sys.argv)
  tr = QTranslator()
  if load_locale(qt, tr):
    qt.installTranslator(tr)
  (home_ := GuiWindowHome()).show()
  sys.exit(qt.exec())


if __name__ == '__main__':
  main()
