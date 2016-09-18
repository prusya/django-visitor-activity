from django.conf import settings
import logging
import urllib

logger = logging.getLogger('visitor_activity')


class VisitorActivity(object):
    """
      def __init__(self):
          self.logger = logging.getLogger('visitor_activity')
          self.logger.setLevel(logging.INFO)
          filename = settings.VISITOR_ACTIVITY_LOGGER_FILENAME or 'visitor_activity.log'
          fh = logging.FileHandler(filename=filename)
          fh.setLevel(logging.INFO)
          formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
          fh.setFormatter(formatter)
          self.logger.addHandler(fh)
          self.logger.info('VisitorActivityLogger initialized')
          """

    def process_request(self, request):
        message = 'x-forwarded[{}] ' \
                  'ip[{}] ' \
                  'method[{}] ' \
                  'url[{}] ' \
                  'user[{}] ' \
                  'agent[{}] ' \
                  'data[{}]'. \
            format(request.META.get('HTTP_X_FORWARDED_FOR', ''),
                   request.META.get('REMOTE_ADDR', ''),
                   request.method,
                   request.path,
                   request.user,
                   request.META['HTTP_USER_AGENT'],
                   urllib.parse.unquote(request.body.decode('utf-8')))
        logger.info(message)
        return None
