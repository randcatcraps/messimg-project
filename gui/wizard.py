# SPDX-License-Identifier: GPL-3.0-or-later OR MIT

from PySide6.QtWidgets import QWidget

from ._wizard import Ui_widget_wizard


class GuiWidgetWizard(QWidget, Ui_widget_wizard):
  def __init__(self, *args, **kwargs):
    QWidget.__init__(self, *args, **kwargs)
    Ui_widget_wizard.__init__(self)
    Ui_widget_wizard.setupUi(self, self)
