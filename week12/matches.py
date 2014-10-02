users = [
    {
        "name": "bob",
        "interests": [
            "rock music",
            "cue sports"
        ]
    },
    {
        "name": "carol",
        "interests": [
            "classical music",
            "hiking"
        ]
    }
]

events = [
    {
        "name": "Rialto Open",
        "description": "cue sports billiards tournament"
    },
    {
        "name": "Blues Festival",
        "description": "Rocking Blues Guitars"
    }
]
# out = {}
# for u in users:
#     for i in u["interests"]:
#         for e in events:
#             found = False
#             keys = e.keys()
#             for f in keys:
#                 if i in e[f]:
#                     found = True
#             if found:
#                 out[e["name"]] = e
# print(out)


class Matcher(object):
    _out = {}

    def __init__(self, events):
        self.events = events

    def getMatches(self, user):
        self._out = {}
        self.user = user
        for i in user["interests"]:
            self._matchInterests(i)
        return self._out

    def _matchInterests(self, i):
        for e in self.events:
            if self._isMatch(i, e):
                self._out[e["name"]] = e

    def _isMatch(self, interest, event):
        found = False
        keys = event.keys()
        for key in keys:
            if interest in event[key]:
                found = True
        return found

if __name__ == "__main__":
    m = Matcher(events)
    for user in users:
        print user["name"] +"="+ str(m.getMatches(user))

    # prints {'Rialto Open': {'name': 'Rialto Open', 'description': 'cue sports billiards tournament'}}