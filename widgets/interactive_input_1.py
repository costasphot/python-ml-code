# interactive_input_1.py

from ipywidgets import widgets
from IPython.display import display

text = widgets.Text(
    placeholder = "Type something and press Enter.",
		continuous_update = False
)
display(text)

def HandleChange(change):
	print(change["new"])  # The new value.
	
text.observe(HandleChange, names = "value")
