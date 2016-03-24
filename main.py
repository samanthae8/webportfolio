
import webapp2
import os
import logging
import jinja2
from google.appengine.api import mail
from google.appengine.api import users 
# import cgi

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	
    	try:
        	template = JINJA_ENVIRONMENT.get_template('templates%s' % self.request.path)
        	self.response.write(template.render())

        except:
        	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        	self.response.write(template.render())

class FormHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render())

    def post(self):
        # contact=self.request.POST['name']
        # email=self.request.POST['email']
        # comments=self.request.POST['comment']
        template = JINJA_ENVIRONMENT.get_template('templates/contactinfo.html')
        self.response.write(template.render())
        
        # mail.send_mail(sender="Example.com Support <support@example.com>", to="Sam <samholz@umich.edu>", subject="subject", body="body")
        
        logging.info("Contact Information of Sender")
        logging.info("Name:")
        logging.info(self.request.get('name'))
        logging.info("Email:")
        logging.info(self.request.get('email'))
        logging.info("Date:")
        logging.info(self.request.get('dateInput'))
        logging.info("Type of Message:")
        logging.info(self.request.get('file'))
        logging.info("Message to teacher:")
        logging.info(self.request.get('comment'))

        # form = cgi.FieldStorage()
        # with open ('comments.txt', 'w') as fileOutput:
        #     fileOutput.write(form.getValue('name'))
        #     fileOutput.write(form.getValue('email'))
        #     fileOutput.write(form.getValue('comment'))
        
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/kidscenter.html', MainHandler),
    ('/photogallery.html', MainHandler),
    ('/contact.html', FormHandler),
    ('/contactinfo.html', FormHandler)
], debug=True)
