import re

a = "Your TAN Number is 604878. Please enter to log"

if "TAN Number" in a:
    print "Good"
    d = re.findall(r'\d+', a)[0]
    print d
else:
    print "Not contain"