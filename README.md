# Problem Statement
An address provider returns addresses only with concatenated street names and numbers. 

Our own system on the other hand has separate fields for street name and street number.

**Input**: string of address

**Output**: string of street and string of street-number as JSON object

Write a simple program that does the task for the most simple cases, e.g.
- "Winterallee 3" -> {"street": "Winterallee", "housenumber": "3"}
- "Musterstrasse 45" -> {"street": "Musterstrasse", "housenumber": "45"}
- "Blaufeldweg 123B" -> {"street": "Blaufeldweg", "housenumber": "123B"}

Consider more complicated cases
- "Am Bächle 23" -> {"street": "Am Bächle", "housenumber": "23"}
- "Auf der Vogelwiese 23 b" -> {"street": "Auf der Vogelwiese", "housenumber": "23 b"}

Consider other countries (complex cases)
- "4, rue de la revolution" -> {"street": "rue de la revolution", "housenumber": "4"}
- "200 Broadway Av" -> {"street": "Broadway Av", "housenumber": "200"}
- "Calle Aduana, 29" -> {"street": "Calle Aduana", "housenumber": "29"}
- "Calle 39 No 1540" -> {"street": "Calle 39", "housenumber": "No 1540"}

# Solution
This solution is based upon Python's Regular Expressions.

Two regular expression based patterns are prepared in order to match all the possible inputs.

The parsing of the address string is done, based on which type of pattern it matches.

Following are the patterns
1. re.compile("(\D+\s?){1,10}(,)?[0-9]{1,4}(\s?\D+)?")
2. re.compile("[0-9]{1,4}(,)?(\D+\s?){1,10}")

## scr/DataCleanerUtility.py

- **Class**: CleanAddress
- **Method**: Perform
This is where the actual processing is done.

This utility can be exported in any other python file for the use.

`from DataCleanerUtility import CleanAddress 

cleanaddress = CleanAddress() 

response=cleanaddress.Perform("Calle 39 No 1540")`

# Testing of the Solution
Testing is done in automated way using pytest framework.

## test/TestAddressLine.py
This file contains the tests that are fetching test data from csv files.

The tests are calling the DataCleanerUtility with various address strings and verifying the response against the expected values as per csv. 

Logs for these tests are stored in separate log folder ("Logs") with unique files for each test run. Logging part is handled by logger\Logger.py
