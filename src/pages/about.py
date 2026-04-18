import streamlit as st

st.set_page_config(
    page_title="About - My First Frontend",
    page_icon="ℹ️"
)

st.title("About This Application")

st.markdown("""
## What is this application?

This is a learning tool designed to help you understand frontend development concepts. 
It's built using Streamlit, a Python library that makes it easy to create web applications.

## Key Concepts Demonstrated

1. **Pages and Navigation**
   - You're looking at a different page right now!
   - Notice how the URL changed
   - The sidebar navigation helps users move between pages

2. **Component Reuse**
   - The page configuration is similar across pages
   - We maintain consistent styling
   - Common elements appear on all pages

3. **State Management**
   - Each page maintains its own state
   - Try refreshing the page
   - Notice how values reset

## Try This!

1. Create a new file in the `pages` folder
2. Name it something like `my_page.py`
3. Copy some code from this page as a starting point
4. Modify it to create your own page!

Remember: The filename will determine the page's URL and navigation title.
""")

# Interactive element to demonstrate state is page-specific
if st.button("Click me!"):
    st.success("This button's state is independent from other pages!") 