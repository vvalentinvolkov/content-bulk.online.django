import multiprocessing

wsgi_app = 'app.wsgi'
bind = '0.0.0.0:80'
workers = multiprocessing.cpu_count() * 2 + 1
limit_request_fields = 32000
limit_request_field_size = 0
loglevel = "info"
