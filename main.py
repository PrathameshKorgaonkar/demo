import jenkins
import argparse
import time

parser = argparse.ArgumentParser()
args_list = [
    ('--URL',),
    ('--USERNAME',),
    ('--PASSWORD',),
    ('--JOB_NAME',),
    ('--VERSION',),
    ('--CREDENTIALS',),
    ('--SPACE_NAME',),
    ('--SPACE_ID',),
    ('--STORE_MODELS',),
    ('--STORE_IN',),
    ('--INCLUDE_FILTER',),
    ('--PYTEST_MARKER',),
    ('--PARALLELISM_VALUE',),
]
for arg in args_list:
    parser.add_argument(*arg)
args = parser.parse_args()
 
try:
    server = jenkins.Jenkins(args.URL, username=args.USERNAME, password=args.PASSWORD)
 
    build_parameters = {
        'VERSION': args.VERSION,
        'CREDENTIALS': args.CREDENTIALS,
        'SPACE_NAME': args.SPACE_NAME,
        'SPACE_ID': args.SPACE_ID,
        'STORE_MODELS': args.STORE_MODELS,
        'STORE_IN': args.STORE_IN,
        'INCLUDE_FILTER': args.INCLUDE_FILTER,
        'PYTEST_MARKER': args.PYTEST_MARKER,
        'PARALLELISM_VALUE': args.PARALLELISM_VALUE
    }
 
    queue_item = server.build_job(args.JOB_NAME, build_parameters)
 
    build_info = server.get_queue_item(queue_item)
    while build_info.get('executable') is None:
        time.sleep(1)
        build_info = server.get_queue_item(queue_item)
 
    build_number = build_info['executable']['number']
 
    console_output = server.get_build_console_output(args.JOB_NAME, build_number)
    print(f"{console_output}")
except jenkins.JenkinsException as e:
    print(f"Failed to connect to Jenkins Server: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
