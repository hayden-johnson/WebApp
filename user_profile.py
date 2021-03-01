import wikipediaapi
from backend import Graph


# User Class: Holds learner profile + State
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.state = State()
        return


# State Class: Holds all dynamic user information from system
class State:
    def __init__(self, history=[], location="Machine Learning", goal="explore"):
        # uri = "bolt://3.84.92.216:7687"
        # user = "neo4j"
        # password = "exchanges-appraisals-intercoms"
        # self.graph = Graph(uri, user, password)  # Domain model
        self.history = history                   # Series of (location, goal, selection) triples
        self.location = location                 # Current Node in graph
        self.goal = goal                         # Learning Objective ("explore", "apply")
        self.refresh_options()                   # update options based on goal
        self.selection = ""                      # action selection
        self.is_terminal = False

    def update_state(self):
        self.history.append((self.location, self.goal, self.selection))
        self.selection = ""

    def refresh_options(self):
        if self.goal == "explore":
            self.options = ["Explore Options: ", " 1: Wiki", " 2: Introduction", " 3: Local concept map"]
        elif self.goal == "apply":
            self.options = [" 1: Tutorial", " 2: Methods", " 3: Tools"]
        # add defaults
        self.options = self.options + ["Default Options: ", " 4: Redefine goal",
                                       " 5: Recommend next steps", " 6: Path", " 7: Exit"]

    # helper for interface
    def goal_str(self):
        if self.goal == "explore":
            return "exploring"
        elif self.goal == "apply":
            return "applying"

    # helper for interface
    def print_options(self):
        s = "\n"
        print(s.join(self.options))

    ######################################################################################
    #                                  Explore Actions                                   #
    ######################################################################################

    # TODO: Find out why some pages cannot be found
    def get_wiki(self, len="short"):
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI)
        page_py = wiki_wiki.page(self.location.replace(' ', '_'))
        print("Page - Exists: %s" % page_py.exists())
        if len == "short":
            print("Page - Summary: \n%s" % page_py.summary)
        else:
            print(page_py.text)
        self.selection = "get_wiki"
        self.update_state()

    # TODO: create cypher query for to search by media type in current graph
    def get_intro(self):
        print("in get_intro")
        self.selection = "get_intro"
        self.update_state()

    # TODO: Find way to create visual representation of current graph
    def get_local_map(self):
        print("in redefine_goal")
        self.selection = "redefine_goal"
        self.update_state()

    ######################################################################################
    #                                   Apply Actions                                    #
    ######################################################################################
    def get_tutorial(self):
        print("in get_tutorial")
        self.selection = "get_tutorial"
        self.update_state()

    def get_methods(self):
        print("in get_methods")
        self.selection = "get_methods"
        self.update_state()

    def get_tools(self):
        print("in get_tools")
        self.selection = "get_tools"
        self.update_state()

    ######################################################################################
    #                                  Default Actions                                   #
    ######################################################################################

    # prompt user to redefine learning objective and topic based on current location
    # TODO: Make next locations dependent on reachable nodes in graph
    def redefine_goal(self):
        self.selection = "redefine_goal"
        self.update_state()
        print("Goals:\n   1: Explore\n   2: Apply\nTopics: \n   1: Supervised Learning\n   "
              "2: Unsupervised Learning\n   3: Reinforcement Learning")
        goal = int(input("\nGoal selection: "))
        topic = int(input("Topic selection: "))
        goal_switch = {
            1: "explore",
            2: "apply"
        }
        self.goal = goal_switch.get(goal, "invalid")
        topic_switch = {
            1: "Supervised Learning",
            2: "Unsupervised Learning",
            3: "Reinforcement Learning"
        }
        self.location = topic_switch.get(topic, "invalid")
        self.refresh_options()

    def rec_next_steps(self):
        print("in rec_next_steps")
        self.selection = "rec_next_steps"
        self.update_state()

    def get_path(self):
        print("in get_path")
        for i in self.history:
            print(f"({i[0]}, {i[1]}, {i[2]})")
        self.selection = "get_path"
        self.update_state()

    def terminate(self):
        self.is_terminal = True
        self.selection = "terminate"
        self.update_state()
