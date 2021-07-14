## 4.2. An overview of the MySQL `World` database used for the project for section 4.2 

First Import the **world** database from **world.sql** to MySQL and write queries

(base) A...:~ $ `mysql -u root -p`
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.

To import the database I first create an empty database called world    

```
mysql> create database world;

mysql> use world;

mysql> show tables;

mysql> source /path-to-database/world.sql
```


### 4.1.1 Alan’s travel details
Give the MySQL command that shows:
- The name of the cities
- The Arrival Date in the cities
- The name of the country the city is in

For all cities and countries visited by “Alan” in alphabetical order by city name.

#### Expected results for 4.1.1
name	dateArrived	name
Arnhem	2002-04-14	Netherlands
Purulia	2002-06-20	India
Suzhou	2002-01-30	China
Tama	2009-02-13	Japan

```sql
show tables;
```

```
+-----------------+
| Tables_in_world |
+-----------------+
| city            |
| country         |
| countrylanguage |
| hasvisitedcity  |
| person          |
+-----------------+
```

## The `person` table.

- The primary key of the person table is the personID.
- There is no foreign key in the `person` table

 - While the `person` table does not have a foreign key itself, there is a foreign key pointing in to it from the `hasvisitedcity` table. 
 - See the `hasvisitedcity` table which has the following foreign key constraint:
 - (CONSTRAINT `fk_personid` FOREIGN KEY (`personID`) REFERENCES `person` (`personid`))

```sql
describe person;
show create table person;
```

```
+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| personID   | int(11)     | NO   | PRI | NULL    | auto_increment |
| personname | varchar(50) | YES  | UNI | NULL    |                |
| age        | int(11)     | YES  |     | NULL    |                |
+------------+-------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

| person | CREATE TABLE `person` (
  `personID` int(11) NOT NULL AUTO_INCREMENT,
  `personname` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`personID`),
  UNIQUE KEY `personname` (`personname`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 |
+--------+-----------------------------------------------
```

```
select * from person where personname = "Alan";
+----------+------------+------+
| personID | personname | age  |
+----------+------------+------+
|        2 | Alan       |   23 |
+----------+------------+------+
1 row in set (0.00 sec)
```




## The `city` table:

- The primary key of the `city` table is the `ID` field.
- There is a foreign key constraint in the `city` table.   
- CONSTRAINT `city_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`code`)
- The `city` table has a foreign key called `CountryCode` which references the `code` field in the `country` table.

```sql
describe city;
show create table city;
```

```
+-------------+----------+------+-----+---------+----------------+
| Field       | Type     | Null | Key | Default | Extra          |
+-------------+----------+------+-----+---------+----------------+
| ID          | int(11)  | NO   | PRI | NULL    | auto_increment |
| Name        | char(35) | NO   |     |         |                |
| CountryCode | char(3)  | NO   | MUL |         |                |
| District    | char(20) | NO   |     |         |                |
| Population  | int(11)  | NO   |     | 0       |                |
+-------------+----------+------+-----+---------+----------------+


| city  | CREATE TABLE `city` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(35) NOT NULL DEFAULT '',
  `CountryCode` char(3) NOT NULL DEFAULT '',
  `District` char(20) NOT NULL DEFAULT '',
  `Population` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`),
  KEY `CountryCode` (`CountryCode`),
  CONSTRAINT `city_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=4082 DEFAULT CHARSET=latin1 |
+-------+---------------------------------------------------------------------
```





## The `country` table:

- The primary key in the `country` table is the `Code` field.
-`CONSTRAINT `country_ibfk_1` FOREIGN KEY (`Capital`) REFERENCES `city` (`id`)
- The `country` table has a foreign key constraint where the `Capital` field of the `country` table references the `id` field in the `city` table.

```sql
describe country;
show create table country;
```
```
+----------------+---------------------------------------------------------------------------------------+------+-----+---------+-------+
| Field          | Type                                                                                  | Null | Key | Default | Extra |
+----------------+---------------------------------------------------------------------------------------+------+-----+---------+-------+
| Code           | char(3)                                                                               | NO   | PRI |         |       |
| Name           | char(52)                                                                              | NO   |     |         |       |
| Continent      | enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') | NO   |     | Asia    |       |
| Region         | char(26)                                                                              | NO   |     |         |       |
| SurfaceArea    | float(10,2)                                                                           | NO   |     | 0.00    |       |
| IndepYear      | smallint(6)                                                                           | YES  |     | NULL    |       |
| Population     | int(11)                                                                               | NO   |     | 0       |       |
| LifeExpectancy | float(3,1)                                                                            | YES  |     | NULL    |       |
| GNP            | float(10,2)                                                                           | YES  |     | NULL    |       |
| LocalName      | char(45)                                                                              | NO   |     |         |       |
| GovernmentForm | char(45)                                                                              | NO   |     |         |       |
| HeadOfState    | char(60)                                                                              | YES  |     | NULL    |       |
| Capital        | int(11)                                                                               | YES  | MUL | NULL    |       |
+----------------+---------------------------------------------------------------------------------------+------+-----+---------+-------+
13 rows in set (0.00 sec)

| country | CREATE TABLE `country` (
  `Code` char(3) NOT NULL DEFAULT '',
  `Name` char(52) NOT NULL DEFAULT '',
  `Continent` enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') NOT NULL DEFAULT 'Asia',
  `Region` char(26) NOT NULL DEFAULT '',
  `SurfaceArea` float(10,2) NOT NULL DEFAULT '0.00',
  `IndepYear` smallint(6) DEFAULT NULL,
  `Population` int(11) NOT NULL DEFAULT '0',
  `LifeExpectancy` float(3,1) DEFAULT NULL,
  `GNP` float(10,2) DEFAULT NULL,
  `LocalName` char(45) NOT NULL DEFAULT '',
  `GovernmentForm` char(45) NOT NULL DEFAULT '',
  `HeadOfState` char(60) DEFAULT NULL,
  `Capital` int(11) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  KEY `Capital` (`Capital`),
  CONSTRAINT `country_ibfk_1` FOREIGN KEY (`Capital`) REFERENCES `city` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |

```

## The `countrylanguage` table.
- The primary key on the `countrylanguage` table is the `CountryCode` and the `Language` fields.
- CONSTRAINT `countryLanguage_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`code`)
- The `countrylanguage` table has a foreign key constraint where the `CountryCode` field references the `code` field in the `country` table.


```sql
describe countrylanguage;
show create table countrylanguage;
```

```
+-------------+---------------+------+-----+---------+-------+
| Field       | Type          | Null | Key | Default | Extra |
+-------------+---------------+------+-----+---------+-------+
| CountryCode | char(3)       | NO   | PRI |         |       |
| Language    | char(30)      | NO   | PRI |         |       |
| IsOfficial  | enum('T','F') | NO   |     | F       |       |
| Percentage  | float(4,1)    | NO   |     | 0.0     |       |
+-------------+---------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

| countrylanguage | CREATE TABLE `countrylanguage` (
  `CountryCode` char(3) NOT NULL DEFAULT '',
  `Language` char(30) NOT NULL DEFAULT '',
  `IsOfficial` enum('T','F') NOT NULL DEFAULT 'F',
  `Percentage` float(4,1) NOT NULL DEFAULT '0.0',
  PRIMARY KEY (`CountryCode`,`Language`),
  KEY `CountryCode` (`CountryCode`),
  CONSTRAINT `countryLanguage_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |

```

## The `hasvisitedcity` table.

```sql
describe hasvisitedcity;
show create table hasvisitedcity;
```


- The primary key on the `hasvisitiedcity` table is the `personID` and`cityID` fields.
-  CONSTRAINT `fk_personid` FOREIGN KEY (`personID`) REFERENCES `person` (`personid`),
-  CONSTRAINT `hasvisitedcity_ibfk_1` FOREIGN KEY (`cityID`) REFERENCES `city` (`id`)
- There are two foreign key constraints on the `hasvisitedcity` table. 
1. The `personID` field in the `hasvisitedcity` table references the `personid` field in the `person` table.
2. The ` cityID` in the `hasvisitedvity` table references the `id` field in the `city` table.
- While the `person` table does not have a foreign key itself, there is a foreign key pointing in to it from the `hasvisitedcity` table.

```
+-------------+---------+------+-----+---------+-------+
| Field       | Type    | Null | Key | Default | Extra |
+-------------+---------+------+-----+---------+-------+
| personID    | int(11) | NO   | PRI | 0       |       |
| cityID      | int(11) | NO   | PRI | 0       |       |
| dateArrived | date    | YES  |     | NULL    |       |
| dateLeft    | date    | YES  |     | NULL    |       |
+-------------+---------+------+-----+---------+-------+
4 rows in set (0.00 sec)


| hasvisitedcity | CREATE TABLE `hasvisitedcity` (
  `personID` int(11) NOT NULL DEFAULT '0',
  `cityID` int(11) NOT NULL DEFAULT '0',
  `dateArrived` date DEFAULT NULL,
  `dateLeft` date DEFAULT NULL,
  PRIMARY KEY (`personID`,`cityID`),
  KEY `cityID` (`cityID`),
  CONSTRAINT `fk_personid` FOREIGN KEY (`personID`) REFERENCES `person` (`personid`),
  CONSTRAINT `hasvisitedcity_ibfk_1` FOREIGN KEY (`cityID`) REFERENCES `city` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+----------------
1 row in set (0.00 sec)

```




