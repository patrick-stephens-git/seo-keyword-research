README.txt

CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 * Requirements
 * Configuration
 * Instructions


INTRODUCTION
------------

The XML Sitemap Keyword Finder Scripts allows you to generate a list of keywords found in the URLs contained within multiple XML sitemaps.


REQUIREMENTS
------------

This module requires the following external modules:

 * bs4 (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 * re (documentation: https://docs.python.org/2/library/re.html)
 * requests (https://docs.python-requests.org/en/latest/)
 * pandas (https://pandas.pydata.org/docs/)


CONFIGURATION
-------------

Within the xml-sitemap-keyword-generator.py script you must include a list of links to sitemaps AND a list of target keywords:

	# Update the sitemap_url_list variable to include a list of XML Sitemaps you want to pull keywords from.
	# Example: sitemap_url_list = ['https://www.website1.com/sitemap_1.xml','https://zety.website2/sitemap-static.xml','https://website3.com/sitemap-dynamic.xml']

	# Update the strings variable to include a list of target keywords.
	# Example: strings = ('job','resume')
	
	## URL in XML Sitemap: https://www.website.com/should-you-start-looking-for-a-job-before-you-quit
	## Result: "should you start looking for a job before you quit"



INSTRUCTIONS
-------------

Input: 
	python3 xml-sitemap-keyword-generator.py
Output: 
	competitor_xml_sitemap_keywords.txt 	- 	gives you list of every keyword discovered

