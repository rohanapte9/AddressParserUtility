import sys
import json
import pandas as pd
import pytest
sys.path.extend(['../scr','../logger'])
from DataCleanerUtility import CleanAddress
from Logger import Logger 

'''
 Constants
'''
SIMPLE_SCENARIOS = r"testdata/SimpleScenarios.csv"
MODERATE_SCENARIOS = r"testdata/ModerateScenarios.csv"
COMPLEX_SCENARIOS = r"testdata/ComplexScenarios.csv"

'''
 Helper Methods
'''
def verify_addressline(log,expected):
  #Create an object for data cleaner utility
  cleanaddress = CleanAddress()
  #Iterate over the test data and verify the results.
  for index, row in expected.iterrows():
    log.debug("---- Iteration "+str(index)+" Started ----")
    #Call the Data Clear Utility with differnt address rows
    testaddress = row['Address Line']
    log.debug("Testing for Address Line: "+testaddress)
    response=cleanaddress.Perform(testaddress)
    actual = json.loads(response)
    #Evaluate the response with expected values.
    try:
      assert actual['street'] == row['street']
      assert actual['housenumber'] == row['housenumber']
    except:
      log.debug("Parsing Failed for: "+testaddress+" Results were: "+response)
      pytest.fail("Parsing Failed for: "+testaddress+" Results were: "+response)
    else:
      log.debug("Results were: "+response)
      log.debug("Verification Successful.")
    log.debug("---- Iteration "+str(index)+" Finished ----\n")


'''
 Tests
'''
@Logger("TestAddressLine","test_simple_address")
def test_simple_address(log):
  '''
  This test verifies the Data Cleaner Utility with some simple address lines.
  for example, 'Winterallee 3' & verifies if the utility performs the split operation correctly.
  '''
  #Read the test Data in pandas frame 
  log.debug("Testing with Simple Address Lines")
  log.debug("Reading Test Data")
  expected = pd.read_csv(SIMPLE_SCENARIOS)
  verify_addressline(log,expected)


@Logger("TestAddressLine","test_with_moderately_complex_address")
def test_with_moderately_complex_address(log):
  '''
  This test verifies the Data Cleaner Utility with moderately complex address lines.
  for example, 'Am Bächle 23' & verifies if the utility performs the split operation correctly.
  '''
  #Read the test Data in pandas frame 
  log.debug("Testing with Simple Address Lines")
  log.debug("Reading Test Data")
  expected = pd.read_csv(MODERATE_SCENARIOS)
  verify_addressline(log,expected)


@Logger("TestAddressLine","test_with_complex_address")
def test_with_complex_address(log):
  '''
  This test verifies the Data Cleaner Utility with complex address lines.
  for example, '4, rue de la revolution' & verifies if the utility performs the split operation correctly.
  '''
  #Read the test Data in pandas frame 
  log.debug("Testing with Simple Address Lines")
  log.debug("Reading Test Data")
  expected = pd.read_csv(COMPLEX_SCENARIOS)
  verify_addressline(log,expected)