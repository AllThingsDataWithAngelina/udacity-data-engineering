import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
    print("Existing tables dropped...")


def create_tables(cur, conn):
    print("Creating new tables...")
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
    print("New tables created")
    

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    print('Connecting to the cluster...')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    print('Connected to the cluster')

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()