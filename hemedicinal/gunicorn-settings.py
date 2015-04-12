#bind = "0.0.0.0:8000"
bind = "unix:/tmp/gunicorn_hemedicinal.sock"

workers = 2
proc_name = "hemedicinal"
#loglevel = 'debug'
