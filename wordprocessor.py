import zerogui as zg

# Initialize the ZeroGUI application
app = zg.Application()

# Create the main window
main_window = zg.Window(title="Simple Word Processor")

# Add a text area for word processing
text_area = zg.TextArea(width=500, height=400)

# Add a save button
def save_text():
    with open("document.txt", "w") as f:
        f.write(text_area.get_text())

save_button = zg.Button(text="Save", command=save_text)

# Add a load button
def load_text():
    try:
        with open("document.txt", "r") as f:
            text_area.set_text(f.read())
    except FileNotFoundError:
        pass

load_button = zg.Button(text="Load", command=load_text)

# Arrange the components in the main window
main_window.add(text_area)
main_window.add(save_button)
main_window.add(load_button)

# Run the application
app.run(main_window)
