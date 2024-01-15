import streamlit as gui
import pandas as pd

gui.set_page_config(layout="wide")

gui.header("The Best Company")
description = """
Apple Inc. (formerly Apple Computer, Inc.) is a multinational technology company that designs, develops, and sells consumer electronics, computer software, and online services. It is known for its products such as the iPhone, iPad, Mac computers, Apple Watch, and Apple TV. Apple is also the creator of the iOS and macOS operating systems, as well as various software applications and services like iTunes, iCloud, and Apple Music. The company is headquartered in Cupertino, California.

"""
gui.write(description)

gui.subheader("Our Team")

col1, col2, col3 = gui.columns(3)

df = pd.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        gui.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        gui.write(row['role'])
        gui.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        gui.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        gui.write(row['role'])
        gui.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        gui.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        gui.write(row['role'])
        gui.image(f"images/{row['image']}")
