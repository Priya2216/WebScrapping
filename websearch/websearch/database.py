# use sqlite to test connection and create table
import _sqlite3

conn = _sqlite3.connect('myquotes.db')
curr = conn.cursor()

curr.execute('''create table quotes_tb(
            title text,
            author text,
            tag text)
            ''')


# curr.execute("""
# insert into quotes_tb values ('python','autho','a')
# """)

conn.commit()
conn.close()