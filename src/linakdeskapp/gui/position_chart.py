# MIT License
# 
# Copyright (c) 2017 Arkadiusz Netczuk <dev.arnet@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
 
 
import logging

from .mpl_canvas import DynamicMplCanvas

try:
    import pandas
except ImportError as e:
    ### No module named <name>
    logging.exception("Exception while importing")
    exit(1)
 
 
 
_LOGGER = logging.getLogger(__name__)
 

 
class PositionChart(DynamicMplCanvas):
     
    def __init__(self, parentWidget = None):
#         super().__init__(parentWidget, 5, 4, 50)
        super().__init__(parentWidget, 10, 10, 50)
        
        self.xdata = list()
        self.ydata = list()
        self.axes.cla()                                     ## clear
        self.ax, = self.axes.plot_date( self.xdata, self.ydata, 'r', 
                                        linewidth=3, antialiased=True)
        
#         xticks = self.axes.xaxis.get_major_ticks()
#         xticks[0].label1.set_visible(True)
#         xticks[-1].label1.set_visible(True)

        ## _LOGGER.info("aaa: %s", dir(self.axes))

    def drawFigure(self):
        self.ax.set_xdata( self.xdata )
        self.ax.set_ydata( self.ydata )
        
        ## draw plot
        self.axes.relim()
        self.axes.autoscale_view()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        
        self.draw()
    
    def add(self, deskHeight):
        currTime = self.getCurrTime()
        self.xdata.append(currTime)
        self.ydata.append(deskHeight)

    def update_figure(self):
        yLen = len(self.ydata)
        if yLen < 1:
            return
        last = self.ydata[-1]
        if yLen < 2:
            ## only one value
            self.add( last )
            return
        ## two or more values
        last2 = self.ydata[-2]
        if last != last2:
            self.add( last )
            return
        self.xdata[-1] = self.getCurrTime()
    
    def getCurrTime(self):
        currTime = pandas.Timestamp.now()
        ## _LOGGER.info("adding plot data: %r %f", currTime, deskHeight )
        return currTime
