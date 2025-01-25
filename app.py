from flask import Flask, render_template, jsonify
#importing functionality from class Flask into the variable app

#Created html file in the templates folder, to use the template we use the function render_template

app = Flask(__name__)

#flask application created

Jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'Remote',
    'salary': 'Rs. 20,00,000'
    },
    {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Gurgaon',
    'salary': 'Rs. 13,00,000'
    },
]
#registration of route
#we have informed flask that when the URL / is accessed the function hello_world() is called.

@app.route("/")
def hello_jovion():
    return render_template('home.html', 
                          jobs = Jobs,
                          companyname = 'Jovion')
#We took the information that was stored inside the list we have passed it into the render variable as a variable

#This was one way to access a dynamic data one oyher way to access some dynaic data is to use API.

@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)


if __name__ == "__main__":
  app.run(host= "0.0.0.0", debug=True)
  
#we put the host and debug parameters to make the app run on the local machine