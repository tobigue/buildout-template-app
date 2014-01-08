from tornado.options import define


# Tornado

define("host", default="localhost", type=str,
       help="The host address.")

define("port", default=8888, type=int,
       help="The port the app listens on.")

define("debug", default=False, type=bool,
       help="Start tornado in debug mode")


# Logging

define("logfile", default="var/log/root.log", type=str,
       help="The path of the logfile.")

define("errormails", default=[], type=list,
       help="A list of email addresses to be notified in case of errors.")
