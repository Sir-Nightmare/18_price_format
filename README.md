# Price Formatter

##About:

This script converts numbers like 12345.000 or 12345,000 into easy-to-read price format 12 345. (123.456 into 123.45)

##Usage:
**Clone repository:** `git clone https://github.com/Sir-Nightmare/18_price_format.git` 

+ Using in your project: 
`from format_price import format_price`
`print(format_price(1234.5600))`
+ Using manually: `python format_price.py <price>`
Note that you have to use only **int**, **float** or **str** type with this function. With other types the function will raise TypeError.
Value in str has to be like **123.456** or **123,456** otherwise function will raise ValueError.

##How to run tests:

Run `python tests.py`

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
