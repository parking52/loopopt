__author__ = 'melchior'

import time
from bokeh.plotting import figure, output_file, show
import numpy as np


def run_loop(outer_count, inner_count):

    for i in range(outer_count):
        for j in range(inner_count):
            pass

N = 1000
result_list = []

for value in range(N):
    start_time = time.time()
    run_loop(value, N - value)
    execution_time = time.time() - start_time
    result_list.append(execution_time)

result = np.array(result_list)
comp_result = []
for i in range(int(len(result)/2)):
    comp_result.append(result_list[i] - result_list[N-1-i])
# hence if result > 0, 2nd half takes less time => better have the bigger number as arg #1
# 25:75 < 75:25

print(comp_result)

output_file("lines.html", title="line plot example")
# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(range(len(comp_result)), np.array(comp_result), legend="Temp.", line_width=2)

# show the results
show(p)

##TODO 2D



