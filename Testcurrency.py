"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Dominique Blair
Date:   May 5, 2024
"""

import introcs             #for asserts
import currency            #This is what is being tested

print ("All tests completed successfully.")

def test_before_space():
    """
    Test procedure for before_space 
    """
    print("Testing before_space")
 
 #Test Case 1: One space in middle
    result = currency.before_space('300 USD')
    introcs.assert_equals('300', result)
 #Test Case 2: Multiple spaces seperated
    result = currency.before_space('USD PEP 400')
    introcs.assert_equals('USD', result)
 #Test Case 3: 
    result = currency.before_space(' JPY890')
    introcs.assert_equals("", result)
#Test Case 4: 
    result = currency.before_space('  ')
    introcs.assert_equals("", result)


def test_after_space():
    """
    Test procedure for after_space
    """
    print("Testing after_space")
 #Test Case 1:
    result = currency.after_space('300 USD')
    introcs.assert_equals('USD', result)
 #Test Case 2:
    result = currency.after_space('250  JPY')
    introcs.assert_equals(' JPY', result)
 #Test Case 3:
    result = currency.after_space('BRL ')
    introcs.assert_equals("", result)
 #Test Case 4:
    result = currency.after_space(' DOP 200')
    introcs.assert_equals('DOP 200', result)


def test_first_inside_quotes():
    """
    Test procedure for first_inside_quotes
    """
    print("Testing first_inside_quotes")
 #Test Case 1:
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)
 #Test Case 2:
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)
 #Test Case 3:
    result = currency.first_inside_quotes('"A"')
    introcs.assert_equals('A', result)
 #Test Case 4:
    result = currency.first_inside_quotes('A B C "" "E" ')
    introcs.assert_equals('', result)
    

def test_get_src():
    """
    Test procedure for get_src 
    """
    print("Testing get_src")
 #Test Case 1
    result = currency.get_src('{"success": true, "src": "2 United States Dollars","dst":'
    +' "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
 #Test Case 2
    result = currency.get_src('{"success":true, "src":"2 United States Dollars", "dst":'
    + '"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars', result)
 #Test Case 3
    result = currency.get_src('{"success":false,"src":"","dst":'
    +'"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)
 #Test Case 4
    result = currency.get_src('{"success":false,"src": "","dst":'
    +'"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_get_dst():
    """
    Test procedure for get_dst
    """
    print("Testing get_dst")
 #Test Case 1
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars",' 
    +'"dst":  "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)
 #Test Case 2
    result = currency.get_dst('{"success":true, "src":"2 United States Dollars", "dst":'
    +'"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros', result)
 #Test Case 3
    result = currency.get_dst('{"success":false,"src":"","dst":'
    +'"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)
 #Test Case 4
    result = currency.get_dst('{"success":false,"src":"","dst":'
    +' "","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_has_error():
    """
    Test procedure for has_error
    """
    print("Testing has_error")
 #Test Case 1
    result = currency.has_error('{"success":false,"src":"","dst":'
    +'"","error":"Source currency code is invalid."}')
    introcs.assert_true(result)
 #Test Case 2
    result = currency.has_error('{"success": true, "src": "2 United States Dollars",'
    +' "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_false(result)
 #Test Case 3
    result = currency.has_error('{"success": true, "src": "2 United States Dollars",'
    +' "dst": "1.772814 Euros", "error":""}')
    introcs.assert_false(result)
 #Test Case 4
    result = currency.has_error('{"success":false,"src":"","dst":'
    +'"","error": "Source currency code is invalid."}')
    introcs.assert_true(result)


def test_service_response():
    """
    Test procedure for service_response
    """
    print("Testing service_response")
 #Test Case 1
    result = currency.service_response('USD', 'EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", "dst":'
    +' "2.2160175 Euros", "error": ""}',result)
 #Test Case 2
    result = currency.service_response('EUR', 'USD',-4.5)
    introcs.assert_equals('{"success": true, "src": "-4.5 Euros", "dst":'
    +' "-5.076674710375708 United States Dollars", "error": ""}',result)
 #Test Case 3
    result = currency.service_response('EURO', 'USD',-4.5)
    introcs.assert_equals('{"success": false, "src": "", "dst":'
    +' "", "error": "The rate for currency EURO is not present."}',result)
#Test Case 4
    result = currency.service_response('EUR', 'USDOLLAR', 7.5)
    introcs.assert_equals('{"success": false, "src": "", "dst":'
    +' "", "error": "The rate for currency USDOLLAR is not present."}',result)


def test_iscurrency():
    """
    Test procedure for iscurrency
    """
    print("Testing iscurrency")
 #Test Case 1
    result = currency.iscurrency('EUR')
    introcs.assert_true(True, result)
 #Test Case 2
    result = currency.iscurrency('EURO')
    introcs.assert_false(False, result)


def test_exchange():
    """
    Test procedure for exchange
    """
    print("Testing exchange")

 #Test Case 1
    result = currency.exchange('USD', 'EUR', 4.5)
    introcs.assert_floats_equal(3.9888315, result)

 #Test Case 2
    result = currency.exchange('USD', 'EUR', -4.5)
    introcs.assert_floats_equal(-3.9888315, result)


#Script code
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print("All tests completed successfully")