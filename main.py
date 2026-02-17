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
def user_create():
    try:
         name = input('Enter your name: ')
         username = input('Enter your username: ')
         email = input('Enter your email: ')
         password = input('Enter your password: ')
         phone = input('Enter your phone number: ')
         address = input('Enter your address: ')
         is_active = True if input('Enter your are active (Y/N): ') == 'Y' else False
         cur.execute('insert into  if not exists data (name, email, username, password, phone, address, is_active) values(%s, %s, %s, %s, %s, %s, %s)',
                     (name, email, username, password, phone, address, is_active))
         conn.commit()
         print('User created successfully...')
         main()
    except psycopg2.Error as e:
        print('This member already exists!!!')
        main()

def user_delete():
    username = input('Enter your username: ')
    try:
        cur.execute(f'delete from data where username = {username};')
        conn.commit()
        print(f'User {username} - sucsessfully deleted...')
        main()
    except psycopg2.Error as e:
        print('This member not found in the database!!!')
        main()

def main():
    print("""
1. Create user
2. Update user
3. Delete user
4. Show users
0. Exit""")

    # cmd = input(">>>\s")
    # if cmd == "1":
    #     user_create()
    # elif cmd == "2":
    #     user_update()
    # elif cmd == "3":
    #     user_delete()
    # elif cmd == "4":
    #     show_users()
    # elif cmd == "0":
    #     exit()
    # else:
    #     print("Invalid command")
    #     main()