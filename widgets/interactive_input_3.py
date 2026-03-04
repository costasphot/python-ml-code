# interactive_input_3.py

import ipywidgets as widgets
from IPython.display import display

button = widgets.Button(description = "Click Me!")
output = widgets.Output()

def OnButtonClicked(_):
  # Display the message within the output widget.
  with output:
    output.clear_output()
    print("Button clicked.")

button.on_click(OnButtonClicked)
display(button, output)
