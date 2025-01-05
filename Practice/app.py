import streamlit as st
import json
import pandas as pd


# Function to convert JSON to CSV
def json_to_csv(json_data):
    try:
        # Load JSON data
        data = json.loads(json_data)

        # Convert JSON to DataFrame
        df = pd.json_normalize(data)

        # Convert DataFrame to CSV
        csv_data = df.to_csv(index=False)

        return csv_data

    except json.JSONDecodeError as e:
        st.error(f"Invalid JSON format: {e}")
        return None


# Streamlit app
st.title('JSON to CSV Converter')

# Sidebar navigation
menu = ["Home", "Upload & Edit", "Convert JSON"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.write("Welcome to JSON to CSV Converter App.")
    st.write("Select an option from the sidebar to proceed.")

elif choice == "Upload & Edit":
    st.header("Upload & Edit")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

    # Check if a file is uploaded
    if uploaded_file is not None:
        # Display the name of the uploaded file
        st.write("Filename: ", uploaded_file.name)

        # Read and display the file contents
        if uploaded_file.name.endswith('.csv'):
            # Read CSV file
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            # Read Excel file
            df = pd.read_excel(uploaded_file)

        # Editable dataframe
        edited_df = st.experimental_data_editor(df, num_rows="dynamic")

        # Display the edited dataframe
        st.write("Edited Data:")
        st.write(edited_df)

        # Option to download the edited data
        @st.cache_data
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df(edited_df)

        st.download_button(
            label="Download edited data as CSV",
            data=csv,
            file_name='edited_data.csv',
            mime='text/csv',
        )
    else:
        st.write("Please upload a file to see and edit the contents.")

elif choice == "Convert JSON":
    st.header("Convert JSON")

    # Radio button to choose input method
    input_method = st.radio("Choose input method:", ("Upload JSON File", "Enter JSON Manually"))

    if input_method == "Upload JSON File":
        # Upload JSON file section
        uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])

        if uploaded_file is not None:
            # Read uploaded JSON file
            json_data = uploaded_file.read()
            st.write("### JSON file content:")
            st.code(json_data, language='json')

            # Convert JSON to CSV
            csv_result = json_to_csv(json_data)
            df = pd.read_csv(csv_result)

            if csv_result:
                st.write("### CSV Output:")
                st.code(csv_result, language='csv')

                # Make CSV editable
                st.write("### Edit CSV Data:")
                edited_df = st.experimental_data_editor(df, num_rows=len(df))

                # Option to download edited data
                @st.cache_data
                def convert_df(csv_result):
                    return csv_result.to_csv(index=False).encode('utf-8')

                edited_csv = convert_df(edited_df)

                st.download_button(
                    label="Download edited data as CSV",
                    data=edited_csv,
                    file_name='edited_data.csv',
                    mime='text/csv',
                )
            else:
                st.warning("Please upload a valid JSON file.")

    elif input_method == "Enter JSON Manually":
        # Enter JSON manually section
        st.write("### Enter JSON data:")
        json_input = st.text_area("Paste JSON here", height=300)

        # Convert JSON to CSV
        csv_result = json_to_csv(json_input)
        df = pd.read_csv(csv_result)

        if csv_result:
            st.write("### CSV Output:")
            st.code(csv_result, language='csv')

            # Make CSV editable
            st.write("### Edit CSV Data:")
            edited_df = st.experimental_data_editor(df, num_rows=len(df))

            # Option to download edited data
            @st.cache_data
            def convert_df(csv_result):
                return df.to_csv(index=False).encode('utf-8')

            edited_csv = convert_df(edited_df)

            st.download_button(
                label="Download edited data as CSV",
                data=edited_csv,
                file_name='edited_data.csv',
                mime='text/csv',
            )
        else:
            st.warning("Please enter valid JSON data.")