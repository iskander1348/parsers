function getdata(estate, name){
    

xhr = new XMLHttpRequest();
xhr.open('get', estate, false)
xhr.send()


tmp = xhr.responseText.slice(0, xhr.responseText.search(name))
tmp = tmp.slice(tmp.lastIndexOf('src')+5)
photo = tmp.slice(0, tmp.search('"'))

 
 tmp = xhr.responseText.slice(xhr.responseText.search(name))
 tmp = tmp.slice(tmp.search('tel:'))
 phone = tmp.slice(4, tmp.search('"'))
 return [photo, name, phone]
 }


tmp = document.getElementsByClassName('flex flex-wrap max-w-full w-full self-end items-start justify-start')[0].getElementsByTagName('img');
names = []
for (t of tmp){
    names.push(t.alt)
}


objectname = document.getElementsByTagName('h2')[0].textContent

estate = document.getElementsByClassName('flex flex-wrap max-w-full w-full self-end items-start justify-start')[0].getElementsByTagName('a')[0].href

managers = []
 for (name of names){
	managers.push(getdata(estate, name))
 }
 
 
 console.log(objectname)
 console.log(managers)
