
## An overview of the MySQL queries for section 4.1, workings and solutions.


### 4.1.1 Alan’s travel details
Give the MySQL command that shows:
- The name of the cities
- The Arrival Date in the cities
- The name of the country the city is in

For all cities and countries visited by “Alan” in alphabetical order by city name.



1. What tables are the data in?

- This data is split across several tables.
- Alan's `personname` and `personID` are in the `person` table. 
- The `cityID` field of the cities visited by Alan and the `dataArrived` field are in the `hasvisitedcity` table.
- The  city `ID`, `Name` and `CountryCode` fields are in the `city` table.
- The country `Code` and `Name` are in the `country` table.


2. How are the tables linked?


- While the `person` table does not have a foreign key itself, there is a foreign key pointing in to it from the `hasvisitedcity` table. 
- The `hasvisitedcity` table has two foreign key constraints:
    1. it's `cityID` field references the `id` field in the `city` table
    2. the `personid` field  references the `personid` in the `person` table

- The `city` table has a foreign key called `CountryCode` which references the `code` field in the `country` table.
-  The `countrylanguage` table has a foreign key `CountryCode` field which references the `code` field in the `country` table.


3. Getting the data.

- Get Alan's `personId` from the `person` table.
- Use this to find the cityID's of the cities visited from the `hasvisitedcity` table. where `person.personid = 2. 
- with the cityID field from `hasvisitedcity`, match to the `ID` field in the `city` table and get the city `Name` and `CountryCode` fields.
- with the `CountryCode` field from the `city` table, match to the `Code` field in the `country` table.

- While the `person` table does not have a foreign key itself, there is a foreign key pointing in to it from the `hasvisitedcity` table. 
 - See the `hasvisitedcity` table which has the following foreign key constraint:
 - (CONSTRAINT `fk_personid` FOREIGN KEY (`personID`) REFERENCES `person` (`personid`))


### Find Alan's personal id. in the `person` table.

```sql
 select * from person where personname = "Alan";
```
 
+----------+------------+------+
| personID | personname | age  |
+----------+------------+------+
|        2 | Alan       |   23 |
+----------+------------+------+

```

### Find the cities that Alan visited in the `hasvisitedcity` table

```sql
select h.cityID, h.dateArrived 
from person p
inner join hasvisitedcity h
on h.personID = p.personID
where p.personname ="Alan";
```
 
 ```
+--------+-------------+
| cityID | dateArrived |
+--------+-------------+
|     18 | 2002-04-14  |
|   1358 | 2002-06-20  |
|   1678 | 2009-02-13  |
|   2133 | 2002-01-30  |
+--------+-------------+
4 rows in set (0.00 sec)
```

### Find the city Name and country code from the `city` table

- with the cityID field from `hasvisitedcity`, match to the `ID` field in the `city` table and get the city `Name` and `CountryCode` fields.


```sql
select h.dateArrived, c.Name, c.CountryCode
from person p
inner join hasvisitedcity h
on h.personID = p.personID

inner join city c
on h.cityID = c.ID
where p.personname ="Alan"
;
```
```
+-------------+---------+-------------+
| dateArrived | Name    | CountryCode |
+-------------+---------+-------------+
| 2002-04-14  | Arnhem  | NLD         |
| 2002-06-20  | Purulia | IND         |
| 2009-02-13  | Tama    | JPN         |
| 2002-01-30  | Suzhou  | CHN         |
+-------------+---------+-------------+
4 rows in set (0.00 sec)

```

### Find the Country `Name from the `country` table
- with the `CountryCode` field from the `city` table, match to the `Code` field in the `country` table.

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
```
name	lifeexpectancy
Moldova	64.5
Ukraine	66.0
```


All the details for this question are in the country table.
Note it is not specifying the average life expectancy for Europe.!

```sql
mysql> select avg(lifeExpectancy) as lifeexpectancy from country;
```

```
+----------------+
| lifeexpectancy |
+----------------+
|       66.48604 |
+----------------+
```


Here getting the average life expectancy for Europe only.

```sql
select avg(lifeExpectancy) as lifeexpectancy from country where continent = "Europe";
```

```
+---------------------+
| avg(lifeExpectancy) |
+---------------------+
|            75.14773 |
+---------------------+
1 row in set (0.00 sec)
```

Now need to compare the life expectancy for each country in Europe to the average life expectancy (but not the average european life expectancy)/

Using a sub-query:


```sql
select Name as name, LifeExpectancy as lifeexpectancy from country where continent = "Europe" and LifeExpectancy < (
    select avg(lifeExpectancy) as lifeexpectancy from country
) order by Name;
```

```
+---------+----------------+
| name    | lifeexpectancy |
+---------+----------------+
| Moldova |           64.5 |
| Ukraine |           66.0 |
+---------+----------------+
2 rows in set (0.00 sec)
```


***

### 4.1.3 Peoples stage of life

Give the SQL command to show the following in ascending personID order:
- The person’s ID
- The person’s name
- The Person’s age
- A column called Stage




For this question all the details are in the `person` table.

```sql
select * from person order by personID;
```

```
+----------+------------+------+
| personID | personname | age  |
+----------+------------+------+
|        1 | Tom        |   33 |
|        2 | Alan       |   23 |
|        3 | Sean       |   30 |
|        4 | Sara       |   25 |
|        5 | Jane       |   25 |
|        6 | Michael    |   19 |
+----------+------------+------+
```


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

```
+----------+------------+------+---------------------+
| personID | personname | age  | Stage               |
+----------+------------+------+---------------------+
|        1 | Tom        |   33 | Thirtysomething     |
|        2 | Alan       |   23 | Late teens/Twenties |
|        3 | Sean       |   30 | Thirtysomething     |
|        4 | Sara       |   25 | Late teens/Twenties |
|        5 | Jane       |   25 | Late teens/Twenties |
|        6 | Michael    |   19 | Late teens/Twenties |
+----------+------------+------+---------------------+

```

***

### 4.1.4 Capitals and Official Languages of North America
Give the SQL command to show for each country in North America:
- The name of the capital city
- The name of the country
- The official language(s)
- The percentage of people who speak the official language(s)
The results should be alphabetical city name order, and within that by country name order, and within that by language order, and within that by ascending percentage.



Give the SQL command to show for each country in North America:
- The name of the capital city
- The name of the country
- The official language(s)
- The percentage of people who speak the official language(s)
The results should be alphabetical city name order, and within that by country name order, and within that by language order, and within that by ascending percentage.



Working with multiple tables here.


1. What tables are the data in?
Working with 3 tables here, the `city` table, the `country` table and the `countrylanguage` table.

- The city Name is in the `city` table
- The country Name (and Continent) are in the `country` table
- The language, official language  and Percentage fields are in the `countryLanguage` table.
- 

2. How are the tables linked?

- The `country` table has a foreign key constraint where the `Capital` field of the `country` table references the `id` field in the `city` table.
 
- The `city` table has a foreign key called `CountryCode` which references the `code` field in the `country` table.

- The `countrylanguage` table has a foreign key constraint where the `CountryCode` field references the `code` field in the `country` table.


```sql
 select name, code, capital from country where continent = "North America" order by name;
```
 
 
```
+----------------------------------+------+---------+
| name                             | code | capital |
+----------------------------------+------+---------+
| Anguilla                         | AIA  |      62 |
| Antigua and Barbuda              | ATG  |      63 |
| Aruba                            | ABW  |     129 |
| Bahamas                          | BHS  |     148 |
| Barbados                         | BRB  |     174 |
| Belize                           | BLZ  |     185 |
```
The `capital` field of the `country` table references the `id` field in the `city` table so join the two tables using an inner join.


```sql
select ci.Name, co.name, co.code from country co
inner join city ci 
on ci.ID = co.capital
where continent = "North America" order by ci.name;
```

```
+--------------------------+----------------------------------+------+
| Name                     | name                             | code |
+--------------------------+----------------------------------+------+
| Basse-Terre              | Guadeloupe                       | GLP  |
| Basseterre               | Saint Kitts and Nevis            | KNA  |
| Belmopan                 | Belize                           | BLZ  |
| Bridgetown               | Barbados                         | BRB  |
| Castries                 | Saint Lucia                      | LCA  |
```

Now join to the countrylanguage table

```sql
select ci.name, co.name,cl.language, cl.percentage from country co
inner join city ci 
on ci.ID = co.capital
inner join countrylanguage cl
on co.code = cl.CountryCode
where continent = "North America" and cl.IsOfficial = "T" order by ci.name, cl.language, cl.percentage;
```

```

| name                     | name                             | language    | percentage |

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

35 rows in set (0.00 sec)


```

***
### 4.1.5 Length of Stays
Give the SQL command to show for each country person:
- The person’s name
- The name of the city the person visited
- A column called Stay Length that shows the following:

Time the person stayed in city: Stay Length column output  

Less than 20 days:   Short  
Between 20 and 99 days:   Long  
Over 99 days:  Very Long

The results should be sorted alphabetically by personname, and within that by city name.


1. What tables are the data in?

- This data is split across several tables.
- The names `personname` and `personID` are in the `person` table. 
- The personID, cityID, dateArrived and dateLeft are in the hasvisitedcity table
- The  city `ID`, and city `Name`fields are in the `city` table.



2. How are the tables linked?


- While the `person` table does not have a foreign key itself, there is a foreign key pointing in to it from the `hasvisitedcity` table. 
- The `hasvisitedcity` table has two foreign key constraints:
    1. it's `cityID` field references the `id` field in the `city` table
    2. the `personid` field  references the `personid` in the `person` table


```sql
select p.personname, c.name, datediff(h.dateLeft, h.dateArrived) as stay
from person p
inner join hasvisitedcity h
on p.personID = h.personid
inner join city c
on h.cityID = c.id

```

```
+------------+------------------------+------+
| personname | name                   | stay |
+------------+------------------------+------+
| Alan       | Arnhem                 | 1122 |
| Alan       | Purulia                |   39 |
| Alan       | Tama                   |  764 |
| Alan       | Suzhou                 |  201 |
| Michael    | Guaíba                 |   58 |
| Michael    | Saint Helier           |    2 |
| Michael    | Nagoya                 |  367 |
| Sara       | Saint Helier           |    2 |
| Sara       | Jaunpur                |  162 |
| Sara       | Zürich                 |   32 |
| Sean       | Dordrecht              |  769 |
| Sean       | Shangqiu               | 1258 |
| Tom        | Dordrecht              |  200 |
| Tom        | Sydney                 |  173 |
| Tom        | São Lourenço da Mata   |   18 |
| Tom        | Muntinlupa             |  116 |
| Tom        | Tanjung Pinang         |  109 |
| Tom        | Suzhou                 |   50 |
```

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
```
```
| personname | name                   | Stay Length |
+------------+------------------------+-------------+
| Alan       | Arnhem                 | Very Long   |
| Alan       | Purulia                | Long        |
| Alan       | Tama                   | Very Long   |
| Alan       | Suzhou                 | Very Long   |
| Michael    | Guaíba                 | Long        |
| Michael    | Saint Helier           | Short       |
| Michael    | Nagoya                 | Very Long   |
| Sara       | Saint Helier           | Short       |
| Sara       | Jaunpur                | Very Long   |
| Sara       | Zürich                 | Long        |
| Sean       | Dordrecht              | Very Long   |
| Sean       | Shangqiu               | Very Long   |
| Tom        | Dordrecht              | Very Long   |
| Tom        | Sydney                 | Very Long   |
| Tom        | São Lourenço da Mata   | Short       |
| Tom        | Muntinlupa             | Very Long   |
| Tom        | Tanjung Pinang         | Very Long   |
| Tom        | Suzhou                 | Long        |
```
