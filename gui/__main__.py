# SPDX-License-Identifier: GPL-3.0-or-later OR MIT

import sys
from PySide6.QtWidgets import QApplication

from .home import GuiWindowHome


def main():
  qt = QApplication(sys.argv)
  (home_ := GuiWindowHome()).show()
  sys.exit(qt.exec())


if __name__ == '__main__':
  main()
