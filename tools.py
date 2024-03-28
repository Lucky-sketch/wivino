import sqlite3
import pandas as pd

def find_tables_info(db):
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()

        # Get table names
        q = """
        SELECT name
        FROM sqlite_schema
        WHERE type = 'table' AND name NOT LIKE 'sqlite_%';
        """
        cur.execute(q)
        tables = cur.fetchall()

        table_info = []
        for table in tables:
            table_name = table[0]

            # Get column information
            q_columns = f"PRAGMA table_info({table_name});"
            cur.execute(q_columns)
            columns = cur.fetchall()
            columns_df = pd.DataFrame(columns, columns=[desc[0] for desc in cur.description])

            # Get foreign key information
            q_foreign_keys = f"PRAGMA foreign_key_list({table_name});"
            cur.execute(q_foreign_keys)
            foreign_keys = cur.fetchall()
            foreign_keys_df = pd.DataFrame(foreign_keys, columns=[desc[0] for desc in cur.description])

            # Append table information to list
            table_info.append((table_name, columns_df, foreign_keys_df))

    return table_info


print(find_tables_info('db/vivino.db'))