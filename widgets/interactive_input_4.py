# interactive_input_4.py

import ipywidgets as widgets
from IPython.display import display

slider = widgets.IntSlider(value = 5, max = 10)
output = widgets.Output()

def OnChange(change):
  with output:
    output.clear_output()
    print("New value:", change["new"])

slider.observe(OnChange, names = "value")
display(slider, output)
