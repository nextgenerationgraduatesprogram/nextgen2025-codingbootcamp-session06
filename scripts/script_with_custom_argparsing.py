import sys


if __name__ == "__main__":    
    # example of custom arg parsing
    parsed_args = dict()
    for idx, arg in enumerate(sys.argv):
        if idx > 0: # avoid the script name
            if "--" in arg: # is it a name?
                key = arg[2:] # trim off the "--" at the start
                val = sys.argv[idx+1] # get the following value
                parsed_args[key] = val # store
    print(parsed_args)

    # validate the args
    assert "x" in parsed_args, f"must provide x"
    assert "y" in parsed_args, f"must provide y"

    # do something
    z = x + y
    print(f"{float(x)} + {float(y)} = {z}")
