# interactive_input_2.py

import ipywidgets as widgets
from IPython.display import display

text = widgets.Text(placeholder = "Type something...")
submit_button = widgets.Button(description = "Submit")

display(widgets.HBox([text, submit_button]))

def HandleClick(_):
  print(text.value)

# The method 'on_submit()' is deprecated.
submit_button.on_click(HandleClick)
