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
    <div id="ilk_div">
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
            <a href="www.instagram.com">İnsta</a>
            <a href="www.wikipedia.com">Wiki</a>
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

"""result=soup.prettify()
print(result)""" #--> hepsini yazdırır
print(soup.title) # <title>Python | Asya Tanrıvere</title>
print(soup.title.name) # title
print(soup.title.string) # Python | Asya Tanrıvere

print(soup.head)
"""
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Python | Asya Tanrıvere</title>
</head>"""
print(soup.find_all("h2"))
"""
[<h2>
<ul>
<li>Numpy</li>
<li>Pandas</li>
<li>Matplotlib</li>
<li>Seaborn</li>
</ul>
</h2>, <h2>
<a href="www.google.com">Google</a>
<a href="www.instagram.com">İnsta</a>
<a href="www.wikipedia.com">Wiki</a>
</h2>]"""
print(soup.find_all("h2")[1])
"""
<h2>
<a href="www.google.com">Google</a>
<a href="www.instagram.com">İnsta</a>
<a href="www.wikipedia.com">Wiki</a>
</h2>
"""
print(soup.find_all("li")[1].string) # Pandas

li_s=soup.find_all("li")

for item in li_s:
    print(item.string)
"""
Numpy
Pandas
Matplotlib
Seaborn
"""
a_s=soup.find_all("a")

for item in a_s:
    print(item.get("href"))
    print(item.string)
"""
www.google.com
Google
www.instagram.com
İnsta
www.wikipedia.com
Wiki
"""
result=soup.find_all("div")[0].h2
print(result)
"""
<h2>
<ul>
<li>Numpy</li>
<li>Pandas</li>
<li>Matplotlib</li>
<li>Seaborn</li>
</ul>
</h2>"""
result2=soup.find_all("div")[0].h2.find_all("li")

for item in result2:
    print(item.string)
"""
Numpy
Pandas
Matplotlib
Seaborn"""
print("------------------------------")
result3=soup.div.findChildren()
print(result3)
"""
[<h2>
<ul>
<li>Numpy</li>
<li>Pandas</li>
<li>Matplotlib</li>
<li>Seaborn</li>
</ul>
</h2>, <ul>
<li>Numpy</li>
<li>Pandas</li>
<li>Matplotlib</li>
<li>Seaborn</li>"""
print("------------------------------")
result4=soup.div.findNextSibling().findNextSibling()
print(result4)
"""
<div class="lor peyniri">
<h2>
<a href="www.google.com">Google</a>
<a href="www.instagram.com">İnsta</a>
<a href="www.wikipedia.com">Wiki</a>
</h2>
</div>
"""
print("------------------------------")
result5=soup.div.findPreviousSibling()
print(result5) # <h1>Data Science, Machine Learning, LLM, Computer Vision</h1>