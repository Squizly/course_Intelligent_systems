import re

from knowledge_base.questions import *
from knowledge_base.rules import *
from expert_system import *
from gui import *

if __name__ == "__main__":

    app = RealEstateApp()
    app.mainloop()