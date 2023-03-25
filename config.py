from sqlite3 import connect


def connect_db():
    try:
        conn = connect('DeviceInfo.db')
        return conn
    except Exception as e:
        print(e)


def close_db(cursor, conn):
    cursor.close()
    conn.close()


def insert_db(dev_info: list):
    try:
        conn = connect('DeviceInfo.db')
        cursor = conn.cursor()

        create_db_cmd = '''
        CREATE TABLE IF NOT EXISTS DEVICEINFO
        (DEVNAME VARCHAR(16) UNIQUE NOT NULL,
        DEVTYPE VARCHAR(16) NOT NULL,
        DEVMODEL VARCHAR(16) NOT NULL,
        DEVIP VARCHAR(32) UNIQUE NOT NULL,
        DEVSITE VARCHAR(16) NOT NULL
        );
        '''
        cursor.execute(create_db_cmd)
        insert_data_cmd = '''
        INSERT INTO DEVICEINFO(DEVNAME,DEVTYPE,DEVMODEL,DEVIP,DEVSITE) VALUES(?,?,?,?,?)
        '''
        cursor.execute(insert_data_cmd, dev_info)
        conn.commit()

    except Exception as e:
        print(e)
