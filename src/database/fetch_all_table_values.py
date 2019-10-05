import sqlite3

from src.constants import DATABASE_FILE

conn = sqlite3.connect(DATABASE_FILE)


def save():
    c = conn.cursor()
    c.execute(
        "INSERT INTO hashtags VALUES (:themes,:groups,:hashtags)",
        {"themes": "camera", "groups": "bnw", "hashtags": "bnw"},
    )
    conn.commit()
    # conn.close()


save()

c = conn.cursor()
c.execute(
    """SELECT * FROM hashtags
"""
)
print(c.fetchall())

c.execute(
    """
    SELECT groups, hashtags FROM hashtags
    WHERE groups == 'BW'
    
"""
)
print('Grouped by themes')
results = c.fetchall()
print(results)

print('\n hashtags ')
for item in results:
    print(item[1])

# just themes
c.execute(
    """
    SELECT DISTINCT themes FROM hashtags

"""
)

print('\n Unique themes')
results = [item[0] for item in c.fetchall()]
print(results)


c.close()
