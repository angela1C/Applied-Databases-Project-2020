# A summary of my answers only to the questions in  the project.

### 4.2.1 Average Age of Students
Give the MongoDB command to find the average age of students.

This is the answer that is expected:
>{ "Average" : 33 }

My answer uses the following: 

Using the `$project` to get rid of the id 
```json
db.docs.aggregate([{$group:{_id:null,"Average":{$avg:"$details.age"}}},{ $project: {"_id":0} }])
```
> { "Average" : 33 }


Alternatively using `unset`
```json
db.docs.aggregate([{$group:{_id:null,"Average":{$avg:"$details.age"}}},{ $unset: ["_id"] }])
```

>{ "Average" : 33 }


There are 7 students in this database. 
`db.docs.count()` returns 11 documents. There are 7 documents for each student and 4 documents with details of the courses.
It looks each student document contains an embedded document with the student details and also a reference to another document for their qualifications.

## `aggregate()` method
See [aggregation quick reference manual](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/).

The `aggregate()` method calculates aggregate values for the data in a collection.
`db.collection.aggregate(pipeline, options)`

- The `aggregate` method takes one parameter which is an array `[]`. When using aggregate you must use a `$` in front of the field. Using the `db.collection.aggregate` method, pipeline stages appear in an array. 
- `db.collection.aggregate( [ { <stage> }, ... ] )`

In the `db.collection.aggregate` method, pipeline stages appear in an array. Documents pass through the stages in sequence. Most stages can appear more than once in a pipeline.
Pipeline stages include 


-  `$group` : to group input documents by a specified identifier expression and applies the accumulator expression(s), if specified, to each group.

- `$project`: Reshapes each document in the stream, such as by adding new fields or removing existing fields. For each input document, outputs one document. (See `$set` and `$unset` which are aliases for `$project`)

- `$unset`: to remove or exclude fields from documents. 
 

The `$group` stage has the following prototype form:
```
{$group:
    {
    _id: <expression>, // Group By Expression
     <field1>: { <accumulator1> : <expression1> },
    ...
    }
 }
 ```

```json
db.docs.aggregate([{$group:{_id:null,"Average":{$avg:"$details.age"}}},{ $project: {"_id":0} }])
db.docs.aggregate([{$group:{_id:null,"Average":{$avg:"$details.age"}}},{ $unset: ["_id"] }])
```

`{$group:{_id:null,"Average":{$avg:"$details.age"}}}`
The `_id` is the expression to group by. In this case we just want an overall average so set it to `null`.
"Average" is the name of the field to return. <field1>
`{$avg:"$details.age"}` is the {accumulator : expression} field is  get the average of the details.age field.


- `$group` is one of the aggregate pipeline stage used here. 

It is used to group the input documents, as we want the average for all the students, set the `_id` to null.
It takes all the input documents and returns one output for each distinct group. (none here)

- `$project` is another aggregate pipeline stage used here. As we do not want the `_id` field to appear in the output, set it to 0. The `$unset` pipeline stage could be used instead.


***



### 4.2.2 Honours Level
Give the MongoDB command to show the name of each course and Honours which has the value true if the course level is 8 or higher, otherwise false. The output should be sorted by name.


```json
{ "name" : "B.A.", "Honours" : true }
{ "name" : "B.Eng.", "Honours" : false }
{ "name" : "H. Dip. in Data Analytics", "Honours" : true }
{ "name" : "H. Dip. in SW Devel", "Honours" : true }
```

My answer:
```json
db.docs.aggregate([{$match: {level:{$exists:true}}}, {$project:{_id:0, name:1, "Honours":{ $eq:["$level", 8]}}},{$sort:{name:1}}])
{ "name" : "B.A.", "Honours" : true }
{ "name" : "B.Eng.", "Honours" : false }
{ "name" : "H. Dip. in Data Analytics", "Honours" : true }
{ "name" : "H. Dip. in SW Devel", "Honours" : true }
```
***

### 4.2.3 Qualified Students
Give the MongoDB command to show the number of Qualified Students i.e. those documents with a qualifications field.

{ "Qualified Students" : 6 }


my answer:

```json
 db.docs.aggregate( [ {$match: {qualifications:{$exists:true}}},  { $group: { _id: null, "Qualified Students": {$sum: 1} } }, {$project: {_id:0}}  ])
{ "Qualified Students" : 6 }
```

An equivalent way to using the `{ $group: { _id: null, "Qualified Students": {$sum: 1} } }, {$project: {_id:0}} ` part of the query is to use `{$count: "Qualified Students"}`

```json
db.docs.aggregate([{$match: { qualifications: {$exists: true}}}, {$count: "Qualified Students"}] )
{ "Qualified Students" : 6 }
```
***


### 4.2.4 Students and their Qualifications
Give the MongoDB command to show the name of each Student and his/her qualifications. The output should be in alphabetical name order.
If the student has no qualifications the word “None” should appear:


{ "details" : { "name" : "Alan Higgins" }, "qualifications" : [ "ENG, SW" ] }
{ "details" : { "name" : "Bernie Lynch" }, "qualifications" : [ "ARTS" ] }
{ "details" : { "name" : "Brian Collins" }, "qualifications" : [ "ENG", "SW" ] }
{ "details" : { "name" : "John Smith" }, "qualifications" : [ "ARTS", "DATA" ] }
{ "details" : { "name" : "Mary Murphy" }, "qualifications" : [ "ARTS" ] }
{ "details" : { "name" : "Mick O'Hara" }, "qualifications" : [ "ENG", "DATA", "SW" ] }
{ "details" : { "name" : "Tom Kenna" }, "qualifications" : "None" }


My answer:

```json
 db.docs.aggregate([{$match: {details:{$exists:true}}},{$project:{"details.name":1,_id:0,qualifications:{ $ifNull:["$qualifications","None"]}}},{$sort:{"details.name": 1}}])

 
{ "details" : { "name" : "Alan Higgins" }, "qualifications" : [ "ENG, SW" ] }
{ "details" : { "name" : "Bernie Lynch" }, "qualifications" : [ "ARTS" ] }
{ "details" : { "name" : "Brian Collins" }, "qualifications" : [ "ENG", "SW" ] }
{ "details" : { "name" : "John Smith" }, "qualifications" : [ "ARTS", "DATA" ] }
{ "details" : { "name" : "Mary Murphy" }, "qualifications" : [ "ARTS" ] }
{ "details" : { "name" : "Mick O'Hara" }, "qualifications" : [ "ENG", "DATA", "SW" ] }
{ "details" : { "name" : "Tom Kenna" }, "qualifications" : "None" }
```