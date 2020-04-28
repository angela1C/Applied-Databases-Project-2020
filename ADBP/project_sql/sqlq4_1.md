
# 4.1.1 Alan’s travel details
Give the MySQL command that shows:
- The name of the cities
- The Arrival Date in the cities
- The name of the country the city is in

For all cities and countries visited by “Alan” in alphabetical order by city name.
```sql
select c.Name as name, h.dateArrived, co.Name as name
from person p
inner join hasvisitedcity h
on h.personID = p.personID
inner join city c
on h.cityID = c.ID
inner join country co
on c.CountryCode = co.Code
where p.personname ="Alan"
order by c.Name
;
```
#### Expected results for 4.1.1

name	dateArrived	name
Arnhem	2002-04-14	Netherlands
Purulia	2002-06-20	India
Suzhou	2002-01-30	China
Tama	2009-02-13	Japan


#### my results for 4.1.1
```
+---------+-------------+-------------+
| name    | dateArrived | name        |
+---------+-------------+-------------+
| Arnhem  | 2002-04-14  | Netherlands |
| Purulia | 2002-06-20  | India       |
| Suzhou  | 2002-01-30  | China       |
| Tama    | 2009-02-13  | Japan       |
+---------+-------------+-------------+
4 rows in set (0.00 sec)
```


***


### 4.1.2 European countries with lower than average life expectancy
Give the MySQL command to show the country name the country’s life expectancy for all countries in Europe whose life expectancy is lower than the average in alphabetical order by country name.

#### Expected results for 4.1.2 

name	lifeexpectancy
Moldova	64.5
Ukraine	66.0

```sql
select Name as name, LifeExpectancy as lifeexpectancy from country where continent = "Europe" and LifeExpectancy < (
    select avg(lifeExpectancy) as lifeexpectancy from country
) order by Name;
```

#### my results for 4.1.2
+---------+----------------+
| name    | lifeexpectancy |
+---------+----------------+
| Moldova |           64.5 |
| Ukraine |           66.0 |
+---------+----------------+


***


### 4.1.3 Peoples stage of life
Give the SQL command to show the following in ascending personID order:
- The person’s ID
- The person’s name
- The Person’s age
- A column called Stage that shows the following:


```sql
select *, 
case 
    when age < 18 then "Child" 
    when age < 29 then "Late teens/Twenties" 
    when age < 39 then "Thirtysomething" 
    else "Other" 
END as "Stage" 
from person 
order by personID;
```
#### Expected results for 4.1.3
personID	personname	age	Stage
1	Tom	33	Thirtysomething
2	Alan	23	Late teens/Twenties
3	Sean	30	Thirtysomething
4	Sara	25	Late teens/Twenties
5	Jane	25	Late teens/Twenties
6	Michael	19	Late teens/Twenties

#### my results for 4.1.3
+----------+------------+------+---------------------+
| personID | personname | age  | Stage               |
+----------+------------+------+---------------------+
|        1 | Tom        |   33 | Thirtysomething     |
|        2 | Alan       |   23 | Late teens/Twenties |
|        3 | Sean       |   30 | Thirtysomething     |
|        4 | Sara       |   25 | Late teens/Twenties |
|        5 | Jane       |   25 | Late teens/Twenties |
|        6 | Michael    |   19 | Late teens/Twenties |
+----------+-

#### Expected results for 4.1.3
personID	personname	age	Stage
1	Tom	33	Thirtysomething
2	Alan	23	Late teens/Twenties
3	Sean	30	Thirtysomething
4	Sara	25	Late teens/Twenties
5	Jane	25	Late teens/Twenties
6	Michael	19	Late teens/Twenties


***
### 4.1.4 Capitals and Official Languages of North America
Give the SQL command to show for each country in North America:
- The name of the capital city
- The name of the country
- The official language(s)
- The percentage of people who speak the official language(s)
The results should be alphabetical city name order, and within that by country name order, and within that by language order, and within that by ascending percentage.




```sql
select ci.name, co.name,cl.language, cl.percentage from country co
inner join city ci 
on ci.ID = co.capital
inner join countrylanguage cl
on co.code = cl.CountryCode
where continent = "North America" and cl.IsOfficial = "T" order by ci.name, cl.language, cl.percentage;
```

#### Expected results for 4.1.4
Ciudad de Guatemala	Guatemala	Spanish	64.7
Ciudad de MÇxico	Mexico	Spanish	92.1
Ciudad de Panam†	Panama	Spanish	76.8
Cockburn Town	Turks and Caicos Islands	English	0.0
Fort-de-France	Martinique	French	0.0
George Town	Cayman Islands	English	0.0
Hamilton	Bermuda	English	100.0
Kingstown	Saint Vincent and the Grenadines	English	0.0
La Habana	Cuba	Spanish	100.0
Managua	Nicaragua	Spanish	97.6
Nuuk	Greenland	Danish	12.5
Nuuk	Greenland	Greenlandic	87.5
Oranjestad	Aruba	Dutch	5.3
Ottawa	Canada	English	60.4
Ottawa	Canada	French	23.4
Plymouth	Montserrat	English	0.0
Port-au-Prince	Haiti	French	0.0
Road Town	Virgin Islands, British	English	0.0
Saint JohnÔs	Antigua and Barbuda	English	0.0
Saint-Pierre	Saint Pierre and Miquelon	French	0.0
San JosÇ	Costa Rica	Spanish	97.5
San Juan	Puerto Rico	Spanish	51.3
San Salvador	El Salvador	Spanish	100.0
Santo Domingo de Guzm†n	Dominican Republic	Spanish	98.0
Tegucigalpa	Honduras	Spanish	97.2
The Valley	Anguilla	English	0.0
Washington	United States	English	86.2
Willemstad	Netherlands Antilles	Dutch	0.0
Willemstad	Netherlands Antilles	Papiamento	86.2


#### my results for 4.1.4

```

| name                     | name                             | language    | percentage |
+--------------------------+----------------------------------+-------------+------------+
| Basse-Terre              | Guadeloupe                       | French      |        0.0 |
| Basseterre               | Saint Kitts and Nevis            | English     |        0.0 |
| Belmopan                 | Belize                           | English     |       50.8 |
| Bridgetown               | Barbados                         | English     |        0.0 |
| Castries                 | Saint Lucia                      | English     |       20.0 |
| Charlotte Amalie         | Virgin Islands, U.S.             | English     |       81.7 |
| Ciudad de Guatemala      | Guatemala                        | Spanish     |       64.7 |
| Ciudad de México         | Mexico                           | Spanish     |       92.1 |
| Ciudad de Panamá         | Panama                           | Spanish     |       76.8 |
| Cockburn Town            | Turks and Caicos Islands         | English     |        0.0 |
| Fort-de-France           | Martinique                       | French      |        0.0 |
| George Town              | Cayman Islands                   | English     |        0.0 |
| Hamilton                 | Bermuda                          | English     |      100.0 |
| Kingstown                | Saint Vincent and the Grenadines | English     |        0.0 |
| La Habana                | Cuba                             | Spanish     |      100.0 |
| Managua                  | Nicaragua                        | Spanish     |       97.6 |
| Nuuk                     | Greenland                        | Danish      |       12.5 |
| Nuuk                     | Greenland                        | Greenlandic |       87.5 |
| Oranjestad               | Aruba                            | Dutch       |        5.3 |
| Ottawa                   | Canada                           | English     |       60.4 |
| Ottawa                   | Canada                           | French      |       23.4 |
| Plymouth                 | Montserrat                       | English     |        0.0 |
| Port-au-Prince           | Haiti                            | French      |        0.0 |
| Road Town                | Virgin Islands, British          | English     |        0.0 |
| Saint John´s             | Antigua and Barbuda              | English     |        0.0 |
| Saint-Pierre             | Saint Pierre and Miquelon        | French      |        0.0 |
| San José                 | Costa Rica                       | Spanish     |       97.5 |
| San Juan                 | Puerto Rico                      | Spanish     |       51.3 |
| San Salvador             | El Salvador                      | Spanish     |      100.0 |
| Santo Domingo de Guzmán  | Dominican Republic               | Spanish     |       98.0 |
| Tegucigalpa              | Honduras                         | Spanish     |       97.2 |
| The Valley               | Anguilla                         | English     |        0.0 |
| Washington               | United States                    | English     |       86.2 |
| Willemstad               | Netherlands Antilles             | Dutch       |        0.0 |
| Willemstad               | Netherlands Antilles             | Papiamento  |       86.2 |


```

***
### 4.1.5 Length of Stays
Give the SQL command to show for each country person:
- The person’s name
- The name of the city the person visited
- A column called Stay Length that shows the following:


The results should be sorted alphabetically by personname, and within that by city name.


```sql
select p.personname, c.name,
case 
when datediff(h.dateLeft, h.dateArrived) <20 then "Short"
when datediff(h.dateLeft, h.dateArrived) <99 then "Long"
else "Very Long"
End as "Stay Length"
from person p
inner join hasvisitedcity h
on p.personID = h.personid
inner join city c
on h.cityID = c.id 
order by p.personname, c.name;
```

#### Expected results for 4.1.5
personname	name	Stay Length
Alan	Arnhem	Very Long
Alan	Purulia	Long
Alan	Suzhou	Very Long
Alan	Tama	Very Long
Michael	Gua°ba	Long
Michael	Nagoya	Very Long
Michael	Saint Helier	Short
Sara	Jaunpur	Very Long
Sara	Saint Helier	Short
Sara	ZÅrich	Long
Sean	Dordrecht	Very Long
Sean	Shangqiu	Very Long
Tom	Dordrecht	Very Long
Tom	Muntinlupa	Very Long
Tom	S∆o Lourenáo da Mata	Short
Tom	Suzhou	Long
Tom	Sydney	Very Long
Tom	Tanjung Pinang	Very Long


#### my results for 4.1.5

+------------+------------------------+-------------+
| personname | name                   | Stay Length |
+------------+------------------------+-------------+
| Alan       | Arnhem                 | Very Long   |
| Alan       | Purulia                | Long        |
| Alan       | Suzhou                 | Very Long   |
| Alan       | Tama                   | Very Long   |
| Michael    | Guaíba                 | Long        |
| Michael    | Nagoya                 | Very Long   |
| Michael    | Saint Helier           | Short       |
| Sara       | Jaunpur                | Very Long   |
| Sara       | Saint Helier           | Short       |
| Sara       | Zürich                 | Long        |
| Sean       | Dordrecht              | Very Long   |
| Sean       | Shangqiu               | Very Long   |
| Tom        | Dordrecht              | Very Long   |
| Tom        | Muntinlupa             | Very Long   |
| Tom        | São Lourenço da Mata   | Short       |
| Tom        | Suzhou                 | Long        |
| Tom        | Sydney                 | Very Long   |
| Tom        | Tanjung Pinang         | Very Long   |
+------------+------------------------+-------------+
18 rows in set (0.00 sec)



