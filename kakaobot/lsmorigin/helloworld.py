from google.appengine.ext import webapp
from google.appengine.ext.webapp.utill import run_wsgi_app

class MainPage(webapp.RequestHandler):
	"""docstring for MainPage"""
	def get(self):
		self.response.headers['Content-Type']='type/plain'
		self.response.out.write('Hello, webapp World!')

application = webapp.WSGIApplication(
	[('/',MainPage)],
	debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
		