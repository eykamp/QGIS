# -*- coding: utf-8 -*-
"""QGIS Unit tests for QgsComposerShape.

.. note:: This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""
__author__ = '(C) 2012 by Dr. Horst Düster / Dr. Marco Hugentobler'
__date__ = '20/08/2012'
__copyright__ = 'Copyright 2012, The QGIS Project'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

import os
import qgis
from PyQt4.QtCore import QFileInfo
from PyQt4.QtXml import QDomDocument
from PyQt4.QtGui import (QPainter, QColor)

from qgis.core import (QgsComposerShape,
                       QgsRectangle,
                       QgsComposition
                     )
from utilities import (unitTestDataPath,
                       getQgisTestApp,
                       TestCase,
                       unittest,
                       expectedFailure
                      )
from qgscompositionchecker import QgsCompositionChecker

QGISAPP, CANVAS, IFACE, PARENT = getQgisTestApp()
TEST_DATA_DIR = unitTestDataPath()


class TestQgsComposerShapes(TestCase):

    def __init__(self, methodName):
        """Run once on class initialisation."""
        unittest.TestCase.__init__(self, methodName)

        # create composition
        self.mComposition = QgsComposition(None)
        self.mComposition.setPaperSize(297, 210)

        self.mComposerShape = QgsComposerShape(20, 20, 150, 100, self.mComposition)
        self.mComposerShape.setBackgroundColor(QColor.fromRgb(255, 150, 0))
        self.mComposition.addComposerShape(self.mComposerShape)

    def testRectangle(self):
        """Test rectangle composer shape"""

        self.mComposerShape.setShapeType(QgsComposerShape.Rectangle)

        checker = QgsCompositionChecker()
        myPath = os.path.join(TEST_DATA_DIR,
                              'control_images',
                              'expected_composershapes',
                              'composershape_rectangle.png')
        myTestResult, myMessage = checker.testComposition('Composer shapes rectangle',
                                             self.mComposition, myPath)

        assert myTestResult == True, myMessage

    def testEllipse(self):
        """Test ellipse composer shape"""

        self.mComposerShape.setShapeType(QgsComposerShape.Ellipse)

        checker = QgsCompositionChecker()
        myPath = os.path.join(TEST_DATA_DIR,
                              'control_images',
                              'expected_composershapes',
                              'composershape_ellipse.png')
        myTestResult, myMessage = checker.testComposition('Composer shapes ellipse',
                                             self.mComposition, myPath)

        assert myTestResult == True, myMessage

    def testTriangle(self):
        """Test triangle composer shape"""

        self.mComposerShape.setShapeType(QgsComposerShape.Triangle)

        checker = QgsCompositionChecker()
        myPath = os.path.join(TEST_DATA_DIR,
                              'control_images',
                              'expected_composershapes',
                              'composershape_triangle.png')
        myTestResult, myMessage = checker.testComposition('Composer shapes triangle',
                                             self.mComposition, myPath)

        assert myTestResult == True, myMessage

    def testRoundedRectangle(self):
        """Test rounded rectangle composer shape"""

        self.mComposerShape.setShapeType(QgsComposerShape.Rectangle)
        self.mComposerShape.setCornerRadius(30)

        checker = QgsCompositionChecker()
        myPath = os.path.join(TEST_DATA_DIR,
                              'control_images',
                              'expected_composershapes',
                              'composershape_roundedrectangle.png')
        myTestResult, myMessage = checker.testComposition('Composer shapes rounded rectangle',
                                             self.mComposition, myPath)

        self.mComposerShape.setCornerRadius(0)
        assert myTestResult == True, myMessage

if __name__ == '__main__':
    unittest.main()

