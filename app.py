from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/test')
def testfunc():
    return 'This is my Flask App'

@app.route('/<name>/<int:age>')
def testname(name,age):
    return f'Hello my name is, {name} and my age is {age}'

@app.route('/handle',methods=['GET'])
def test_args_kwargs():
    args = request.args.getlist('args')
    kwargs = {key: value for key,value in request.args.items() if key !='args'}

    args_list = list(args)
    kwargs_dict = dict(kwargs)

    
    result = {
        'args': args_list,
        'kwargs' : kwargs_dict
    }
    return jsonify(result)
@app.route('/index')
def index():
    app_name = 'Ecommerce App'
    list1 = ['Sarita',29,56.7,0x00123,{'city':'Pune'}]

    dict1 = {
        1001 : {'Name':'Sarita','Position':'trainer','Salary':'300000'},
        1002 : {'Name':'Aditya','Position':'Manager','Salary':'400000000'},
        1003 : {'Name':'Vivek','Position':'CEO','Salary':'30000000'},
        1004 : {'Name':'Ankita','Position':'Maid','Salary':'5000'},
        1005 : {'Name':'Gaurav','Position':'Watchman','Salary':'3500','Diwali_Bonus':'501'}
    }

    return render_template('index.html',data=app_name,list_data=list1,data_dict=dict1)






app.run()   