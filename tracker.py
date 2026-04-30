from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

#  this is for removing cache !!
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
absences = np.zeros(5)

def generate_graph():
    document.getElementById("output").innerHTML = ""
    plt.figure(figsize=(7, 4))
    
    # inputs
    plt.plot(days, absences, marker='o', color="#6dab82", linewidth=2)
    
    # parts of graph
    plt.title('Weekly Attendance (Absences)')
    plt.xlabel('Day')
    plt.ylabel('Number of Absences')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.ylim(bottom=0)

    display(plt.gcf(), target="output")
    plt.close()

# updates
def update_tracker(event):
    day_idx = int(document.getElementById("day").value)
    val = document.getElementById("absence").value
    
    if val:
        absences[day_idx] = int(val)
        document.getElementById("absence").value = ""
        generate_graph()

# generate hehe
generate_graph()