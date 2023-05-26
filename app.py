import streamlit as st
import snowflake.connector as sf

# Snowflake connection details
connection_config = {
    'user': 'YOUR_USERNAME',
    'password': 'YOUR_PASSWORD',
    'account': 'YOUR_ACCOUNT_URL',
    'warehouse': 'YOUR_WAREHOUSE',
}

# Establish the Snowflake connection
conn = None

# Create Snowflake connection function
def create_connection(username, password, account, warehouse):
    connection_config['user'] = username
    connection_config['password'] = password
    connection_config['account'] = account
    connection_config['warehouse'] = warehouse

    try:
        global conn
        conn = sf.connect(**connection_config)
        st.success("Snowflake connection established successfully!")
    except Exception as e:
        st.error(f"Error connecting to Snowflake: {str(e)}")

# Get list of databases
def get_databases():
    try:
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [row[0] for row in cursor]
        return databases
    except Exception as e:
        st.error(f"Error fetching databases: {str(e)}")
        return []

# Get list of schemas in a database
def get_schemas(database):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SHOW SCHEMAS IN DATABASE {database}")
        schemas = [row[0] for row in cursor]
        return schemas
    except Exception as e:
        st.error(f"Error fetching schemas: {str(e)}")
        return []

# Get list of tables/views in a schema
def get_tables(schema):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SHOW TABLES IN SCHEMA {schema}")
        tables = [row[0] for row in cursor]
        return tables
    except Exception as e:
        st.error(f"Error fetching tables/views: {str(e)}")
        return []

# Main function
def main():
    st.title("Snowflake Connection")

    # Snowflake connection form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    account = st.text_input("Account URL")
    warehouse = st.text_input("Warehouse")

    if st.button("Connect"):
        create_connection(username, password, account, warehouse)

    # Database, Schema, and Table/View selection form
    if conn is not None:
        databases = get_databases()
        selected_database = st.selectbox("Select Database", databases)

        schemas = get_schemas(selected_database)
        selected_schema = st.selectbox("Select Schema", schemas)

        tables = get_tables(selected_schema)
        selected_table = st.selectbox("Select Table/View", tables)

        st.success(f"Selected Database: {selected_database}")
        st.success(f"Selected Schema: {selected_schema}")
        st.success(f"Selected Table/View: {selected_table}")

if __name__ == '__main__':
    main()