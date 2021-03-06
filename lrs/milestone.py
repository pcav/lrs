# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LrsPlugin
                                 A QGIS plugin
 Linear reference system builder and editor
                              -------------------
        begin                : 2013-10-02
        copyright            : (C) 2013 by Radim Blažek
        email                : radim.blazek@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from qgis.core import *

from utils import *

class LrsMilestone(object):

    def __init__(self, fid, geoPart, nGeoParts, pnt, measure):
        self.fid = fid # point 
        # multigeometry part
        self.geoPart = geoPart
        # number of geometry parts in original feature, used for error checksum
        self.nGeoParts = nGeoParts
        self.pnt = pnt   # QgsPoint
        self.measure = measure # field measure
        self.part = None # part index
        # distance from beginning of part to the point on part nearest to pnt
        self.partMeasure = None 
