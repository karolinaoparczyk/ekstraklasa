import urllib3
from bs4 import BeautifulSoup
import requests

from get_teams import get_first_team_list, get_teams_and_points

teams = []

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_piłce_nożnej_(2017/2018)'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_first_team_list(soup, teams)

url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2016/2017)'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_teams_and_points(soup, teams, 5)

url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2015/2016)'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_teams_and_points(soup, teams, 5)

url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2014/2015)'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_teams_and_points(soup, teams, 5)

url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2013/2014)'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_teams_and_points(soup, teams, 5)

url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2012/2013)'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_teams_and_points(soup, teams, 1)

url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2011/2012)'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_teams_and_points(soup, teams, 1)

url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2010/2011)'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_teams_and_points(soup, teams, 1)

url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2009/2010)'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_teams_and_points(soup, teams, 1)

url = u'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2008/2009))'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
get_teams_and_points(soup, teams, 1)

teams.sort(key=lambda x: x.score, reverse=True)
for index, team in enumerate(teams):
    print(index, team.name, team.score)