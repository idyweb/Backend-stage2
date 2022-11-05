from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/getJson', methods = ['GET'])
def getJson():
    if(request.method == 'GET'):
        data = {
            "slackUsername": "idyValour",
            "backend": True,
            "age":27,
            "bio": "Build and Host server"
        }

        return jsonify(data)

@app.route('/math',  methods=['POST'])
def do_math():
    all_json = request.get_json()
    approved_json = ['x','y','operation_type']
    for item in approved_json:
        if item not in all_json:
             return {"error": f"{item} cannot be empty"},403 
    try:
        x = float(request.json.get('x'))
    except:
        return {"error": "Input x is not a number"},403
    try:
        y = request.json.get('y')
    except:
        return {"error": "Input y is not a number"},403
    try:

        operation_type = request.json.get('operation_type')
        if type(operation_type) != str:
            return {"error": "operation type is not string"},403
                
    except:
        pass
        #return {"error": "operation type cannot be empty"}
    
    if (operation_type == "addition") or (operation_type == "add"):
        return {"slackUsername": "idyValour",
                "result": x + y,
                "operation_type":operation_type},200
    elif (operation_type == "subtractions") or (operation_type == "subtract"):
        return {"slackUsername":"idyValour",
                "result": x - y,
                "operation_type": operation_type},200
    elif (operation_type == "multiplication") or (operation_type == "multiply"):
        return {"slackUsername":"idyValour",
                "result": x * y,
                "operation_type": operation_type},200
    else:
        return {"error": "operation does not exist"}, 403

@app.route('/', methods = ['GET'])
def home():

    data = {
         "slackUsername": "idyValour",
        "message": "Welcome to Home"
        }

    return jsonify(data)


if __name__=='__main__':
    app.run(port = 5000, debug=True)



