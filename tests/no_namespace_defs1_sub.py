#!/usr/bin/env python

#
# Generated  by generateDS.py.
# Python 2.7.14 (default, Sep 23 2017, 22:06:14)  [GCC 7.2.0]
#
# Command line options:
#   ('--no-dates', '')
#   ('--no-versions', '')
#   ('--disable-xml', '')
#   ('--disable-generatedssuper-lookup', '')
#   ('--member-specs', 'list')
#   ('-f', '')
#   ('-a', 'xsd:')
#   ('-o', 'tests/no_namespace_defs2_sup.py')
#   ('-s', 'tests/no_namespace_defs2_sub.py')
#   ('--super', 'no_namespace_defs2_sup')
#   ('--no-warnings', '')
#
# Command line arguments:
#   tests/no_namespace_defs.xsd
#
# Command line:
#   generateDS.py --no-dates --no-versions --disable-xml --disable-generatedssuper-lookup --member-specs="list" -f -a "xsd:" -o "tests/no_namespace_defs2_sup.py" -s "tests/no_namespace_defs2_sub.py" --super="no_namespace_defs2_sup" --no-warnings tests/no_namespace_defs.xsd
#
# Current working directory (os.getcwd()):
#   generateds
#

import sys
## from lxml import etree as etree_

import no_namespace_defs2_sup as supermod

## def parsexml_(infile, parser=None, **kwargs):
##     if parser is None:
##         # Use the lxml ElementTree compatible parser so that, e.g.,
##         #   we ignore comments.
##         parser = etree_.ETCompatXMLParser()
##     doc = etree_.parse(infile, parser=parser, **kwargs)
##     return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class peopleTypeSub(supermod.peopleType):
    def __init__(self, person=None, specialperson=None):
        super(peopleTypeSub, self).__init__(person, specialperson, )
supermod.peopleType.subclass = peopleTypeSub
# end class peopleTypeSub


class personTypeSub(supermod.personType):
    def __init__(self, value=None, id=None, ratio=None, name=None, interest=None, category=None, description=None):
        super(personTypeSub, self).__init__(value, id, ratio, name, interest, category, description, )
supermod.personType.subclass = personTypeSub
# end class personTypeSub


