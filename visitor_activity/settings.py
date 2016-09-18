from django.conf import settings
import logging
import logging.config

filename = getattr(settings, 'USER_ACTIVITY_LOG_FILENAME', 'visitor_activity.log')

VISITOR_ACTIVITY_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'visitor_activity_formatter': {
            'format': '%(asctime)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'visitor_activity_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': filename,
            'formatter': 'visitor_activity_formatter',
        },
    },
    'loggers': {
        'visitor_activity': {
            'handlers': ['visitor_activity_handler'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

LOGGING = getattr(settings, 'LOGGING', '{}')
if LOGGING:
    if 'formatters' in LOGGING.keys():
        LOGGING['formatters'].update(VISITOR_ACTIVITY_LOGGING['formatters'])
    else:
        LOGGING['formatters'] = VISITOR_ACTIVITY_LOGGING['formatters']

    if 'handlers' in LOGGING.keys():
        LOGGING['handlers'].update(VISITOR_ACTIVITY_LOGGING['handlers'])
    else:
        LOGGING['handlers'] = VISITOR_ACTIVITY_LOGGING['handlers']

    if 'loggers' in LOGGING.keys():
        LOGGING['loggers'].update(VISITOR_ACTIVITY_LOGGING['loggers'])
    else:
        LOGGING['loggers'] = VISITOR_ACTIVITY_LOGGING['loggers']
else:
    LOGGING.update(VISITOR_ACTIVITY_LOGGING)

logging.config.dictConfig(LOGGING)
