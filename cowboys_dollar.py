def cowboys_dollars(boots: list[str]) -> str:
    search = "[(1)]"
    counter = [0, 0]
        
    for i, boot in enumerate(boots):
        segments = boot.split("&")[0]
        counter[i] = segments.count(search)
        
    return f"This Rhinestone Cowboy has {counter[1]} dollar bills in his right boot and {counter[0]} in the left"