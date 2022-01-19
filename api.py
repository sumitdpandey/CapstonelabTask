from flask import Flask
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)

##EMPLOYEES= {} 

EMPLOYEES = {
  '1': {'name': 'Mark', 'age':28 , 'spec':'devops'},
  '2': {'name': 'Jane', 'age':32 , 'spec':'php'},
  '3': {'name': 'Peter', 'age':41 , 'spec':'python'},
  '5': {'name': 'Mike', 'age':25 , 'spec':'devsecops'},
  '6': {'name': 'Anil', 'age':55 , 'spec':'secops'},
}

parser = reqparse.RequestParser()
 
class EmployeeList(Resource):
    def get(self):
        return EMPLOYEES
    
    def post(self):
        parser.add_argument("name")
        parser.add_argument("age") 
        parser.add_argument("spec")
        args = parser.parse_args()
        employee_id = int(max(EMPLOYEES.keys())) + 1
        employee_id = '%i' % employee_id
        EMPLOYEES[employee_id] = {
             "name" : args["name"],
             "age" : args ["age"],
             "spec" : args["spec"],
        }
        return EMPLOYEES[employee_id] , 201

class Employee(Resource):
    def get(self, employee_id):
        if employee_id not in EMPLOYEES:
            return "NOT FOUND", 404
        else:
            return EMPLOYEES[employee_id]
    
    def put(self, employee_id):
        parser.add_argument("name")
        parser.add_argument("age") 
        parser.add_argument("spec")
        args = parser.parse_args()
        if employee_id not in EMPLOYEES:
            return "Record not found", 404
        else:
            employee = EMPLOYEES[employee_id]
            employee["name"] = args["name"] if args["name"] is not None else employee["name"]
            employee["age"] = args["age"] if args["age"] is not None else employee["age"]
            employee["spec"] = args["spec"] if args["spec"] is not None else employee["spec"]
            EMPLOYEES[employee_id]["name"]=args["name"] if args["name"] is not None else employee["name"]
            EMPLOYEES[employee_id]["age"] = args["age"] if args["age"] is not None else employee["age"]
            EMPLOYEES[employee_id]["spec"]=args["spec"] if args["spec"] is not None else employee["spec"]
            return employee, 200
    
    def delete(self, employee_id):
        if employee_id not in EMPLOYEES:
            return "Not found", 404
        else:
            del EMPLOYEES[employee_id]
            return '', 204
    



api.add_resource(EmployeeList,"/employee")
api.add_resource(Employee,"/employee/<employee_id>")

if __name__ == "__main__":
    app.run(debug = True)