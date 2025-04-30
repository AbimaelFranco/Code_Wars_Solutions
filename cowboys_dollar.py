def cowboys_dollars(boots: list[str]) -> str:
    counter = [ boot.split("&")[0].count("[(1)]") for boot in boots]
        
    return f"This Rhinestone Cowboy has {counter[1]} dollar bills in his right boot and {counter[0]} in the left"