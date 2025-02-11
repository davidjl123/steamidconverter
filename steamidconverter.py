# Steam ID Converter
# by davidjl123
# steamID3, steamID64

import tkinter as tk
from tkinter import ttk

def extract(id_64):
    """Extracts the short-form Steam ID from a long-form ID."""
    return id_64 % (1 << 32)

def build_id(short_id):
    """Builds the long-form Steam ID from a short-form ID."""
    BASE = 103582791429521408  # This base is divisible by 2^32
    return BASE + short_id

def convert_id():
    """Converts the input Steam ID based on the current mode."""
    input_text = entry.get().strip()
    try:
        num = int(input_text)
        if conversion_mode.get():
            # Convert short-form to long-form
            result = build_id(num)
            output_var.set(f"Long-form ID: {result}")
        else:
            # Convert long-form to short-form
            result = extract(num)
            output_var.set(f"Short-form ID: {result}")
    except ValueError:
        output_var.set("Invalid input! Please enter a valid integer.")

def clear_fields():
    """Clears the input field and the output message."""
    entry.delete(0, tk.END)
    output_var.set("")

def copy_output():
    """Copies only the number portion of the current output text to the clipboard."""
    text = output_var.get()
    # Look for a colon and split off the descriptive part if present.
    if ":" in text:
        # Split on the first colon and take the part after it.
        number_text = text.split(":", 1)[1].strip()
    else:
        number_text = text
    if number_text:
        root.clipboard_clear()
        root.clipboard_append(number_text)

def toggle_conversion_mode():
    """Updates labels and button text when the conversion mode is toggled."""
    if conversion_mode.get():
        convert_btn.config(text="Convert to Long-form")
    else:
        convert_btn.config(text="Convert to Short-form")

# Create the main application window
root = tk.Tk()
root.title("Steam ID Converter")
root.resizable(False, False)

# Set up ttk style for a modern look
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10))
style.configure("TEntry", font=("Segoe UI", 10))

# Create a main frame with padding
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.grid(row=0, column=0, sticky="NSEW")

# Header Section (centered)
header_label1 = ttk.Label( main_frame, text="Steam ID Converter", font=("Segoe UI", 12, "bold"), anchor="center" )
header_label1.grid(row=0, column=0, columnspan=2, sticky="EW", pady=(0, 5))
header_label2 = ttk.Label( main_frame, text="by davidjl123 (jk3)", font=("Segoe UI", 10), anchor="center" )
header_label2.grid(row=1, column=0, columnspan=2, sticky="EW", pady=(0, 5))
header_label3 = ttk.Label( main_frame, text="steamID3, steamID64", font=("Segoe UI", 10), anchor="center" )
header_label3.grid(row=2, column=0, columnspan=2, sticky="EW", pady=(0, 10))

# Conversion mode variable:
# False -> long-form to short-form (default)
# True  -> short-form to long-form
conversion_mode = tk.BooleanVar(value=False)

# Input Section
id_label = ttk.Label(main_frame, text="Enter Steam ID:")
id_label.grid(row=3, column=0, sticky="W", pady=(0, 10))
entry = ttk.Entry(main_frame, width=30)
entry.grid(row=3, column=1, sticky="EW", pady=(0, 10))
main_frame.columnconfigure(1, weight=1)

# Checkbox to toggle conversion mode
toggle_cb = ttk.Checkbutton(
    main_frame,
    text="Convert short-form to long-form",
    variable=conversion_mode,
    command=toggle_conversion_mode
)
toggle_cb.grid(row=4, column=0, columnspan=2, sticky="W", pady=(0, 10))

# Buttons Section
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=(0, 10))
# Convert button in its own row
convert_btn = ttk.Button(button_frame, text="Convert to Short-form", command=convert_id)
convert_btn.grid(row=0, column=0, columnspan=2, pady=(0, 10))
# Clear and Copy buttons in the row below, side by side
clear_btn = ttk.Button(button_frame, text="Clear", command=clear_fields)
clear_btn.grid(row=1, column=0, padx=(0, 10))
copy_btn = ttk.Button(button_frame, text="Copy", command=copy_output)
copy_btn.grid(row=1, column=1)

# Output Section
output_var = tk.StringVar()
output_label = ttk.Label(main_frame, textvariable=output_var, foreground="blue")
output_label.grid(row=6, column=0, columnspan=2, pady=(10, 0))

# Start the GUI event loop
root.mainloop()