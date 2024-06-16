import argparse
 
def main():
    parser = argparse.ArgumentParser(description='Process some parameters.')
    
    # Define the arguments
    parser.add_argument('--VERSION', type=str, help='Version')
    parser.add_argument('--CREDENTIALS', type=str, help='Credentials')
    parser.add_argument('--SPACE_NAME', type=str, help='Space Name')
    parser.add_argument('--SPACE_ID', type=str, help='Space ID')
    parser.add_argument('--STORE_MODELS', type=str, help='Store Models')
    parser.add_argument('--STORE_IN', type=str, help='Store In')
    parser.add_argument('--INCLUDE_FILTER', type=str, help='Include Filter')
    parser.add_argument('--PYTEST_MARKER', type=str, help='Pytest Marker')
    parser.add_argument('--PARALLELISM_VALUE', type=str, help='Parallelism Value')
    
    # Parse the arguments from the command line
    args = parser.parse_args()
    
    # Print the parameters
    print(f"VERSION: {args.VERSION}")
    print(f"CREDENTIALS: {args.CREDENTIALS}")
    print(f"SPACE_NAME: {args.SPACE_NAME}")
    print(f"SPACE_ID: {args.SPACE_ID}")
    print(f"STORE_MODELS: {args.STORE_MODELS}")
    print(f"STORE_IN: {args.STORE_IN}")
    print(f"INCLUDE_FILTER: {args.INCLUDE_FILTER}")
    print(f"PYTEST_MARKER: {args.PYTEST_MARKER}")
    print(f"PARALLELISM_VALUE: {args.PARALLELISM_VALUE}")
 
if __name__ == "__main__":
    main()
