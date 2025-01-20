# before making package
# importing functions from module sales
# from sales import calc_shipping, calc_tax

# calc_tax()
# calc_shipping()

# 2nd way to import
# import sales

# sales.calc_shipping()
# sales.calc_tax()

# to import everything from a module
# from sales import *

# calc_tax()
# calc_shipping()

# ----------------------------------------------------------------------------
# Module search path
# import sys

# print(sys.path) #path that python looks for importing a module

# ----------------------------------------------------------------------------
# Package
# It is a container for one or more modules
# To create a package we must create a folder and add all our modules in it
# Necessary add a file named "__init__.py" to make it a package

# from ecommerce.sales import calc_shipping, calc_tax

# calc_shipping()
# calc_tax()

# other way
# from ecommerce import sales

# sales.calc_tax()
# sales.calc_shipping()
# ----------------------------------------------------------------------------
# to create a subpackage follow the same procedure(package within package)
#----------------------------------------------------------------------------
