import re
import json


class CleanAddress:
  '''
    An address provider returns addresses only with concatenated street names and numbers. 
    Our own system on the other hand has separate fields for street name and street number.

    CleanAddress Class is created for parsing the concatenated addresses to extract 
      - The House Number  
      - The Streen Address.

    Perform method from CleanAddress class does this processing and returns the JSON object as response.  

    Input: string of address
    Output: string of street and string of street-number as JSON object
  '''

  def __self__(self):
    pass


  def Perform(self, addressline):
    result ={}
    # Pattern Set 1
    # This set is intended to match addresses with Street number at the end of the string
    NameFirstPattern = re.compile("(\D+\s?){1,10}(,)?[0-9]{1,4}(\s?\D+)?")
    NameFirstNm = re.compile("(\D+\s?){1,10}")  #To Extract the street part
    NameFirstNo = re.compile("[0-9]{1,4}(\s?\D+)?") #To Extract the house number part

    # Pattern Set 2
    # This set is intended to match addresses with Street number at the begining of the string
    NoFirstPattern = re.compile("[0-9]{1,4}(,)?(\D+\s?){1,10}")
    NoFirstNm = re.compile("(\D+\s?){1,10}") #To Extract the street part
    NoFirstNo = re.compile("[0-9]{1,4}") #To Extract the house number part

    ObjNameFirst=re.search(NameFirstPattern,addressline)

    if ObjNameFirst:
      # If the String matches Pattern Set 1 perform the following steps
      if " No " in addressline:
        # Special handling for one of the complex kind of addresses. e.g. "Calle 39 No 1540"
        line = addressline.split("No")
        result['street'] = line[0].strip()
        result['housenumber'] = "No "+line[1].strip()
      else:
        # General handling of Pattern Set 1 addresses.
        result['street'] = re.search(NameFirstNm,addressline).group().replace(",",'').strip()
        result['housenumber'] = re.search(NameFirstNo,addressline).group().replace(",",'').strip()
    else:
        # If the String matches Pattern Set 2 perform the following steps
      objNoFirst = re.search(NoFirstPattern,addressline)
      if objNoFirst:
        result['street'] = re.search(NoFirstNm,addressline).group().replace(",",'').strip()
        result['housenumber'] = re.search(NoFirstNo,addressline).group().replace(",",'').strip()
      else:
        # In case pattern does not match with any of the pattern sets.
        result['error'] = "Could not parse the data."

    return json.dumps(result)

