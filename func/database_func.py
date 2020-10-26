import sqlite3


# Return connection to db
def connect_to_db():
    conn = sqlite3.connect('data.db')
    return conn


# Return a single value from table
def get_config_value(column, table_name):

    # Execute database commands
    conn = connect_to_db()
    value = conn.execute('SELECT "' + column + '" FROM "' + table_name + '"').fetchone()
    conn.close()

    # Return value
    return value[0]


# Return column
def get_column_data(column, table_name):

    # Execute database commands
    conn = connect_to_db()
    items = conn.execute('SELECT ' + column + ' FROM ' + table_name + '').fetchall()
    conn.close()

    # Return value
    return items


# Writes list of items to db
def write_list_to_db(items, table_name, column):

    # Connect to database
    conn = connect_to_db()

    # For each item in list
    for item in items:
        conn.execute('INSERT INTO ' + table_name + ' ("' + column + '") VALUES("' + item + '")')

    # Close connection
    conn.commit()
    conn.close()


# Removes list of items from db
def remove_list_from_db(items, table_name, column):

    # Connect to database
    conn = connect_to_db()

    # For each item in list
    for item in items:
        conn.execute('DELETE FROM ' + table_name + ' WHERE ' + column + ' = "' + item + '"')

    # Close connection
    conn.commit()
    conn.close()

'''
# Remove from list in database
def remove_from_list(items, table):
    
    # Connect to database
    conn = connect_to_db()

    # For each item in list
    for item in items:
        conn.execute('INSERT INTO ' + table + ' VALUES("' + item + '")')

    # Close connection
    conn.commit()
    conn.close()
'''