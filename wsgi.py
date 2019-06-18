import sys

p = '/home/russellromney/dash-blog/dash-blog'
if p not in sys.path:
    sys.path.append(p)

from app import server as application