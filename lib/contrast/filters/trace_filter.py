class TraceFilter(object):
    ExpandCard = 'card'
    ExpandEvents = 'events'
    ExpandNotes = 'notes'
    ExpandRequest = 'request'
    ExpandApplication = 'application'

    TimestampFirst = 'FIRST'
    TimestampLast = 'LAST'

    def __init__(self):
        self.filter_text = None
        self.start_date = None
        self.end_date = None
        self.filter_tags = []
        self.severities = []
        self.statuses = []
        self.vuln_types = []
        self.servers = []
        self.environments = []
        self.urls = []
        self.modules = []
        self.timestamp_filter = ''
        self.expand = []
        self.limit = 20
        self.offset = 0
        self.sort = '-lastTimeSeen'


    def get_params_as_json(self):
        return {
            'filterText': self.filter_text,
            'startDate': self.start_date,
            'endDate': self.end_date,
            'filterTags': ','.join(self.filter_tags),
            'severities': ','.join(self.severities),
            'status': ','.join(self.statuses),
            'vulnTypes': ','.join(self.statuses),
            'servers': ','.join(self.servers),
            'environments': ','.join(self.environments),
            'urls': ','.join(self.urls),
            'modules': ','.join(self.modules),
            'timestampFilter': self.timestamp_filter,
            'expand': ','.join(self.expand),
            'limit': self.limit,
            'offset': self.offset,
            'sort': self.sort
        }