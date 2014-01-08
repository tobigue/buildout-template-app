import logging
import logging.handlers
import socket

from tornado.options import options


root = logging.getLogger()

formatter = logging.Formatter(' - '.join(['[%(asctime)s',
                                          '%(relativeCreated).3f]',
                                          '%(name)s',
                                          '%(levelname)s',
                                          '%(message)s']))

logfile_handler = logging.handlers.TimedRotatingFileHandler(options.logfile,
    when='midnight', interval=1, backupCount=10)
logfile_handler.setLevel(logging.INFO)
logfile_handler.setFormatter(formatter)
root.addHandler(logfile_handler)

if options.errormails:
    smtp_handler = logging.handlers.SMTPHandler(
        mailhost='localhost',
        fromaddr='logging',
        toaddrs=options.errormails,
        subject='[LOG] Error on server "%s"' % socket.gethostname())
    smtp_handler.setLevel(logging.ERROR)
    smtp_handler.setFormatter(formatter)
    root.addHandler(smtp_handler)
