import sqlite3
import threading
import time
 
class db:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._connection = None
        return cls._instance

    def get_conn(self):
        if self._connection is None:
            self._connection = sqlite3.connect('app.db',check_same_thread=False)
        return self._connection
    
    def close_conn(self):
        if self._connection:
            self._connection.close()
            self._connection = None

class db_init(db):
    def __init__(self):
        self._connection = None
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY, name TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                          (id INTEGER PRIMARY KEY, user_id INTEGER, product TEXT,
                           FOREIGN KEY(user_id) REFERENCES users(id))''')
        cursor.execute("INSERT OR IGNORE INTO users (id, name) VALUES (1, 'Alice')")
        cursor.execute("INSERT OR IGNORE INTO users (id, name) VALUES (2, 'Bob')")
        cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, product) VALUES (1, 1, 'Laptop')")
        cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, product) VALUES (2, 1, 'Mouse')")
        cursor.execute("INSERT OR IGNORE INTO orders (id, user_id, product) VALUES (3, 2, 'Keyboard')")
        conn.commit()


class UserService:
    def __init__(self):
        self.db_instance = db()
        

    def get_user(self, user_id):
        conn = self.db_instance.get_conn()  # Use the singleton connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        #conn.close()
        return result
    
class UserService_singleton:

    def get_user(self, user_id):
        conn = sqlite3.connect('app.db')  # Another new connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result
 
class OrderService_singleton:
    def __init__(self):
        self.db_instance = db()

    def get_orders(self, user_id):
        #conn = sqlite3.connect('app.db')  # Another new connection
        conn=self.db_instance.get_conn()  # Use the singleton connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        #conn.close()
        return result
    
class OrderService:

    def get_orders(self, user_id):
        conn = sqlite3.connect('app.db')  # Another new connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result

   
#db_init()  # Initialize the database and tables
start=time.perf_counter()
get_user=UserService()
get_order=OrderService()

print(get_user.get_user(1))
print(get_order.get_orders(1))

print(f"thread count: {threading.active_count()}")
end=time.perf_counter()
print(f"processing time: {end - start:.6f} 秒")

# Using singleton pattern for database connection
start1=time.perf_counter()
get_user_s=UserService_singleton()
get_order_s=OrderService_singleton()

print(get_user_s.get_user(1))
print(get_order_s.get_orders(1))

print(f"thread count: {threading.active_count()}")
end1=time.perf_counter()
print(f"processing time of singleton: {end1 - start1:.6f} 秒")
