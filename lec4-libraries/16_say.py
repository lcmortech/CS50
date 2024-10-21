# PACKAGES
	# PyPI pypi.org - python package index (similar to npm in js)
	# pypi.org/project/cowsay
	# pip - python
	
import cowsay
import sys

if len(sys.argv) == 2:
	cowsay.cow("Hello, " + sys.argv[1])

# ++ Terminal Window ++
# python say.py Name
# python say.py 
# python say.py Name >> produces a dinosaur

# ====
# pypi.org/project/requests - APIs