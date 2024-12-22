import sqlite3


def convert_postgres_to_sqlite(postgres_dump_file, sqlite_db_file):
    with open(postgres_dump_file, 'r') as pg_dump:
        conn = sqlite3.connect(sqlite_db_file)
        cursor = conn.cursor()
        commands = pg_dump.read().split(';\n')
        for command in commands:
            if command.strip():
                try:
                    cursor.execute(command)
                except sqlite3.Error as e:
                    print(f"An error occurred: {e}")
        conn.commit()
        conn.close()


postgres_dump_file = 'yy.sql'
sqlite_db_file = 'zz.db'
convert_postgres_to_sqlite(postgres_dump_file, sqlite_db_file)
