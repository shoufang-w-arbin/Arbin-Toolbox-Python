import os
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))

clr.AddReference("System")
clr.AddReference(os.path.join(current_dir, "bin", "ArbinCTI"))
clr.AddReference(os.path.join(current_dir, "bin", "ArbinDataModel"))