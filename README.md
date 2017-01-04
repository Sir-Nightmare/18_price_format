# Price Formatter

This script converts numbers like 12345.000 or 12345,000 
into easy-to-read price format 12 345.  
All numbers like 123.456 will be rounded to  two digits after dot; result: 123.46.

##Usage:
**Clone repository:** `git clone https://github.com/Sir-Nightmare/18_price_format.git` 

+ Using in your project: 
`from format_price import format_price`
`print(format_price(1234.5600))`
+ Using manually: `python format_price.py <price>`

Note that you have to use only **int**, **float** or **str** type with this function. With other types the function will raise TypeError.
Value in str has to be like **123.456** or **123,456** otherwise function will raise ValueError.

##Tests:

Runing tests: `python tests.py`

list of tests (input -> output):

+ **big int value:** 9876543210 -> '9 876 543 210'
+ **float value:** 9876.54 -> '9 876.54'
+ **float with zeros:** 54321.00 -> '54 321'
+ **int string:** '109876543210' -> '109 876 543 210'
+ **float string with dot:** '12345.67' -> '12 345.67'
+ **float string with comma:** '12345,67' -> '12 345.67'
+ **incorrect string:** 'qwert1234' ->  ValueError raised
+ **incorrect type (list):** ['123456'] -> TypeError raised

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
