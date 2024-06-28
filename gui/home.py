# SPDX-License-Identifier: GPL-3.0-or-later OR MIT

from PySide6.QtWidgets import QMainWindow

from ._home import Ui_window_home
from .wizard import GuiWidgetWizard


class GuiWindowHome(QMainWindow, Ui_window_home):
  def __init__(self, *args, **kwargs):
    QMainWindow.__init__(self, *args, **kwargs)
    Ui_window_home.__init__(self)
    Ui_window_home.setupUi(self, self)

    self.wizard = GuiWidgetWizard(self.root)
    self.wizard.setObjectName(u"wizard")
