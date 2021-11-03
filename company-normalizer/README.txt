README.txt

CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 * Requirements
 * Configuration
 * Instructions


INTRODUCTION
------------

The Company Normalizer Script allows you to generate a list of normalized company names by removing suffixes (& Co., Inc., etc) from 1 input list of companies.

!!! This is a work in progress and will NOT normalize all company names. !!!
!!! Find a list of excluded suffixes used for normalization in 'list-of-suffix-exclusions.txt' !!!


REQUIREMENTS
------------

This module requires the following external modules:

 * re (documentation: https://docs.python.org/2/library/re.html)
 * sys (documentation: https://docs.python.org/2/library/sys.html)


CONFIGURATION
-------------

 * company-normalizer.py
	# Ex 1:
	##  Input Company: "iHeartMedia, Inc."
	## Result Company: "iHeartMedia"

	# Ex 2:
	##  Input Company: "Total Quality Logistics (TQL)"
	## Result Company: "Total Quality Logistics"

	# Ex 3:
	##  Input Company: "ABC Supply Co. Inc"
	## Result Company: "ABC Supply"


INSTRUCTIONS
-------------

Command:
	$ python company-normalizer.py input_file.txt
Input: 
	input_file.txt			-	one company per line
Output: 
	normalized-file.txt 	- 	gives you list of normalized companies

