import re

from team import Team


def get_first_team_list(soup, teams):
    for index, link in enumerate(soup.find_all('table', class_='wikitable')):
            if index == 5:
                    team = link.find_all_next("td", align='left')
                    for indeks, title in enumerate(team):
                        name = title.find('a').get('title')
                        if indeks < 16:
                            pattern = '.*piłka nożna.*'
                            result = re.match(pattern, str(name))
                            if result:
                                team_obj = Team(name[:-14], 0)
                            else:
                                team_obj = Team(name, 0)
                            teams.append(team_obj)
                    point = link.find_all_next("b")
                    count = 0
                    for ind, pnt in enumerate(point):
                        if ind < 26:
                            pattern = '<b>[0-9][0-9]</b>'
                            result = re.match(pattern, str(pnt))
                            if result:
                                p = str(pnt)[3:5]
                                teams[count].add_points(int(p))
                                count = count + 1


def get_teams_and_points(soup, teams, param):
    for index, link in enumerate(soup.find_all('table', class_='wikitable')):
            team_count = 0
            if index == param:
                    team = link.find_all_next("td", align='left')
                    indeks = 16
                    for title in team:
                        if indeks > 0:
                            point = link.find_all_next("b")
                            name = title.find('a').get('title')
                            pattern = '.*piłka nożna.*'
                            result = re.match(pattern, str(name))
                            found = False
                            team_count = team_count + 1
                            if result:
                                idx_tm = 0
                                for idx, tm in enumerate(teams):
                                    pat = str(tm.name)
                                    res = re.match(pat, str(name[:-14]))
                                    if res:
                                        found = True
                                        idx_tm = idx
                                        break
                                if found is False:
                                    idx_tm = teams.__len__()
                                    team_obj = Team(name[:-14], 0)
                                    teams.append(team_obj)

                                count = 0
                                for ind, pnt in enumerate(point):
                                    pattern = '<b>[0-9][0-9]</b>'
                                    result = re.match(pattern, str(pnt))
                                    if result:
                                        count = count + 1
                                        if count == team_count:
                                            p = str(pnt)[3:5]
                                            teams[idx_tm].add_points(int(p))
                                            break
                            else:
                                idx_tm = 0
                                for idx, tm in enumerate(teams):
                                    pat = str(tm.name)
                                    res = re.match(pat, str(name))
                                    if res:
                                        found = True
                                        idx_tm = idx
                                        break
                                if found is False:
                                    idx_tm = teams.__len__()
                                    team_obj = Team(name, 0)
                                    teams.append(team_obj)

                                count = 0
                                for ind, pnt in enumerate(point):
                                    pattern = '<b>([0-9][0-9])</b>'
                                    result = re.match(pattern, str(pnt))
                                    if result:
                                        count = count + 1
                                        if count == team_count:
                                            p = str(pnt)[3:5]
                                            teams[idx_tm].add_points(int(p))
                                            break
                        indeks = indeks - 1
