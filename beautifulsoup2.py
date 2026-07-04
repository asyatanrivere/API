from bs4 import BeautifulSoup
my_html_doc="""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python | Asya Tanrıvere</title>
</head>
<body>
    <h1>Data Science, Machine Learning, LLM, Computer Vision</h1>
    <div id="ilk_div" name="just_a_name">
        <h2>
            <ul>
                <li>Numpy</li>
                <li>Pandas</li>
                <li>Matplotlib</li>
                <li>Seaborn</li>
            </ul>
        </h2>
    </div>
    <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem quaerat incidunt, consectetur autem, sed, repudiandae quis debitis perspiciatis porro ad architecto vitae adipisci blanditiis sit! Quasi voluptates quae at rem!
        Deserunt voluptas vero officiis quo itaque voluptatem amet ex esse, at laborum. Cumque ab quia ea modi dolore hic voluptatum tempora accusantium. Ipsum, at quos. Placeat aperiam accusamus eveniet modi.
        Totam placeat rem ipsum! Nisi temporibus illum quo odio earum similique magnam architecto doloremque voluptate, fuga, consectetur facilis nam delectus aut maxime, perspiciatis totam deserunt nobis molestias laborum harum. Vitae.
    </p>
    <div class="lor peyniri">
        <h2>
            <a href="www.google.com">Google</a>
            <a href="www.instagram.com" id="insta_linki">İnsta</a>
            <a href="www.wikipedia.com" >Wiki</a>
        </h2>
    </div>
    <div>
        <p>
            <img src="angara.png" alt="angara">
        </p>
    </div>
</body>
</html>"""
soup = BeautifulSoup(my_html_doc,"html.parser")

print(soup.title.name) # title
print(soup.title.parent.name) # head
print(soup.head.parent.name) # html
print(soup.div["id"]) # ilk_div
print(soup.div["name"]) # just_a_name
print(soup.find_all("div")[0].attrs) # {'id': 'ilk_div', 'name': 'just_a_name'}
print(soup.find_all("div")[0].attrs.keys()) # dict_keys(['id', 'name'])

print(soup.find_all("div")[0].attrs["name"]) # just_a_name
soup.find_all("div")[0].attrs["name"]="special_colour"
print(soup.find_all("div")[0].attrs["name"]) # special_colour
print(soup.find_all("div")[0].attrs) # {'id': 'ilk_div', 'name': 'special_colour'}

print(soup.title.string) # Python | Asya Tanrıvere
soup.title.string.replace_with("Deneme")
print(soup.title.string) # Deneme

print(soup.find("a")) # <a href="www.google.com">Google</a>
print(soup.find("a").string) # Google

print(soup.head.contents) # ['\n', <meta charset="utf-8"/>, '\n', <meta content="width=device-width, initial-scale=1.0" name="viewport"/>, '\n', <title>Deneme</title>, '\n']
print(soup.head.contents[1]) # <meta charset="utf-8"/>
print(soup.head.contents[1]["charset"]) # UTF-8
print(soup.head.contents[5]) # <title>Deneme</title>
print(soup.head.contents[5].contents) # ['Deneme']

print("------------------------------")
for child in soup.head.descendants:
    print(child)
"""
                                                               ---> \n

<meta charset="utf-8"/>
                                                               ---> \n

<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
                                                               ---> \n

<title>Deneme</title>
Deneme
                                                               ---> \n

"""

print(len(list(soup.descendants))) # 68

for string in soup.strings:
    print(repr(string))
"""
'\n'
'\n'
'\n'
'\n'
'\n'
'\n'
'Deneme'
'\n'
'\n'
'\n'
'Data Science, Machine Learning, LLM, Computer Vision'
'\n'
'\n'
'\n'
'\n'
'Numpy'
'\n'
'Pandas'
'\n'
'Matplotlib'
'\n'
'Seaborn'
'\n'
'\n'
'\n'
'\n'
'\n        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem quaerat incidunt, consectetur autem, sed, repudiandae quis debitis perspiciatis porro ad architecto vitae adipisci blanditiis sit! Quasi voluptates quae at rem!\n        Deserunt voluptas vero officiis quo itaque voluptatem amet ex esse, at laborum. Cumque ab quia ea modi dolore hic voluptatum tempora accusantium. Ipsum, at quos. Placeat aperiam accusamus eveniet modi.\n        Totam placeat rem ipsum! Nisi temporibus illum quo odio earum similique magnam architecto doloremque voluptate, fuga, consectetur facilis nam delectus aut maxime, perspiciatis totam deserunt nobis molestias laborum harum. Vitae.\n    '
'\n'
'\n'
'\n'
'Google'
'\n'
'İnsta'
'\n'
'Wiki'
'\n'
'\n'
'\n'
'\n'
'\n'
'\n'
'\n'
'\n'
'\n'
"""

for string in soup.stripped_strings:
    print(string)
"""
Deneme
Data Science, Machine Learning, LLM, Computer Vision
Numpy
Pandas
Matplotlib
Seaborn
Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem quaerat incidunt, consectetur autem, sed, repudiandae quis debitis perspiciatis porro ad architecto vitae adipisci blanditiis sit! Quasi voluptates quae at rem!
        Deserunt voluptas vero officiis quo itaque voluptatem amet ex esse, at laborum. Cumque ab quia ea modi dolore hic voluptatum tempora accusantium. Ipsum, at quos. Placeat aperiam accusamus eveniet modi.
        Totam placeat rem ipsum! Nisi temporibus illum quo odio earum similique magnam architecto doloremque voluptate, fuga, consectetur facilis nam delectus aut maxime, perspiciatis totam deserunt nobis molestias laborum harum. Vitae.
Google
İnsta
Wiki
"""
print(soup.title.parent)
"""
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Deneme</title>
</head>
"""
print("------------------------------------")
for parent in soup.a.parents:
    print(parent.name)
"""
h2
div
body
html
[document]
"""
print(soup.div.next_sibling.next_sibling.next_sibling.next_sibling)
"""
<div class="lor peyniri">
<h2>
<a href="www.google.com">Google</a>
<a href="www.instagram.com">İnsta</a>
<a href="www.wikipedia.com">Wiki</a>
</h2>
</div>"""
print(soup.div.previous_sibling.previous_sibling) # <h1>Data Science, Machine Learning, LLM, Computer Vision</h1>

for item in soup.a.next_siblings:
    print(repr(item))
"""
'\n'
<a href="www.instagram.com">İnsta</a>
'\n'
<a href="www.wikipedia.com">Wiki</a>
'\n'"""
print("----------------------------------")
for item in soup.find(id="ilk_div").previous_siblings:
    print(repr(item))
"""
'\n'
<h1>Data Science, Machine Learning, LLM, Computer Vision</h1>
'\n'"""
print(soup.find("a",id="insta_linki").next_element) # İnsta
print(soup.find("a",id="insta_linki").previous_element.previous_element) # Google
print(soup.find("a",id="insta_linki").previous_element.previous_element.previous_element) # <a href="www.google.com">Google</a>
print("------------------------------------------")
for item in soup.find("a", id="insta_linki").next_elements:
    print(repr(item))
"""
'İnsta'
'\n'
<a href="www.wikipedia.com">Wiki</a>
'Wiki'
'\n'
'\n'
'\n'
<div>
<p>
<img alt="angara" src="angara.png"/>
</p>
</div>
'\n'
<p>
<img alt="angara" src="angara.png"/>
</p>
'\n'
<img alt="angara" src="angara.png"/>
'\n'
'\n'
'\n'
'\n'"""
