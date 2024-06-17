import jenkins
import argparse
import time
 
def fetch_live_logs(server, job_name, build_number):
    console_log = server.get_build_console_output(job_name, build_number)
    print("Live Console Output:")
    print(console_log)
 
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
 
    # Trigger the build
    queue_item_info = server.build_job(args.JOB_NAME, parameters=build_parameters)
 
    if queue_item_info:
        queue_item_number = queue_item_info['id']
        print(f"Build queued successfully. Job ID: {queue_item_number}")
 
        # Wait for the build to start
        time.sleep(10)  # Adjust delay as needed
 
        # Poll until the build completes
        build_info = server.get_build_info(args.JOB_NAME, queue_item_number)
        build_number = build_info['number']
        build_result = build_info['result']
 
        while build_result is None:
            time.sleep(5)
            build_info = server.get_build_info(args.JOB_NAME, queue_item_number)
            build_result = build_info['result']
 
            # Fetch and display live logs
            fetch_live_logs(server, args.JOB_NAME, build_number)
 
        # Once build completes, fetch final logs
        fetch_live_logs(server, args.JOB_NAME, build_number)
 
        # Display final build status
        print(f"Build '{args.JOB_NAME}' {build_result}")
 
    else:
        print(f"Failed to trigger '{args.JOB_NAME}'.")
 
except jenkins.JenkinsException as e:
    print(f"Failed to connect to Jenkins Server: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
