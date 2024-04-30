import pandas as pd
from tkinter import Tk, Button

# Function to create and save the DataFrame as a CSV file
def create_csv():
    data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
    df = pd.DataFrame(data)
    df.to_csv('output.csv', index=False)
    print("CSV file has been created")

# Setting up the GUI
root = Tk()
root.title("CSV Creator")
button = Button(root, text="Here", command=create_csv)
button.pack(pady=20)
root.mainloop()
