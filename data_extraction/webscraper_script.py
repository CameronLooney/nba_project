import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver



def years_to_scrap():
    years = list(range(1990, 2023))
    return years


def get_url(year):
    url_template =  "https://www.basketball-reference.com/awards/awards_{}.html"
    url = url_template.format(year)
    return url

def fetch_data_mvp():
    df_list  = []
    years = years_to_scrap()
    for year in years:
        url = get_url(year)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        soup.find("tr", class_="over_header").decompose()
        mvp = soup.find(id="mvp")
        data = pd.read_html(str(mvp))[0]
        data["Year"] =str(year)
        df_list.append(data)
    df = pd.concat(df_list)


    return df



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def all_players_html_page(year):
    driver.get("https://www.google.com")
    url_template = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"
    driver.get(url_template.format(year))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    html = driver.page_source
    return html

def fetch_all_players_data():
    years = years_to_scrap()
    df_list = []
    for year in years:
        html = all_players_html_page(year)
        soup = BeautifulSoup(html, "html.parser")
        soup.find("tr", class_="thead").decompose()

        players_dataframe = soup.find( id="per_game_stats")
        player = pd.read_html(str(players_dataframe))[0]
        player = player[player["Player"] != "Player"]
        player["Year"] = str(year)
        df_list.append(player)
    df = pd.concat(df_list)
    return df

#fetch_all_players_data()
def generate_url(year,url):
    url_template = url
    url = url_template.format(year)
    return url

def fetch_standings():
    df_list = []
    years = years_to_scrap()
    for year in years:
        url = generate_url(year,"https://www.basketball-reference.com/leagues/NBA_{}_standings.html")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        soup.find("tr", class_="thead").decompose()
        team_table = soup.find(id="divs_standings_E")
        team = pd.read_html(str(team_table))[0]
        team["Year"] = str(year)
        team["Team"] = team["Eastern Conference"]

        team.drop("Eastern Conference", axis=1, inplace=True)
        df_list.append(team)

        soup = BeautifulSoup(response.text, "html.parser")
        soup.find("tr", class_="thead").decompose()
        team_table = soup.find(id="divs_standings_W")
        team = pd.read_html(str(team_table))[0]
        team["Year"] = str(year)
        team["Team"] = team["Western Conference"]

        team.drop("Western Conference", axis=1, inplace=True)
        df_list.append(team)

    df = pd.concat(df_list)
    return df




