#! /usr/bin/env python

from colours import OKGREEN, ENDC, FAIL, WARNING

print("hello there! %sChecks OK%s") % (OKGREEN, ENDC)
print("Something went wrong. %sFAIL%s") % (FAIL, ENDC)
