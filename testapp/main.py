from google.appengine.api import users
from google.appengine.ext import webapp

class MyHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ("Welcome, %s &lt;%s&gt;! (<a href=\"%s\">sign out</a>)" %
                        (user.nickname(), user.email(), users.create_logout_url("/")))
        else:
            greeting = ("<a href=\"%s\">Sign in or register</a>." %
                        users.create_login_url("/"))
            
        self.response.out.write("<html><body>%s</body></html>" % greeting)

def main():
    import wsgiref
    application = webapp.WSGIApplication(
        [('/', MyHandler),], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
