from flask import jsonify

from app import app


# this is api file where any one can access the data of our api..
# time O(n) documents and O(m) space
@app.route('/pull_j0', methods=['GET'])
def pull_j0():
    from app import mongo
    data = []
    jobs = mongo.db.jobs
    for job in jobs.find():
        data.append({'salary': job['salary'], 'experience': job['experience'], 'company': job['company'], 'role': job['role'],
             'location': job['location']})
    return jsonify({'result': data})


# time O(n) documents and O(m) space
@app.route('/pull_j1', methods=['GET'])
def pull_j1s():
    from app import mongo
    data = []
    jobs = mongo.db.experience
    for job in jobs.find():
        data.append(
            {'salary': job['salary'], 'experience': job['experience'], 'company': job['company'], 'role': job['role'],
             'location': job['location']})
    return jsonify({'result': data})


# time O(n) documents and O(m) space
@app.route('/pull_j2', methods=['GET'])
def pull_j2():
    from app import mongo
    data = []
    jobs = mongo.db.freshers
    for job in jobs.find():
        data.append(
            {'salary': job['salary'], 'experience': job['experience'], 'company': job['company'], 'role': job['role'],
             'location': job['location']})
    return jsonify({'result': data})
