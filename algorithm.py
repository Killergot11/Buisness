import geoformulas
#import webbrowser
import responses as long
import questions as q
import random
#import webbrowser


responses = [
    {'reply':[str(long.unknown())],'requirements':['tomorrow','tomorrow\'s','time'],'must':[],'hasArg':True,'probability':0},
    {'reply':[str(long.unknown())],'requirements':['yesterday','yesterday\'s','time'],'must':[],'hasArg':True,'probability':0},
    {'reply':[str(long.unknown())],'requirements':[],'must':[],'hasArg':True,'probability':0},
    {'reply':["Bye!! see you around"],'requirements':['goodbye','bye'],'must':[],'hasArg':True,'probability':0},
    {'reply':["Hello","Sup","Hey!!","Hola"],'requirements':[],'must':['hi','hello','Hi'],'hasArg':True,'probability':0},
    {'reply':["My name is ChadBot"],'requirements':["what"],'must':['name'],'hasArg':True,'probability':0},
    {'reply':["I am a simple ChatBot"],'requirements':['what','you'],'must':[],'hasArg':True,'probability':0},
    {'reply':["Yes,I am doing fine"],'requirements':['you?','are'],'must':['fine'],'hasArg':True,'probability':0},
    {'reply':["Your Welcome!"],'requirements':['thanks','a lot','thank'],'must':[],'hasArg':True,'probability':0},
    {'reply':[long.R_TIME],'requirements':['today\'s','time'],'must':[],'hasArg':True,'probability':0},
    {'reply':[long.R_DATE],'requirements':[],'must':['date'],'hasArg':True,'probability':0},
    {'reply':['I don\'t know'],'requirements':['die','death'],'must':['when','will'],'hasArg':True,'probability':0},
    {'reply':[long.R_ADVICE],'requirements':['advice'],'must':['give',],'hasArg':True,'probability':0},
    {'reply':[q.reflection],'requirements':[],'must':['reflection'],'hasArg':True,'probability':0},
    {'reply':[q.refraction],'requirements':[],'must':['refraction'],'hasArg':True,'probability':0},
    {'reply':[q.dispersion],'requirements':[],'must':['dispersion'],'hasArg':True,'probability':0},
    {'reply':[q.vsepr],'requirements':['vsepr','VSEPR'],'must':[],'hasArg':True,'probability':0},
    {'reply':[q.quadraticequations],'requirements':[],'must':['quadratic'],'hasArg':True,'probability':0},
    {'reply':[q.indiafreedom],'requirements':[],'must':['india','independence'],'hasArg':True,'probability':0},
    {'reply':[q.louisXVI],'requirements':[],'must':['louis'],'hasArg':True,'probability':0},
    {'reply':[q.tokens],'requirements':['python'],'must':['tokens'],'hasArg':True,'probability':0},
    {'reply':[q.types],'requirements':['python','systems'],'must':[],'hasArg':True,'probability':0},
    {'reply':[q.covalency],'requirements':[],'must':['carbon'],'hasArg':True,'probability':0},
    {'reply':[q.fatherofchem],'requirements':['father','of'],'must':['chemistry'],'hasArg':True,'probability':0},
    {'reply':[q.freefall],'requirements':['free','fall'],'must':[],'hasArg':True,'probability':0},
    {'reply':[q.newton],'requirements':['laws','of'],'must':['motion'],'hasArg':True,'probability':0},  
    {'reply':[q.force],'requirements':['types','of'],'must':['force'],'hasArg':True,'probability':0},
    {'reply':[q.wet],'requirements':[],'must':['work','energy','theorem'],'hasArg':True,'probability':0},
    {'reply':[q.gravity],'requirements':['discovered','discover'],'must':['gravity'],'hasArg':True,'probability':0},
    {'reply':[q.flowchart],'requirements':[],'must':['flowchart'],'hasArg':True,'probability':0},
    {'reply':[q.asciii],'requirements':[],'must':['ascii'],'hasArg':True,'probability':0},
    {'reply':[q.specialascii],'requirements':[],'must':['ascii','speciality'],'hasArg':True,'probability':0},
    {'reply':[q.iscii],'requirements':[],'must':['iscii'],'hasArg':True,'vidurl':'https://www.youtube.com/embed/hW_gJRHF7lU','probability':0},
    {'reply':[q.specialiscii],'requirements':[],'must':['iscii','speciality'],'hasArg':True,'probability':0},
    {'reply':[q.chatbotwhat],'requirements':['what'],'must':['chatbot'],'hasArg':True,'probability':0},
    {'reply':[q.boolean],'requirements':[],'must':['boolean'],'hasArg':True,'probability':0},
    {'reply':[q.primeofind],'requirements':[],'must':['prime','minister','india'],'hasArg':True,'imageurl':"https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Official_portrait_of_Narendra_Modi%2C_2022_%28cropped%29.jpg/300px-Official_portrait_of_Narendra_Modi%2C_2022_%28cropped%29.jpg",'probability':0},
    {'reply':[q.presofind],'requirements':[],'must':['president','india'],'hasArg':True,'imageurl':"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUWFRgVFRUYFRgaGBgYGBgYEhIYGBgYGBgZGRgYGBgcIS4lHB4rHxgYJjgmKy8xNTU1GiQ7QDs0Py40NTEBDAwMEA8QHhISHjQlISw0NjQ0NDQ0MTQ0NDU0NDQ0NDQ0NDQ0NDQ0MTQ1NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0P//AABEIARMAtwMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAABAAIDBAYFB//EAD4QAAIBAgQDBgQEBQMCBwAAAAECAAMRBBIhMQVBUQYiYXGBkTKhsdETQlLBYoKS4fAUI3IzogdDU3OywvH/xAAaAQADAQEBAQAAAAAAAAAAAAAAAQIDBAUG/8QAJxEAAgICAQQCAgIDAAAAAAAAAAECEQMxIQQSQVEFMiJhE6GBkbH/2gAMAwEAAhEDEQA/AO9CY1jHAzA6gXighiABhEaYRAAiK8UJEABDaKOgAxo0R7GAQADCNIjyY0wASwGIxXiAaYrwmNMBhEEQiMACRFaGC8AGRQkRQAmaIRpMfKEKIwGIxAC0cogjlgAbSOvVVFLuwVQLliQAB4mPdwoLE2AFyToABuZ5v2n7QfjtlQkU1+EbZj+o/sI4xsTdHex/bFBpRTP/ABNcL5hdzKydoKrcxr0toeYA5zEO5Jk9GsQdJp20Tdmsq8dqjLz1J1Y9NLzpYDtCGOUkg2Fr2Yam2ttfGZhKmgzEX5RqA7A78x0Nxb6wTXkmUX4N8nEVzhH7rEaX0BvtaXZgzxQIAjkupACsFGZADsGJ18/GdvgPE7rkZ84Gzc1HK/Ub6yZJeCot6kaG0aY5W6QTM0GMYCY9hGGABgaICKACWGACIwARgiigBI0cIDHERiATDGxWgA60Igh8YAY/t3xcKow6nU2Z7dPyr67zAu/haWeL401KruTqzE+Q2A9BaDh/DnqnTQczNVUUZ05PgjoUnc5U9TO1huBbZzfqB+5nd4fwpaagAa9TLei6WkSuRvGMYnNo8MRRYKB67yyuEUW0lm/S/wAo469JizVFCrg0O6g+glKrhygLU2KjUW6+E61VDysfeVXpMu40+vvHGRE4+y72O4iXV6bbpYjwB09pozMj2bp5MU42D0yw9GH95riJRAiYDERADAAgxXivCYCFeNihEABFDFEMfeOJjQIpQgrCI2OWABlfiTkUahG4RyP6TLMqcVJ/BqW3KOAOpKkAe8BHiyG7a9ZuuAICosLadJhjSZXsRYg2IIOh8Z6FwVAlIEnU/wAL/aVLYY9M6dQgDUgeso1+IInxKT6W+sTupa7VECgXv+JYDzLAWnLxPEqBW+mugzM1z6Kpt62idtcGqaXLLycXRzYAjz+8srVB1G0zFNkzWysOfdYDQ89RO+1FAgCutmW+uckeBIX6TOSa5LjKLI8RxGmu/wApEONIdMpYfSc3E0EsGLh7hjlVqgNlZl0BTX4b7jnI6WOoqNENtrm/2EFF7JlNN0aLh9v9TSYG4KVB/wBoP7zVGZXs26M91y6AEXbU3uO7f1v6TT3lMzEYISYDABXhgBhBgAITATFEARFBFGBKYiIIbxiFEsRggA+cXtVmNDKpKl3RbjQ95rTtATn8bX/ZLH8rK3swuYhraMBxDAKK5CMX+G9zdtAASfaa3CLdQvQATl4HClCxfvFzcMBcZdgD0Ph4y9hmINvGNS9mjir4HVOGi+aw/wA8JRqYPOT3LgGw+EDx5Tv0WB3Mr4r8NASDbnobfSJy4svsOfh+CpqSADbZb2HruZOmCupO4GgOlj5eHITlYPEpVqMzvkRCMoLGzN1N+QmipYymVPfDacjf6SHyhxXJmxhPyndWOUHfI1jYeRzf1Rf6K5sUP3lnH1EZviI00II0NtDqNR1HPwkGDxiuveAuDY26j9od1Intt0X+FYRabrsuo0vqSTbaaYCZLDEZxYW1H1muaNS7jOUe1ggIhiMokbDeAQwAJgiJigAiYoLRRASgxCKGUIBhBghEAHgyLE0g6Mp2IIjxDaIZmqyCmqF2XvABBcXHfKAEcjpHWtrMbxjijPWLHYVMyjoFbT6X8yZrKtXTwIuPIwkqRpCVkb4u05ONxLOwRTvueQHOW3AlapSubLox59BpIqzVyaR0aOFphAtgR4gG56m859bAKrZksl+SkD3XaWKODA+N39MoH0MdUoYcc3v/AO5/eU48DikzmVsL3u8wY9b/AC8JCEyPmX1HWWcTTQ3yFh5teV6VMhrEkjxN5NEydOkdThLZ6qL/ABgnyGp+Qm3My3ZjDXqF+SqfdtPpeagwiuDKbtjWgjjGkSyACOEaIQIgCYIhFeMBCKCKAEhEQhgMYgxAxt4gYDJbxSMGOgI8y7b8NFGtmX4agLjwa/eHzv6zocLqlsPTY75St+uVigPymo7Q8MSvSKucpBur/pbb1v0nCpYXJTWnfVBYm3Pn7xtpqisaalZUqtbeHDMM1zvGu99DpIcltjM6o2fJ2lQON7SrU4enMk+o+soLjGXceo+0Jxt+vzilKxqJK+EVdR9ZEtBnZUQXY7QmvcaAnxO3tzmh7NYTKDUbV20HgOcFyRLg6vDcGKSBBqd2PVucsGIvGM8ozHGC8aGizRiDaERuaERDCRFBeEGACtFEYoCCWiLQEyMmUA4vG54xmlrAcPqVj3F7oNi5NlHrz8hBKxN0MBkWJxqpp8TdPuZoq3ZhWWwrsrdSgyn0vce8x3FOF1cO1qi6X0cao3k37HWTPuitF4uyT2Uce71LljfoBsPL7wVHNRS4H+4g/wBwfrUf+YP36HXY6W6aXEY9BlYOhyspuD9RbmCNCOYJnP3O7OvsVcHGxFIMMy69QdLH6gznvTb8p9DoffnO/wARwYK/jUxlFwHS/wADHYeKH8p9PPlsA3xD/PAzXutWRRzWLDQ3HpD6y49Fv+Q8fvKjm3I+5iTQNNEiOR/m01XZ7EqUyZhnBJy5hmy3+K29rneZHWabsjb8SmHUNepl13y1siNa2xBUEGVFiWKWS69N/wCjus8YXmqq9j73y1vIMnyJB/acXG9ncSlzkzjqhzf9vxfKauLRxqcX5OeHhV5WzdY5akkssho8NKweSK8QEwMN5GGjgYDHXigWKAhrNI3aJ2lvg2B/GqhT8C95/wDjfQeZOnvKStibovcA4F+LZ6lwnJeb+JPJfrNb8ACqoVRoABYSVCFAAAAAtYdIPxJ0RjRhJtkTVAw1Eq1aehXRlOhVgCCOhB0Mt1EB1GhkCG9xzjEZrGdmUJzUG/CY/ka7UyfA7r8x4ThYzD1KbZaqlTyO4YdVOxE37ryMgqqpXLUUOh5HW3keU554Yy1wdOPqJR3yjzoNlbMAG3DKfhZT8SsOh/vKOLwIHfS5Qk2vqVO5Rv4h15jXy2fFuzRAz0LsvNd2Xy/V9fOZm5Qm40OjrtcDbfZhyPL3nJKMoOmdsZxmrichadpDi8OrDXQ9Z1MfQyWIIZWF1YbML2PkQdCORnDdix8L2HjGmbYsLyypEtLAsQCbAdOonU4CpbEUUXcVEPkFZSZWaobBBvotvHkJ0+yOGKYykCpLM4VjyFgXsP6DNI8tHo5Iw6fBJLdP/h7Ej6nzI+kkZv7Smza38z63/sJOrXU+BnWj5Boo8S4RRrC7oM36l7re439bzMYvse4uaTq/8Ld1reexPtNmj3/eMY2MTimOMmtHmuJwFWl/1EZPEi6/1DSQo89RL8j/AJ5zlY7g+HqXzJ+G361GX6d0+shx9Gscl7RiFaPSXuI8Del3gQ6fqGh9RynPUyGqNvFk4ijVMUAIXM1/ZjDZaKtzclz5XyqPYX9TMdUM9BwCZaVNeYRAfPKLzXGuTKeiwWgvGXhvpNjIBe/nGNrqNx8xE/8Ahjc3v9REwH1CGFxEiZhrIlazAcnvbzte3yPtJsMbtl5ARAMUZTpKfFuFUsRv3Gto6gX8mH5hLyjM5ttOL2s4sMLQd1tn0VAebnbTnYXPpIkk070a4lKU1GO2ef8AaKm1Bmw5ZWvla6sTl10I5qxUWIPK3QGcvDLdhptKRrMzF3YszEsxO5J3Jml4JhCF/EYaHVbjcfq8ZxUr4PsOnxxwYud+f2y5heEsLVTudAOnPXo37TU8Kw6u9NsrK1Ji5I+Fro1NQfE5z/TOXwzEN+IqqL5iFKH4W1+Vt78tZvMNRRO6oAF7nnc73ud51Qijw/keokuJbeq9Bb4rdAB8ocO+pHUA/KQI13J8YC9iPAL9BNTxWidGsxEkrLcSo7d68u30gIrZ9ITUsLgE9QOkjY2JjUcWN9JJSRy+KYfQ1aRsNc6D4SOZy9eonnXFuINTxBtopVTl5a32np+MpMRmptZt+RVx0P3nmnbWgCFqqMtiUdf0k66eFwdPGY5Fwez8dKLfbNWnwdLA4gVFDDnf5RSPhNDJSRTvlufM6n5mKJaOTJXfLt1fBYw1Au6INczAel9fleeivMf2Upg1mY/lQ28yQL+1/ea+pOjGuLOSb5IxApiG8Q5zQgDGVy0meQNExoirv8Ntw6H0zAE+xl4KRe27aD9zObiCLXJy21v0HMzsmqoQvcAAbkgAAa3J5SUUUuIY6lhqZeowVRudSSTsABqT4Tx3tHxZ8VVzt3VGiJ+lfH+I8z9p1O0vGmxNQgH/AG1Y5B+rlnPny6A+JnBFBmbKBr9B1M5cuTu/FaPqfj/j1hh/JP7P+gYHD53At3Rv9p6Lw6kpslTLkIGUnQq3I328NfppM1wzDqjKjC6kjMR8Qvuw+02y8EdnWxBQ2JZTsAL+55eYhjiZ9dnj9ZOvTOlw3gyUWNQXJIsoP5QdyPp5TpIMqs3hYf5/m0aWudNhYAfSLGtYKvvOmktHzU5ubtu2R4cSHEN3iPAfQSajK1c99vOIglB0lmjUuJBTGkfRNjaAmDEGQo0lxQlVD0iZSI8XTampelsNSn5fEr+nyGkwPazHLcva4cISp/WG1+nznoaYi/ccZWttyYdVPMeG4nmHb7DlKiKo7rZioHjlFh66TPJo9PoKeRKW/ftHXwtYOqsNmFx9opX4Rg/w6Spz3PmdT9vSKSc+RVN9ujT9jl79Q9FUe5P2mnczM9jW71UfwofYtb6maNzOmH1Oaf2AIhv6RCI7iWQNqSBpO0gYRMaKOOUFWU63Vh7gicHtpxwCjTw1I6uqvUIOoQgFV/m5+A8Z2uJEhSRvPLKVc1GZ230HkFAUD0AA9JhllUaR7HxXTRy5lKWlz/kfTQ7AXJmo4RwUMpClTUtcgkC/gL9PUHwlHhuCI7zDU/COg6+c69GoyEFGIYcx+/UTCEa5Z7vVZXKLjjdDKfCKivqjW0tYE77fbz9JuMIDRpKhN2I1/hB1t6R3D8SrotW3ha4N25+0eaGc5r+k6IxUdHy3VdTLJ+MlVP8Asnwyczy1+0q13zMTy2Es13yJbmZTvKfo4l7J8N/npr+0p87+MuqbKfI/aU0EQyzThvrAkLmMQ2u0proZYc6yNl1iZSFiaYdCp6aHmDyImAxZaq9MPq1J2157EEH+YKZtcUDTVnW5XUul/dk6HqNj5zC8drfhs7rswDoeRzf3mc2eh0kbtLzr9M6SiKQ4SuHRXH5gD5dRFEc84tOmd/see9V/4p9WmkaZfsk/+446pf2ZfvNO06IfUwlsAibl5wLC40lkhNpGdNxJFNxGFYmBQ4jSDIfKeXdnML/u1S4OWm7LsD3gzW0uLgDW1xy1nq9aYmtQWniKqBTd2WoFAvmZ1C2A80J9ZhkjfJ6fx+Vxk17R2qXBWdc9NgykXAIKtfmpv8j/APsI7O1i1rhRcXY32N9l66beM6fZ2jVpgioMinZSwLDx7rFV+s61arePtjViydZlhJxi017KYsqqqiyqLAfufEy9SewzeEpU1uZYxD2GUf4YJ+ThlzsrvVLtcwneBY6mO9Alk+INk87D9/3ldP2kmNa5C9I2nH5F4JUiqnSImV6tbW0GwSEpieJTE0QyGrVGqMCCdr7OOdj18N55Z2mchFS+gdh7cvexnquNQMhHseh5EeU8h7TljWCczqf+Tmx+YMyyaPT+NrvO12bQigpP5ixHle37X9YJ1MPTCqEA0UAD0FoIJcHLml/Jkcjo9mXtXA/Urr8s3/1muMxHC6mWvTP8YH9XdP1m3M6MejnlsAjjGiOmhmRoeUawhA1jXiGQ1W6+/wB5ysPQBxaPzFKov83dKkehf3nTqykulWmw/UwPkVbSRI0i2rovK5U67Sde9tElPNykjIE+E68/CJhZJYIPH6f3lQam8Ja+8eokMNDWGkdhhrfprGsYHbKni2npAKI2fMxPjHh5XEekVhRK7WF5UQ3Mmqm8gpwYJFpWiZo2NtAKKuLrsh7xBRjodijW2PVTb0PnMdxXhJfGq4FwqNUPSykWI/mf5TUdpFzUmA5ANv0IJ+V5weHcQKsinUMTRN+QqjKB5Zsh8ryXy6Z3YFJRco7polWKOqUmUlToQbH0igcpVYkajcaiegrUDAMNmAYeovMAxsb9Df2noLkGxGxAIm2PyZTBHKYwGPWamY2pbf8AaRO4tJnWQ3vvExldrEaG46icuuGzoBvn9tDrL+JpKNVOVuoBHuOc5eJqsHS41zG5G2o0I+ftMpMuJsKSBV8espVmuZO9buKeoBlMtG2JIBEGYiEmN3kFj6YzHw5yCs+Zr8hoPKWaiZVy8zv5dJWcWiYIYWhz8owR9NNYDHsNJDSlnEaCV6MGIstGObCPc7eUgxL8oMSOYzG7I5ve5U7Eqdx6faYXjdRqVlGjBwR/J3gffLNL2mfvIOdid/H+0xXG65ZwCb5FA99fplmUme10GO/y8Pwb/HnMwflUVHB65lBil2vQZcFRpnKMqUgwBB1CAG3rFNDyW0mzg1JucG+ahTb+Bb+2vzBmGabTs82bCp/DnHsxI+RE0x7M56LIMeDIgY4GbGZOrjnIaiqDvbpfSSI3gIHA2KiAirUUHkD8x8pxOIDVdLd7UfbwvO5Vog/kC+uWc3GYRitgcx3ADXNxMpK0aRfJ0mrZlW2lgBbyjAZz8G5+E8tD4ES/lk3Y9BlqggAzH085Fh6dzJ6rchsI0vIN+CF9TeVKxlx5RrnWSwQkEs0VkKLLVIQQMixe0r4YSbFmDDrF5DwLENacvHu4IdBmA+JOZHVfES/im1AkDbxMuLp2ZPtNiQSlQG6ZTr4jUjz1mLoo1Zwqi71HsAOrHT0H7Tt9ta2Wo1IcznO3MA8vH/4yf/w6wAqYhmOyISPBmYKPlmmTXdKj3sL/AIeneT9cHo5Smo7xAFgO8CBDLK0LC1wR0YXEU6aPnO4wtSbDsgh/AN+bsR7AfUGY12m67MJbDU/EMT6uSPlaKGyp6H1BYkQiScRW1mHkfOV6VSbmZKBJAW6gfWAQgRgQ1GS9zqZWFQnREsOdv3Mvmmu5F/pIsRc/CQvh9pDQFF8OR3jlX94+hUubRrheZLn2EYaliCABbYAfvIaKTOw3dFuZkaiV8PWzHXeWjDYEFQymRrLbyHJIZSColhBI0WSjaNAyniNWkqDeRvq0WIewPUyRlOoxJJG+tv2lXCYoPe4ysDZlO4P2lxBOJx2iQBUXQiwYi97E6beNt4ma44xk+1+fJhO1r5sXV8CoHoi/3noP/hvwwJQZ2FmchvHLrlH1P8089TDNiMaUPevU73/FT3j7Ce68NoZEAAtoLADkJOKNybPQ+QzdmGOFelZEw1ilqqOoim54h5e/Oel4BAtJABYBF09BFFFA0mNxnwN5TjoYopsiUXKBlmKKAmQ1WPU+5kdFBm2iigwFXQX2kbILbRRSWAyiNAfH95eTaKKQiiN4wwxSWMcJJygigBW/NK+J3hikjRGnwyhxH/pP/wAW+kUUT0a4/sjzX/VvSfE1KZyuKpUNlUkAsdBceE7p4lWYXatVOn/qvb2vaKKQzrz/AGIG7QYqiyinXcA3uGbONjsHuB6RRRRx0cs0rP/Z",'probability':0},
    #{'reply':[str(q.web())],'requirements':['web','browser','chrome','search'],'must':['search','web'],'hasArg':True,'probability':0},
    #{'reply':str(news()),'requirements':['news'],'must':['current','affairs'],'hasArg':False,'probability':0},

    {'reply':geoformulas.areaOfSquare,'requirements':[],'must':['area','square'],'hasArg':True,'probability':0},
    {'reply':geoformulas.perimeterOfSquare,'requirements':[],'must':['perimeter','square'],'hasArg':True,'probability':0},
    {'reply':geoformulas.areaOfCircle,'requirements':[],'must':['area','circle'],'hasArg':True,'probability':0},
    {'reply':geoformulas.perimeterOfCircle,'requirements':[],'must':['perimeter','circle'],'hasArg':True,'probability':0},
    {'reply':geoformulas.areaOfRectangle,'requirements':[],'must':['area','rectangle'],'hasArg':True,'probability':0},
    {'reply':geoformulas.perimeterOfRectangle,'requirements':[],'must':['perimeter','rectangle'],'hasArg':True,'probability':0},
    {'reply':geoformulas.areaOfTriangle,'requirements':[],'must':['area','triangle'],'hasArg':True,'probability':0},
    #{'reply':geoformulas.perimeterOfTriangle,'requirements':[],'must':['perimeter','triangle'],'hasArg':True,'probability':0},
]
if responses == [str(long.unknown)]:
    pass
def getProbability(wordlist):
    tempMark = 0
    for x in responses:
        for y in wordlist:
            if y.lower() in x['requirements']:
                tempMark += 5
            if y.lower() in x['must']:
                tempMark += 10
        x['probability'] = tempMark
        tempMark = 0

def getBotResponce(message):
    index = 0
    temphigh = 0

    arguments = {}
    flag = False
    arg = ""

    getProbability(message.split(" "))
    for x in range(len(responses)):
        if temphigh < responses[x]['probability']:
            index = x
            temphigh = responses[x]['probability']

    if responses[index]['hasArg'] == True and len(arguments.keys()) > 0:
        return(responses[index]['reply'](arguments))
    else:
        return(responses[index]['reply'][random.randint(0,len(responses[index]['reply']))-1])

def getBotImage(message):
    index = 0
    temphigh = 0

    arguments = {}
    flag = False
    arg = ""

    getProbability(message.split(" "))
    for x in range(len(responses)):
        if temphigh < responses[x]['probability']:
            index = x
            temphigh = responses[x]['probability']

    if 'imageurl' in responses[index].keys():
        return(responses[index]['imageurl'])
    # print(responses[index].keys())

def getBotVid(message):
    index = 0
    temphigh = 0

    arguments = {}
    flag = False
    arg = ""

    getProbability(message.split(" "))
    for x in range(len(responses)):
        if temphigh < responses[x]['probability']:
            index = x
            temphigh = responses[x]['probability']

    if 'vidurl' in responses[index].keys():
        return(responses[index]['vidurl'])
        # print(responses[index].keys())

#while True:
#    global user
#    user = input("User: ")
#    getProbability(user.split(" "))
#    print("Bot: "+getResponce() + "\n")