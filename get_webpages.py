#!/usr/bin/env python
import urllib
from datetime import datetime

subjects = {
	"polsci" : {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=POL+SCI"
	},
	"math": {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=MATH"
	},
	"comsci": {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=COM+SCI"
	},
	"econ": {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=ECON"
	},
	"lifesci": {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=LIFESCI"
	},
	"mgmt": {
		"url": "http://www.registrar.ucla.edu/schedule/crsredir.aspx?termsel=14F&subareasel=MGMT"
	},
	"chem": {
		"url": "http://www.registrar.ucla.edu/schedule/crsredir.aspx?termsel=14F&subareasel=CHEM"
	},
	"physics": {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=PHYSICS"
	},
	"engl": {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=ENGL"
	},
	"elengr": {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=EL+ENGR"
	},
	"psych": {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=PSYCH"
	},
	"pic": {
		"url": "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=14F&subareasel=COMPTNG"
	}
}

now = datetime.now().isoformat()[0:16] # cuts off milliseconds

for key, value in subjects.iteritems():
	filename = key + "_" + now + ".html"
	urllib.urlretrieve(value["url"], filename)





















































































