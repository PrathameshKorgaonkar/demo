def main(config):
    # Extract values from the config dictionary
    VERSION = config.get("VERSION")
    CREDENTIALS = config.get("CREDENTIALS")
    SPACE_NAME = config.get("SPACE_NAME")
    SPACE_ID = config.get("SPACE_ID")
    STORE_MODELS = config.get("STORE_MODELS")
    STORE_IN = config.get("STORE_IN")
    INCLUDE_FILTER = config.get("INCLUDE_FILTER")
    PYTEST_MARKER = config.get("PYTEST_MARKER")
    PARALLELISM_VALUE = config.get("PARALLELISM_VALUE")
 
    # Print the values
    print("VERSION:", VERSION)
    print("CREDENTIALS:", CREDENTIALS)
    print("SPACE_NAME:", SPACE_NAME)
    print("SPACE_ID:", SPACE_ID)
    print("STORE_MODELS:", STORE_MODELS)
    print("STORE_IN:", STORE_IN)
    print("INCLUDE_FILTER:", INCLUDE_FILTER)
    print("PYTEST_MARKER:", PYTEST_MARKER)
    print("PARALLELISM_VALUE:", PARALLELISM_VALUE)
 
if __name__ == "__main__":
    import sys
    # This allows the script to be run directly with a config dict
    if len(sys.argv) > 1:
        import ast
        config = ast.literal_eval(sys.argv[1])
        main(config)
