from bs4 import BeautifulSoup
import re
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
                <li class="deneme">Pandas</li>
                <li class="deneme">Matplotlib</li>
                <li>Seaborn</li>
            </ul>
        </h2>
    </div>
    <p class="title">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem quaerat incidunt, consectetur autem, sed, repudiandae quis debitis perspiciatis porro ad architecto vitae adipisci blanditiis sit! Quasi voluptates quae at rem!
        Deserunt voluptas vero officiis quo itaque voluptatem amet ex esse, at laborum. Cumque ab quia ea modi dolore hic voluptatum tempora accusantium. Ipsum, at quos. Placeat aperiam accusamus eveniet modi.
        Totam placeat rem ipsum! Nisi temporibus illum quo odio earum similique magnam architecto doloremque voluptate, fuga, consectetur facilis nam delectus aut maxime, perspiciatis totam deserunt nobis molestias laborum harum. Vitae.
    </p>
    <div class="lor peyniri" name="my_links">
        <h2>
            <a href="www.google.com">Google</a>
            <a href="www.instagram.com" id="insta_linki">İnsta</a>
            <a href="www.wikipedia.com" >Wiki</a>
        </h2>
    </div>
    <div class="imageler">
        <p>
            <img src="angara.png" alt="angara">
        </p>
    </div>
</body>
</html>"""
soup = BeautifulSoup(my_html_doc,"html.parser")

for tag in soup.find_all(re.compile("^d")):
    print(tag.name)
"""
div
div
div
"""
for tag in soup.find_all(re.compile("t")):
    print(tag.name)
"""
html
meta
meta
title
"""
for tag in soup.find_all(True):
    print(tag.name) # prints all tag names (html,meta,title,p,h1,ul,li etc.)

print(soup.find_all(["a","p"])) # tüm link ve paragrafları bul ve yazdır
"""
[<p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem quaerat incidunt, consectetur autem, sed, repudiandae quis debitis perspiciatis porro ad architecto vitae adipisci blanditiis sit! Quasi voluptates quae at rem!
        Deserunt voluptas vero officiis quo itaque voluptatem amet ex esse, at laborum. Cumque ab quia ea modi dolore hic voluptatum tempora accusantium. Ipsum, at quos. Placeat aperiam accusamus eveniet modi.
        Totam placeat rem ipsum! Nisi temporibus illum quo odio earum similique magnam architecto doloremque voluptate, fuga, consectetur facilis nam delectus aut maxime, perspiciatis totam deserunt nobis molestias laborum harum. Vitae.
    </p>, <a href="www.google.com">Google</a>, <a href="www.instagram.com" id="insta_linki">İnsta</a>, <a href="www.wikipedia.com">Wiki</a>, <p>
<img alt="angara" src="angara.png"/>
</p>]
"""
print("--------------------------------")
print(soup.find_all("p","title")) # title classına mensup olan p'leri getir
"""
[<p class="title">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem quaerat incidunt, consectetur autem, sed, repudiandae quis debitis perspiciatis porro ad architecto vitae adipisci blanditiis sit! Quasi voluptates quae at rem!
        Deserunt voluptas vero officiis quo itaque voluptatem amet ex esse, at laborum. Cumque ab quia ea modi dolore hic voluptatum tempora accusantium. Ipsum, at quos. Placeat aperiam accusamus eveniet modi.
        Totam placeat rem ipsum! Nisi temporibus illum quo odio earum similique magnam architecto doloremque voluptate, fuga, consectetur facilis nam delectus aut maxime, perspiciatis totam deserunt nobis molestias laborum harum. Vitae.
    </p>]
    """
print(soup.find_all(attrs={"id":"ilk_div"}))
"""
[<div id="ilk_div" name="just_a_name">
<h2>
<ul>
<li>Numpy</li>
<li>Pandas</li>
<li>Matplotlib</li>
<li>Seaborn</li>
</ul>
</h2>
</div>]
"""
print(soup.html.find_all("title",recursive=False)) # []
# title sadece çocuğu ise bulur
# sadece benim belirlediğim etiketin bir alt çocuğunu getir
print(soup.html.find_all("title",recursive=True)) # [<title>Python | Asya Tanrıvere</title>]
# etiketin altında ne kadar "title" varsa yazdır
print(soup.find("a")) # <a href="www.google.com">Google</a>
# nokta atışı tek bir tane 
print(soup.css.select("#ilk_div")) # id için diyez koyuyoruz
"""
[<div id="ilk_div" name="just_a_name">
<h2>
<ul>
<li>Numpy</li>
<li>Pandas</li>
<li>Matplotlib</li>
<li>Seaborn</li>
</ul>
</h2>
</div>]
"""
print(soup.css.select("body a")) # body etiketindeki linkleri ver
# [<a href="www.google.com">Google</a>, <a href="www.instagram.com" id="insta_linki">İnsta</a>, <a href="www.wikipedia.com">Wiki</a>]
print(soup.css.select("head > title")) # head etiketi içindeki title etiketini getir
# [<title>Python | Asya Tanrıvere</title>]
print(soup.css.select(".deneme")) # deneme classına mensup olanları getir
# [<li class="deneme">Pandas</li>, <li class="deneme">Matplotlib</li>]

soup.div["id"]="deniyorum" # ilk divin id'sini değiştirdim
soup.div.name="p" # ilk divi p etiketine dönüştürür
print(soup.prettify())
"""
<!DOCTYPE html>
<html lang="tr">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>
   Python | Asya Tanrıvere
  </title>
 </head>
 <body>
  <h1>
   Data Science, Machine Learning, LLM, Computer Vision
  </h1>
  <p id="deniyorum" name="just_a_name">
   <h2>
    <ul>
     <li>
     .
     .
     .
     """
print("--------------------------------")
del soup.p["id"] # ilk p etiketinin id attribute'e siler
del soup.p["name"] # ilk p etiketinin name attribute'e siler
print(soup.prettify())

soup.li.string="Numpy - Numeric Python" # ilk li etiketinin içeriğini değiştir

soup.img.append("New Image budur") # ilk img etiketine metni ekle
print(soup.find(("img","imageler"))) # imageler isimli classa mensup olan img etiketini yazdır
# <img alt="angara" src="angara.png">New Image budur</img>
print("-------------------------------------")
for item in soup.find_all("a"):
    item.append("New Link")

print(soup.find("div","lor peyniri")) # classı lor peyniri olan divleri yazdırır
"""
<div class="lor peyniri" name="my_links">
<h2>
<a href="www.google.com">GoogleNew Link</a>
<a href="www.instagram.com" id="insta_linki">İnstaNew Link</a>
<a href="www.wikipedia.com">WikiNew Link</a>
</h2>
</div>
"""
soup.h1.extend([","," ","Github"]) # etiketin içeriğini genişleterek değiştirir, ekleme yapar

new_tag=soup.new_tag("li")
new_tag.string="Scikit-Learn"
soup.ul.insert(-1,new_tag) # 0 --> first index -1 --> last index
"""
 <ul>
     <li>
      Numpy - Numeric Python
     </li>
     <li class="deneme">
      Pandas
     </li>
     <li class="deneme">
      Matplotlib
     </li>
     <li>
      Seaborn
     </li>
     <li>
      Scikit-Learn
     </li>
    </ul>
    """
new_tag2=soup.new_tag("span")
new_tag2.string="INSERTED TEXT DUDE"
soup.ul.insert_before(new_tag2)
"""
.
.
 <span>
     INSERTED TEXT DUDE
    </span>
    <ul>
     <li>
      Numpy - Numeric Python
     </li>
     .
     ."""
new_tag3=soup.new_tag("span")
new_tag3.string="INSERTED TEXT DUDE BUT AFTER UL"
soup.ul.insert_before(new_tag3)

soup.title.clear() # etiket içerğini siler
print(soup.find("head"))
"""
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title></title>
</head>
"""
print("-------------------------------------")
tag=soup.title.extract() # siler ama tamamen yok etmez
print(tag) 
# <title></title>
print(soup.find("head"))
"""
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>

</head>"""
tag2=soup.meta.decompose() # tamamen siler
print(tag2)  
# None
print(soup.find("head"))
"""
<head>

<meta content="width=device-width, initial-scale=1.0" name="viewport"/>

</head>
"""
print("**************************************")
print(soup.prettify())
"""
<!DOCTYPE html>
<html lang="tr">
 <head>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
 </head>
 <body>
  <h1>
   Data Science, Machine Learning, LLM, Computer Vision
   ,
   Github
  </h1>
  <p>
   <h2>
    <span>
     INSERTED TEXT DUDE
    </span>
    <span>
     INSERTED TEXT DUDE BUT AFTER UL
    </span>
    <ul>
     <li>
      Numpy - Numeric Python
     </li>
     <li class="deneme">
      Pandas
     </li>
     <li class="deneme">
      Matplotlib
     </li>
     <li>
      Seaborn
     </li>
     <li>
      Scikit-Learn
     </li>
    </ul>
   </h2>
  </p>
  <p class="title">
   Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem quaerat incidunt, consectetur autem, sed, repudiandae quis debitis perspiciatis porro ad architecto vitae adipisci blanditiis sit! Quasi voluptates quae at rem!
        Deserunt voluptas vero officiis quo itaque voluptatem amet ex esse, at laborum. Cumque ab quia ea modi dolore hic voluptatum tempora accusantium. Ipsum, at quos. Placeat aperiam accusamus eveniet modi.
        Totam placeat rem ipsum! Nisi temporibus illum quo odio earum similique magnam architecto doloremque voluptate, fuga, consectetur facilis nam delectus aut maxime, perspiciatis totam deserunt nobis molestias laborum harum. Vitae.
  </p>
  <div class="lor peyniri" name="my_links">
   <h2>
    <a href="www.google.com">
     Google
     New Link
    </a>
    <a href="www.instagram.com" id="insta_linki">
     İnsta
     New Link
    </a>
    <a href="www.wikipedia.com">
     Wiki
     New Link
    </a>
   </h2>
  </div>
  <div class="imageler">
   <p>
    <img alt="angara" src="angara.png">
     New Image budur
    </img>
   </p>
  </div>
 </body>
</html>
"""