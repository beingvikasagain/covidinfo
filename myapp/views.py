from django.shortcuts import render
import requests
import time
from bs4 import BeautifulSoup
# Create your views here.
def mycovidinfo(request):

    covid_data = {}
    url = 'https://www.worldometers.info/coronavirus/'
    r_data = requests.get(url)
    ar_data = BeautifulSoup(r_data.content,'lxml')
    total_detail = ar_data.select('div.content-inner')
    last_updated = total_detail[0].select('div')
    latest_time = last_updated[1].text.split('d:')[1].strip()

    total_cases = total_detail[0].select('div.maincounter-number')[0].text.strip()
    total_deaths = total_detail[0].select('div.maincounter-number')[1].text.strip()
    total_recovered = total_detail[0].select('div.maincounter-number')[2].text.strip()
    currently_infected = total_detail[0].select('div.panel_front')[0].select('div')[0].text
    covid_data['lastest_data']=latest_time
    covid_data['total_cases'] = total_cases
    covid_data['total_deaths'] = total_deaths
    covid_data['total_recovered'] = total_recovered
    covid_data['currently_infected'] = currently_infected
    time.sleep(3)
    return render(request,'myapp/index.html',context=covid_data)
