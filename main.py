import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1",
    database="why",
    port="5432"
)
cur = conn.cursor()
cur.execute("create table if not exists data ("
            "id serial primary key,"
            "name varchar(255) not null,"
            "username varchar(255) unique not null,"
            "email varchar(255) not null unique,"
            "password varchar(100) not null,"
            "phone varchar(255) not null,"
            "address varchar(255) not null,"
            "is_active boolean not null"
            ");")
conn.commit()



def user_update():
    id = int(input(" id:"))
    name = input("name:")
    username = input("username:")
    email = input("email:")
    password = input("password:")
    phone = input("phone:")
    address = input("address:")
    is_active = input("is_active:")
    if is_active.lower() == "true":
        is_active = True
    else:
        is_active = False

    try:
        cur.execute(f"update data set name='{name}', username='{username}', email='{email}', password='{password}', phone='{phone}', address='{address}', is_active='{is_active}' where id='{id}';")
        conn.commit()
        print("User updated successfully!")
        main()
    except psycopg2.Error as e:
        print("This member does not exist!")
        main()
def show_users():
    cur.execute("select * from data")
    data = cur.fetchall()
    for row in data:
        print(row)
    main()
def main():
    print("""
1. Create user
2. Update user
3. Delete user
4. Show users
0. Exit""")

    cmd = input(">>>")
    if cmd == "1":
        user_create()
    elif cmd == "2":
        user_update()
    elif cmd == "3":
        user_delete()
    elif cmd == "4":
        show_users()
    elif cmd == "0":
        exit()
    else:
        print("Invalid command")
        main()

main()