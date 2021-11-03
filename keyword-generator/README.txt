README.txt

CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 * Requirements
 * Configuration
 * Instructions


INTRODUCTION
------------

The Cartesian Generator Scripts allow you to generate a small or massive list of keywords from 2 input list(s) and 1 template list.


REQUIREMENTS
------------

This module requires the following external modules:

 * Time (documentation: https://docs.python.org/2/library/time.html)
 * Re (documentation: https://docs.python.org/2/library/re.html)
 * Itertools (documentation: https://docs.python.org/2/library/itertools.html)
 * Sys (documentation: https://docs.python.org/2/library/sys.html)


CONFIGURATION
-------------

 * cartesian-product-2keyword-generator.py
	# Use this generator if you are generating keywords with 2 keywords + 1 template combination:
	# Ex Combination:
	## Keyword: "software engineer", "san antonio tx"
	## Template: "average {keyword1} salary in {keyword2}"
	## Result: "average software engineer salary in san antonio tx"


INSTRUCTIONS
-------------

Command:
	$ cartesian-product-2keyword-generator.py template_file.txt keyword1_file.txt keyword2_file.txt
Input: 
	template_file.txt -	one template per line
	keyword1_file.txt - one keyword per line
	keyword2_file.txt - one keyword per line
Output: 
	2keyword_templates_cartesian_product - gives you list of every combination

