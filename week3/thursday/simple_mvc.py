# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE
class Model(object):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = []

    def create(self, item):
        self.objects.append(item)


# VIEW: A TEMPLATE FOR A PAGE OR PAGE FRAGMENT
class View(object):
    def __init__(self, template, model):
        self.template = template
        self.model = model

    def render(self):
        output = ""
        for item in self.model:
            item_template = self.template
            for field in item:
                output += field
                # item_template.replace()
            output += item_template


# CONTROLLER: Routes messages
class Controller(object):
    def __init__(self):
        self.routes = {}

    def route(self, path):
        return map[path].view.render()


# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()

# CREATE AN APPLICATION INSTANCE
app = Application()

app.models.append("user", ["user_name", "date_of_birth"])
app.models.append("game", ["game_name", "description"])

app.models["user"].objects = [
    {"name": "Bob", "score": "0"},
    {"name": "Carol", "score": "0"},
    {"name": "Ted", "score": "0"},
    {"name": "Alice", "score": "0"}
]


page = View("model")

