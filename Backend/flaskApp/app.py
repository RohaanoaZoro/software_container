
from flask import Flask, request, Response, jsonify
from dbconnect import MongoDatabaseProperty
import azure.functions as func
import json

from flask_cors import cross_origin, CORS

from bson.json_util import dumps

from bson import ObjectId



app = Flask(__name__)


@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()


colz = MongoDatabaseProperty()

@app.route('/')
@cross_origin()
def test():
    return 'Hello World123'

@app.route('/searchProperty', methods = ['GET'])
@cross_origin()
# ‘/’ URL is bound with hello_world() function.
def searchProperty():

    q = request.args.get('q')
    print("q", q)

    if ";" in q:
        params = q.split(";")
        s_query = {}
        for p in params:
            if ":" in p:
                keyV = p.split(":")
                print("params", keyV)
                if len(keyV) == 2:
                    s_query[keyV[0]] = keyV[1]
        res = colz.find(s_query)
                    

    elif ":" in q:
        keyV = q.split(":")
        print("params", keyV)
        if len(keyV) == 2:
            res = colz.find({keyV[0]:keyV[1]})
    else:
        #Get all entries from mongo. Inside {} filters can be added
        res = colz.find({"address":q})

    
    if res:
        # Converting to the JSON
        list_cur = list(res)
        json_data = dumps(list_cur, indent = 2) 
    
        return json_data
    else:
        return "Error could not retieve data", 400
    
@app.route('/deleteProperty/<id>', methods = ['GET'])
@cross_origin()
# ‘/’ URL is bound with hello_world() function.
def deleteProperty(id):

    res = colz.find({"_id": ObjectId(id)})
 
    if res:
        # Converting to the JSON
        colz.delete_one({"_id": ObjectId(id)})
    
        return "Successfully Deleted Property"
    else:
        return "Error could not delete data", 400
    
@app.route('/updateProperty/<id>', methods = ['POST'])
@cross_origin()
# ‘/’ URL is bound with hello_world() function.
def updateProperty(id):

    q = request.args.get('q')
    print("q", q)

    res = {}
    if q:
        if ";" in q:
            return "Can update only one field at a time"
                    
        elif ":" in q:
            keyV = q.split(":")
            if len(keyV) == 2:
                res = colz.find({"_id": ObjectId(id)})
                if res:
                    newvalues = { "$set": {keyV[0]:keyV[1]} }
                    colz.update_one({"_id": ObjectId(id)}, newvalues)

                    return "Successfully updated data", 200
    else:
        res = colz.find({"_id": ObjectId(id)})

        patch_body = request.json

    
        if res:
            # Converting to the JSON
            colz.delete_one({"_id": ObjectId(id)})

            patch_body["_id"] = ObjectId(id)

            colz.insert_one(patch_body)

            return "Updated Data Succesfully", 200    
        
        else:
            return "Error could not delete data", 400




@app.route('/getProperty', methods = ['GET'])
@cross_origin()
# ‘/’ URL is bound with hello_world() function.
def getProperty():

    d = request.args.to_dict()


    find_query = """ {
        "greenscore": { "$gte": %s },
        "address": "%s",
        "propertyvalues.propertytype": "%s",
        "propertyvalues.co2": { "$gte": %s },
        "propertyvalues.waste": { "$gte": %s },
        "propertyvalues.cleanenergy": { "$gte": %s },
        "propertyvalues.area": { "$gte": %s }
    }
    
    """%( d['greenscore'], d['address'],  d['propertytype'],  d['co2'], d['waste'], d['cleanenergy'], d['area'])


    find_query = find_query.replace(""" "address": "",""", "" )
    find_query = find_query.replace('"propertyvalues.propertytype": "",', "" )

 
    print("find query: ", find_query)
    # print("json query: ", json.loads(find_query))


    res = colz.find( json.loads(find_query))


    if res:
        # Converting to the JSON
        list_cur = list(res)
        json_data = dumps(list_cur, indent = 2)
        return json_data
    else:
        return "Error could not retieve data", 400

    # 127.0.0.1:5000/getProperty?greenscore={"$or":[{"$gt":10},{"$gt":22}]}
    # 127.0.0.1:5000/getProperty?greenscore={%22$or%22:[{%22$gt%22:3},{%22$gt%22:4}]}&propertyvalues.co2={%22$or%22:[{%22$gt%22:234},{%22$gt%22:233}]}

    #Get all entries from mongo. Inside {} filters can be added

    # find_query = {}

    # numeric_filters = [key for key in ["greenscore",
    #                                    "propertyvalues.area",
    #                                    "propertyvalues.waste",
    #                                    "propertyvalues.co2",
    #                                    "propertyvalues.energy",
    #                                    "propertyvalues.cleanenergy"]
    #                    if key in d]

    # if numeric_filters:

    #     # Parse the numeric filter parameters and convert it to a valid MongoDB query format
    #     for key in numeric_filters:

    #         # $gt, $lt or $or is in filter condition
    #         if '$' in d[key]:
    #             try:
    #                 key_filter_values = json.loads(d[key])

    #                 # Format disjunction of key_filter_values through dict comprehension.
    #                 if "$or" in key_filter_values:
    #                     or_list = [{key: {op: value}} for condition in key_filter_values["$or"]
    #                                for op, value in condition.items() if op in ("$gt", "$lt")]

    #                     # Set disjunction operator of find query.
    #                     if "$or" in find_query:
    #                         find_query["$or"] = find_query["$or"] + or_list
    #                     else:
    #                         find_query["$or"] = or_list
    #                 else:
    #                     find_query[ key] = key_filter_values

    #             except json.JSONDecodeError:
    #                 return 'Invalid ' + key + ' parameter', 400
    #         else:

    #             # Convert key_filter_values to int, because for some reason it is string type in this branch.
    #             find_query[ key] = int( d[ key])
    #         d.pop( key) # remove key from args dict to ensure non-numeric filter values are added after parsing.

    #     # Add remaining non-numeric filter values.
    #     for key in d:
    #         find_query[ key] = d[ key]
    # else:
    #     find_query = d # Add non-numeric filter values.

    # # Execute the query and get the results
    # print("find query: ", find_query)
    # res = colz.find( find_query)


    # if res:
    #     # Converting to the JSON
    #     list_cur = list(res)
    #     json_data = dumps(list_cur, indent = 2)
    #     return json_data
    # else:
    #     return "Error could not retieve data", 400

@app.route('/addProperty', methods = ['POST', 'OPTIONS'])
@cross_origin()
def postProperty():

    post_body = request.json

    print("Post Body Recieved")

    if "name" not in post_body:
        return "Missing 'name' in body", 400

    if "greenscore" not in post_body:
        return "Missing 'greenscore' in body", 400
    
    if "description" not in post_body:
        return "Missing 'description' in body", 400

    if "address" not in post_body:
        return "Missing 'address' in body", 400
    
    if "propertyvalues" not in post_body:
        return "Missing 'propertyvalues' in body", 400
    
    if "energy" not in post_body["propertyvalues"]:
        return "Missing 'energy' in body", 400
    
    if "co2" not in post_body["propertyvalues"]:
        return "Missing 'co2' in body", 400
    
    if "waste" not in post_body["propertyvalues"]:
        return "Missing 'waste' in body", 400
    
    if "cleanenergy" not in post_body["propertyvalues"]:
        return "Missing 'cleanenergy' in body", 400
    
    if "area" not in post_body["propertyvalues"]:
        return "Missing 'area' in body", 400
    
    if "propertytype" not in post_body["propertyvalues"]:
        return "Missing 'propertytype' in body", 400
    

    
    temp_dict = {"address":post_body["address"]}

    res = colz.find_one(temp_dict)
    if res:
        return 'already exists', 409


    colz.insert_one(post_body)

    res = colz.find_one(temp_dict)
    

    if res:
        return str(res["_id"]), 200
    else: 
        return 'could not add to mongo', 400

    
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the WSGI handler.
    """
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)


 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0', port=5000)
