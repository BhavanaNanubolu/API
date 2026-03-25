from django.shortcuts import render
import requests

def index(request):
    
    data = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,flags").json()

    if request.method == 'POST':
        con = request.POST.get('country')
        res= requests.get(f"https://restcountries.com/v3.1/name/{con}?fields=name,capital,region,subregion,borders,area,maps,population,timezones,continents,currencies,languages,latlng,flags,coatOfArms,startOfWeek,postalCode,independent?status=true,car").json()
        a=res[0]
        return render(request, 'single.html', {'a': a, 'data': data})
    context={'data': data}
    return render(request, 'index.html',context)