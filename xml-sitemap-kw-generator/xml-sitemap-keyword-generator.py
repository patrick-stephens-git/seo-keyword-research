from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

# XML Sitemap Parser Functions:
def get_sitemap(url):
    get_url = requests.get(url)
    if get_url.status_code == 200:
        return get_url.text
    else:
        print('Unable to fetch sitemap: %s' % url)
        
def process_sitemap(s):
    soup = BeautifulSoup(s, 'html.parser')
    result = []
    for loc in soup.findAll('loc'):
        result.append(loc.text)
    return result

def is_sub_sitemap(s):
    if s.endswith('.xml') and 'sitemap' in s:
        return True
    else:
        return False

def parse_sitemap(s):
    sitemap = process_sitemap(s)
    result = []
    while sitemap:
        candidate = sitemap.pop()
        if is_sub_sitemap(candidate):
            sub_sitemap = get_sitemap(candidate)
            for i in process_sitemap(sub_sitemap):
                sitemap.append(i)
        else:
            result.append(candidate)
    return result

# Converts sitemap URLs to string:
def convert_string_to_list(string): 
    li = list(string.split("\n")) 
    return li 

# Main Process Function:
def main(sitemap_url):
    sitemap = get_sitemap(sitemap_url)
    sitemap_urls = '\n'.join(parse_sitemap(sitemap))
    return sitemap_urls

# Function for turning list of URLs into keywords
def normalize_sitemap_keywords(input_list):
    urls = []
    for line in input_list:
        line = (re.sub('https://.*\\.com/','',line,count=0,flags=re.I)) # Removes domain
        line = (re.sub('.*/','',line,count=0,flags=re.I)) # Removes directories
        line = (re.sub('-',' ',line,count=0,flags=re.I)) # Removes dashes
        line = (re.sub(',','',line,count=0,flags=re.I)) # Removes commas
        line = (re.sub('\\(','',line,count=0,flags=re.I)) # Removes (
        line = (re.sub('\\)','',line,count=0,flags=re.I)) # Removes )
        line = (re.sub('[0-9]','',line,count=0,flags=re.I)) # Removes numbers
        line = (re.sub('%','',line,count=0,flags=re.I)) # Removes % symbols
        line = (re.sub('\\.html','',line,count=0,flags=re.I)) # Removes .html
        line = (re.sub('\\.shtml','',line,count=0,flags=re.I)) # Removes .shtml
        line = (re.sub('\\.aspx','',line,count=0,flags=re.I)) # Removes .aspx
        line = (re.sub('\\.pdf','',line,count=0,flags=re.I)) # Removes .pdf
        line = (re.sub('\\.','',line,count=0,flags=re.I)) # Removes periods
        line = (re.sub('\\s+',' ',line,count=0,flags=re.I)) # Removes double spaces in a line
        line = (re.sub('\\s$','',line,count=0,flags=re.I)) # Removes space at the end of a line
        line = (re.sub('^\\s','',line,count=0,flags=re.I)) # Removes space at the beginning of a line
        urls.append(line)
    return urls

def export_csv(df):
    with open('competitor_xml_sitemap_keywords.txt','w') as export_file:
        df.to_csv('competitor_xml_sitemap_keywords.txt', mode='w', encoding='utf-8', index=False, header=False)

sitemap_url_list = ['https://www.thebalancecareers.com/sitemap_1.xml','https://zety.com/sitemap-static.xml','https://zety.com/sitemap-dynamic.xml'] # If these sitemaps don't work then update to a URL you know has an active sitemap

# Start Pulling Sitemap URLs:
list_of_keywords = []
if __name__ == '__main__':
    for sitemap_url in sitemap_url_list:
        print('Pulling URLs from {0}'.format(sitemap_url))
        sitemap_keywords = main(sitemap_url)
        sitemap_keywords = (convert_string_to_list(sitemap_keywords)) 
        list_of_keywords.extend(sitemap_keywords)
# len(list_of_keywords)

# Removes domain from URLs:
print('Converting XML sitemap URLs into keywords...')
keywords = normalize_sitemap_keywords(list_of_keywords)
# Turns all keywords into lowercase
keywords = [keyword.lower() for keyword in keywords]

# Find more specific keywords in a list:
refined_keywords = []
strings = ('job','resume','cover letter','cv','curriculum vitae','position','opening','career','company','companies','business','pay','paid','salary','salaries','raise','income','compensation','skill','interview','work','vacancy','vacancies','opening','employ','opportunity','opportunities','hire','hiring','license','certification','profession','answer','question','entry','refer','offer','weakness','strength','close','closing','open','introduce','introduction','network','promoting','promote','promotion','gap','boss','worklife','work life','dress code','dresscode','attire','icebreaker','ice breaker','quit','followup','follow up','resign','intern','responsibility','responsibilities','skill','relocate','relocating','industry','industries','application','apply','qualification','qualified','office','performance','leadership','talent','train','training')

for line in keywords:
    if any(s in line for s in strings):
        refined_keywords.append(line)

# Convert list to a dataframe:
#### IF YOU WANT A LIST OF ALL KEYWORDS DISCOVERED THEN:
#### Switch 'refined_keywords' in line 104 to 'keywords'
keyword_df = pd.DataFrame(refined_keywords)
keyword_df = keyword_df.drop_duplicates().sort_values(0, ascending=True)

# Writes refined discovered keywords into a file:
export_csv(keyword_df)