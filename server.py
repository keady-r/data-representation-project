from flask import Flask, url_for, request, redirect, abort,jsonify


app = Flask(__name__, static_url_path='', static_folder='staticpages' )

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
    return jsonify(jobs)

@app.route('/entry/<jobRole>', methods = ['POST'])
def newJobEntry(jobRole):
    ip_addr = request.remote_addr
    data = (jobRole, ip_addr)
    newid = jobEntry.create(data)

    return jsonify({'id':newid})


@app.route('/entry/<jobRole>', methods = ['GET'])
def returnJobCount(jobRole):
    count = jobEntry.countjobs(jobRole)
    return jsonify({jobRole:count})

@app.route('/entry', methods = ['GET'])
def getAllCount():
    allcounts = []
    for job in jobs:
        job = ['Role'] 
        count = jobEntry.countjobs(jobRole)
        allcounts.append({job:count})
    return jsonify(allcounts)

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

    return "find by ID"+str(id)


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