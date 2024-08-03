text_from_wiki = "Kannada is a Dravidian language spoken predominantly by the people of Karnataka in Southern India. " \
                 "The language is also spoken by linguistic minorities in the states of Maharashtra, Andhra Pradesh, " \
                 "Tamil Nadu, Telangana, Kerala and Goa; and also by Karnatakas expats abroad."
len(text_from_wiki)
print(len(text_from_wiki))
print(text_from_wiki.upper())
# doesnt modify the original string but creates a new string
print(text_from_wiki)
print(text_from_wiki.lower())
text_from_wiki = 'MICRODEGREE'
print(text_from_wiki.isupper())
text_from_wiki = "Kannada is a Dravidian language spoken predominantly by the people of Karnataka in Southern India. " \
                 "The language is also spoken by linguistic minorities in the states of Maharashtra, Andhra Pradesh, " \
                 "Tamil Nadu, Telangana, Kerala and Goa; and also by Karnatakas expats abroad."
#first occurrence of a character
print(text_from_wiki.find("D"))
#pass a sequence of characters and find index
print(text_from_wiki.find("language"))
print(text_from_wiki.replace('Karnataka','Karunadu'))
# exact case
print(text_from_wiki.replace('karnataka','Karunadu'))
#existence of character
print('k' in text_from_wiki)
print('z' in text_from_wiki)
print('India' in text_from_wiki)
print('Bharat' in text_from_wiki)