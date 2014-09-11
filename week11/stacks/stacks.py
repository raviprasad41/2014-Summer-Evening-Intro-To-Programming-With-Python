loose_change = [
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
]
# How many stacks of N units can we make for each denomination of coin?
grouped = {}
stack_limit = 4

for coin in loose_change:
    denomination = coin["denomination"]
    if denomination not in grouped.keys():
        grouped[denomination] = [ [] ]
    last_stack = grouped[denomination][-1]
    if len(last_stack) < stack_limit:
        last_stack.append(coin)
    else:
        new_stack = []
        new_stack.append( coin)
        grouped[denomination].append(new_stack)

for denomination in grouped:
    stacks = grouped[denomination]
    print(str(len(stacks)) + " stack of " + denomination)