import multiprocessing

wsgi_app = 'app.wsgi'
bind = '127.0.0.1:8000'
workers = multiprocessing.cpu_count() * 2 + 1
limit_request_fields = 32000
limit_request_field_size = 0
loglevel = "info"
