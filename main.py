import requests
from bs4 import BeautifulSoup

url="https://indianexpress.com/"
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)

soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

#title=soup.title
#print(type(soup))
#print(type(title))
#print(type(title.string))

#paras=soup.find_all('p')
#print(paras)

#print(soup.find('p'))
#print(soup.find('p')['class']) 
#no class in this websites
#print(soup.find('p').get_text())
#print(soup.get_text())

#markup="<p><!-- this is a comment --></p>"
#soup2=BeautifulSoup(markup)
#print((soup2.p.string))
#exit()


#anchors=soup.find_all('a')
#print(anchors)

#all_links=set()
#for link in anchors:
    #if(link.get('href') !='#'):
        #linkText="https://indianexpress.com/" +link.get('href')
        #all_links.add(link)
        #print(linkText)



# Check if the request was successful
if r.status_code == 200:

    # Step 1: Extract headlines
    
    headlines = soup.find_all('h3')

    # Step 2: Print the extracted headlines
    for headline in headlines:
        print(headline.get_text())
else:
    print("Failed to retrieve the web page")
    
    
# CSS Selector
#elem=soup.select('evnav_login_ham')
#print(elem)