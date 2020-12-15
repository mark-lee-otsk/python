import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect("misdev", "misdev123$", "10.65.224.211/ONEMIS")

cursor = connection.cursor()
cursor.execute("""
        SELECT loc_cd, loc_nm
        FROM dwc_location""")
       # WHERE LOC_CD = :did AND ROWNUM > :eid""",
       # did = 'USLGB',
       # eid = 190)
for fname, lname in cursor:
    print("Values:", fname, lname)