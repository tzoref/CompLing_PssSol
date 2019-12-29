#!/usr/bin/env python
# coding: utf-8

# # Selecting Gendered-Terms in PSALMS of SOLOMON

# The Psalms of Solomon is a collection of 18 psalms in classical Greek, composed in Judea in the first or second centuries BCE. Since I am working on an article about the representation of gender in this composition, I am interested in using computational language processing techniques to capture and analyze relevant data. The exercise I chose for this assignment is to find instances of the terms "woman", "father", "mother", "son", and "daughter".
# 
# A description of the process is provided in the final cell, following the coding.

# In[1]:


# Import the textual data from https://sacred-texts.com and writing to a file "pss"

import requests_html

# Iterate over chapter numbers in URL to get complete text without line numbers or link to next page

session = requests_html.HTMLSession()
with open("tag.txt", "w",) as pss:

    for psalm in range(1,19):
    
        URL = "https://sacred-texts.com/bib/sep/pss" + f'{psalm:03d}' + ".htm"
        SELECTOR = "//p/text()"

        request = session.get(URL)

        for tag in request.html.xpath(SELECTOR):
            print(tag.lstrip(), file=pss)
            
        print(file=pss)


# In[2]:


# To search for woman, match each line with letter sequence "γυν"
# Tokenize the file, with a line for each word, and match each line for γυν 

import re
counter = 0

with open("tag.txt", "r") as pss:
    for line in pss:
        tokens = line.rstrip().split()
        for token in tokens:
            woman = re.search("γυν", token)
            if woman:
                print(token)
                counter += 1
    print("There are", counter, "occurences")


# In[3]:


# Check for words with accent on the upsilon

counter = 0
with open("tag.txt", "r") as pss:
    for line in pss:
        tokens = line.rstrip().split()
        for token in tokens:
            woman = re.match("γ(ύ|ϋ|ΰ|υ)", token)
            if woman:
                print(token)
                counter += 1
    print("There are", counter, "occurences")


# In[4]:


# Search for father, using: πατ followed by ὴ or έ

counter = 0
with open("tag.txt", "r") as pss:
    for line in pss:
        tokens = line.rstrip().split()
        for token in tokens:
            father = re.match("πατ(ὴ|έ)", token)
            if father:
                print(token)
                counter += 1
    print("There are", counter, "occurences")


# In[5]:


# To search for mother: μητ

counter = 0
with open("tag.txt", "r") as pss:
    for line in pss:
        tokens = line.rstrip().split()
        for token in tokens:
            father = re.match("μητ", token)
            if father:
                print(token)
                counter += 1
    print("There are", counter, "occurences")


# In[6]:


# To search for son: υἱ

counter = 0
with open("tag.txt", "r") as pss:
    for line in pss:
        tokens = line.rstrip().split()
        for token in tokens:
            son = re.search("υἱ", token)
            if son:
                print(token)
                counter += 1
    print("There are", counter, "occurences")


# In[7]:


# To search for daughter: θυγατ 

counter = 0
with open("tag.txt", "r") as pss:
    for line in pss:
        tokens = line.rstrip().split()
        for token in tokens:
            daughter = re.search("θυγατ", token)
            if daughter:
                print(token)
                counter += 1
    print("There are", counter, "occurences")


# In[8]:


# To search for daughter: θυγατ 

counter = 0
with open("tag.txt", "r") as pss:
    for line in pss:
        tokens = line.rstrip().split()
        for token in tokens:
            man = re.search("νθρωπ(ο|ό)", token)
            if man:
                print(token)
                counter += 1
    print("There are", counter, "occurences")


# I first needed to grab and scrape the online Greek text of the 18 chapters of Psalms of Solomon from the website https://sacred-texts.com/bib/sep/pss001.htm.
# 
# Using the "View" option on my MacBook, I selected "Developer" and "View Source" to see the sources code for the site. The sacred-texts website uses html code and features one chapter per page. To get the cleaned text for each chapter, I iterated over all 18 chapters with a for loop, using zero-padding, to select only the text tagged as "//p" (this removed line numbers and links to "Next" psalm). The zero padding was necessary because the psalms in the URL are numbered from 001 to 018. 
# 
# I created a file tag.txt to store the scraped Greek text, to be called as pss.
# 
# My next goal was to locate the terms for woman, i.e., words beginning with γυν.
# I initially thought I would try to use UNIMORPH, but found this too daunting, and realized that a simple regex search would suffice.
# 
# When this worked, I also did separate searches for father, mother, son, and daughter. And then (hu)man, ἄνθρωπος. I performed each search in a separate cell because this felt neater to me.  But I wonder whether there can be a more economical way to do the searches, without having to repeat the tokenizing, and having the output yield the results for each word separately, with blank lines between the words. I did not try to do this because as I thought about how this search program could be useful for research on the Psalms, I realized that I would want indexing-- not just lists of the matched words, but the ability to locate the occurence at a chapter and line. 
# In its current form, my coding seemed more useful for counting occurences than finding them, so I added a counter. (For consistency, I did this even where the count can be seen at a glance).
# 
# Casefolding was not necessary, because the only upper-case letters in the text are those used for proper names.
# I was not sure whether the upsilon in γυν- words ever takes any accent, and whether the coding would catch accented letters in case it does. So I emended the search to add the alternative of unaccented or accented upsilon.  I saw I did not need to add the nu, since the list was identical to the γυν search.
# 
# For son, I initially searched for υἱο, but realized this was not capturing the whole list.  Before playing with possible regex options, I tried searching for just υἱ and all of the output are "son" words, so I did not need to fiddle further. 
# 
# Another approach I would be interested to explore would be to try to use word frequencies to identify key motifs in the text, and see if there are any clusters of the above family/gender terms in relation to the motifs. I recognize that this is the sort of task, at this small scope, that is better suited to manual close-reading than computational analysis, but I think it might be a useful exercise.  I also wonder whether there could be any point to isolating masculine and feminine verbs and adjectives; I think not, but what prompts this thought is that Jerusalem, as a city, is feminine and the personification of the city is very gendered.
# 
# 
