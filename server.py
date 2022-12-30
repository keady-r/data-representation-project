from flask import Flask, url_for, request, redirect, abort,jsonify
from databaseCreate import run
import mysql.connector
import webbrowser

# Testing connection to database - if unsuccessful try running the databaseCreate Command again

conn = mysql.connector.connect(user='root', password='', host='localhost',database='datarepresentation')

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")






# Creating Flask Application 
app = Flask(__name__, static_url_path='', static_folder='staticpages' )

#jobs = run.showJobsTable()

jobs = [
    {"id":1,"Role":"Waitress","Company":"Papa Rich","Year_Start":2018,"Year_End":2019,"Description":"Waites tables in busy resturant"},
    {"id":2,"Role":"Researcher","Company":"WestWay Health","Year_Start":2019,"Year_End":2019,"Description":"Researched Novel forms of antibiotics"},
    {"id":3,"Role":"Laboratory Systems Analysts","Company":"Takeda","Year_Start":2019,"Year_End":2021,"Description":"Subject Matter Expert in MODA, LIMS, EMPOWER. System Administrator."},
    {"id":4,"Role":"LabOps Developer","Company":"Pfizer","Year_Start":2021,"Year_End":2022,"Description":"Responsible for the validation and implementation of LIMS system"},
    {"id":5,"Role":"Software Systems Architect","Company":"Pfizer","Year_Start":2022,"Year_End":"Current","Description":"Technical Arectect for multiple softwares. Database implementation, server upgrade manager."},
]
nextjobsId=6 


#### - Start 

@app.route('/jobs', methods = ['GET'])
def getAllJobs():
    selectJobsTable = """SELECT * FROM jobs"""
    cursor = conn.cursor()
    cursor.execute(selectJobsTable)
    result = cursor.fetchall()
    p = []

    jobs = "ID,Role,Company,YearStart,YearEnd,Description"
    p.append(jobs)

    for row in result:
        a = "%s"%row[0]
        p.append(a)
        b = "%s"%row[1]
        p.append(b)
        c = "%s"%row[2]
        p.append(c)
        d = "%s"%row[3]
        p.append(d)
        e = "%s"%row[4]

        
    return jsonify(result)

@app.route('/education', methods = ['GET'])
def getAllEducation():
    selectEducationTable = """SELECT * FROM education"""
    cursor = conn.cursor()
    cursor.execute(selectEducationTable)
    rows = cursor.fetchall()
    p = []

    school = "ID,School,Course,Award,YearStart,YearEnd"
    p.append(school)

    for row in rows:
        a = "%s"%row[0]
        p.append(a)
        b = "%s"%row[1]
        p.append(b)
        c = "%s"%row[2]
        p.append(c)
        d = "%s"%row[3]
        p.append(d)
        e = "%s"%row[4]


    return jsonify(rows)


@app.route('/jobs', methods = ['POST'])
def newJobEntry(Role, Company, YEAR_START, YEAR_END, Description):
    dataJobs = (Role, Company, YEAR_START, YEAR_END, Description)
    newid = run.createJobsRow(dataJobs)
    
    return jsonify({'id':newid})


@app.route('/jobs', methods = ['GET'])
def returnJobCount(jobRole):
    count = run.countschool('Labware')
    return jsonify({jobRole:count})


@app.route('/entry/all', methods = ['delete'])
def deleteAllEntries():
    return jsonify({'done':True})

##### - End 


#Find by ID 
@app.route('/jobs/<int:id>')
def findID(id):
    foundJobs = list(filter(lambda t : t["id"]== id, jobs))
    if len(foundJobs) == 0:
        return jsonify({}), 204
    return jsonify(foundJobs[0])


#curl -H "Content-Type:application/json" -X POST -d‘{"Role":“xxx","Company":“xxx","Year_Start":3000}’
#http://127.0.0.1:5000/portfolio
#curl -X POST -H "content-type:application/json" -d "{\"Role\":\"test\",\"Company\":\"Ruth\",\"Year_Start\":15,\"Year_End\":15,\"Description":15}" http://127.0.0.1:5000/portfolio
@app.route('/jobs', methods = ['POST'])
def create():
    global nextjobsId
    if not request.json:
        abort(400)
        
    jobs={
        "id": nextjobsId, 
        "Role": request.json["Role"],
        "Company":request.json["Company"],
        "Year_Start": request.json["Year_Start"],
        "Year_End": request.json["Year_End"],
        "Description":request.json["Description"],
    }
    jobs.append(jobs)
    nextjobsId =+1
    return jsonify(jobs)

    
#curl -X PUT -d "{\"Role\":\"test\",\"Company\":\"Ruth\",\"Year_Start\":15,\"Year_End\":15,\"Description":15}" -H "content-type:application/json" http://127.0.0.1:5000/portfolio/4
@app.route('/jobs/<int:id>', methods = ['PUT'])
def update(id):
    foundJobs = list(filter(lambda t : t["id"]== id, jobs))
    if len(foundJobs) == 0:
        return jsonify({}), 404
    currentJobs = foundJobs[0]
    
    if "Role" in request.json:
        currentJobs['Role'] = request.json['Role']
        
    if "Company" in request.json:
        currentJobs['Company'] = request.json['Company']
        
    if "Year_Start" in request.json:
        currentJobs['Year_Start'] = request.json['Year_Start']
        
    if "Year_End" in request.json:
        currentJobs['Year_End'] = request.json['Year_End']
        
    if "Description" in request.json:
        currentJobs['Description'] = request.json['Description']
        
    return jsonify(currentJobs)
#curl -X DELETE http://127.0.0.1:5000/jobs/1
@app.route('/jobs/<int:id>', methods = ['DELETE'])
def delete(id):
    foundJobs = list(filter(lambda t : t["id"]== id, jobs))
    if len(foundJobs) == 0:
        return jsonify({}), 404
    jobs.remove(foundJobs[0])

    return jsonify({"done":True})

if __name__ =="__main__":
    app.run(debug = True)