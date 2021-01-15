import os
from datetime import datetime
import logging


class Logger:
  '''
    Description: 
      Logger class provides methods to log debug statements in logs
      For every test execution a unique log gets created with TestName and Timestamp.
    
    Usage:
      Every PyTest should be decorated with Logger with 2 arguments.
        arg 1: File Name where test is located
        arg 2: Name of the test method.
      Example,
        test_simple_address method from TestAddressLine.py should be written as follows:
        @Logger("TestAddressLine","test_simple_address")
        def test_simple_address(log):
          log.debug("Testing with Simple Address Lines")
          {code}
  '''


  def __init__(self, filename, testname):
    self.logfile = ''
    self.filename = filename
    self.testname = testname


  def __call__(self, func):
    #Create a unique log file path based on current date
    def innerfunction(capsys):
      self.compositename = self.testname+"_"+datetime.now().strftime("%Y_%m_%d__%H_%M_%S")+".log"
      self.logpath = os.path.join("..","Logs",self.filename)
      #Create log directory if not present.
      if not os.path.exists(self.logpath):
        os.makedirs(self.logpath)
      self.logfile = os.path.join(self.logpath,self.compositename)
      logging.basicConfig(filename=self.logfile, level=logging.INFO)
      # Making a call to the decorated method.
      func(self)
    return innerfunction


  def debug(self, logstring):
    # Writes log statements with timestamp
    with open(self.logfile,'a') as logs:
      logs.write(datetime.now().strftime("%H:%M:%S.%f  ")+logstring+"\n")