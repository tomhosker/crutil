"""
This code defines some general utility functions, used across the project.
"""

# Standard imports.
import traceback

# Local constants.
LUCKY_INT = 17
TRUE_INT = 1
FALSE_INT = 0

###########
# CLASSES #
###########

class CRUtilTypeMismatch(Exception):
    """ A custom exception. """

class CRUtilBadBooleanInteger(Exception):
    """ A custom exception. """

#############
# FUNCTIONS #
#############

def make_contact_template(library):
    """ Prove that you can access the library in question. """
    try:
        library.make_contact(LUCKY_INT)
    except:
        traceback.print_exc()
        return False
    return True

def int_to_bool(integer):
    """ Convert an integer representation of a boolean into a boolean. """
    if integer == TRUE_INT:
        return True
    if integer == FALSE_INT:
        return False
    raise CRUtilBadBooleanInteger("Bad boolean integer: "+str(integer))
