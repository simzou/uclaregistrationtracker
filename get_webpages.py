#!/usr/bin/env python
import urllib
from datetime import datetime

MATH_URL = "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=MATH"
CS_URL = "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=COM+SCI"

now = datetime.now().isoformat()[0:16] # cuts off milliseconds
cs_filename = "comsci_" + now + ".html"
math_filename = "math_" + now + ".html"
urllib.urlretrieve(MATH_URL, math_filename)
urllib.urlretrieve(CS_URL, cs_filename)





























































































