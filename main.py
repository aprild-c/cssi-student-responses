# main.py
# the import section
import webapp2
import jinja2
import os
import random

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class StudentPage(webapp2.RequestHandler):
    total = 0
    pos = []
    positive = 0
    negative = 0

    def get(self): #for a get request
        student_template = the_jinja_env.get_template('templates/studentView.html')
        self.response.write(student_template.render())  # the response

    def postThumbsUp(self):
        student_template = the_jinja_env.get_template('templates/studentView.html')
        StudentPage.total += 1
        StudentPage.positive += 1
        StudentPage.pos.append((random.randint(25,80), random.randint(0,95)))
        self.response.write(student_template.render())  # the response

    def postThumbsDown(self):
        student_template = the_jinja_env.get_template('templates/studentView.html')
        StudentPage.total += 1
        StudentPage.negative += 1
        StudentPage.pos.append((random.randint(25,80), random.randint(0,95)))
        self.response.write(student_template.render())  # the response


class TeacherPage(webapp2.RequestHandler):
    def get(self): #for a get request
        teacher_template = the_jinja_env.get_template('templates/teacherView.html')
        response_data = {
            "total" : StudentPage.total,
            "pos" : StudentPage.pos,
            "positive" : StudentPage.positive,
            "negative" : StudentPage.negative
        }
        self.response.write(teacher_template.render(response_data))  # the response

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', StudentPage), #this maps the root url to the Main Page Handler
    ('/teacher', TeacherPage)
], debug=True)
