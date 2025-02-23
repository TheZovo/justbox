import sqlite3

class DB:
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def __del__(self):
        try:
            self.conn.close()
        except AttributeError:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def execute(self, sql, params=None):
        try:
            if params:
                return self.cursor.execute(sql, params)
            else:
                return self.cursor.execute(sql)
        except sqlite3.Error as e:
            print(f"SQL execution error: {e}")
            raise

    def commit(self):
        try:
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Commit error: {e}")
            raise

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def add_user(self, telegram_id, username):
        try:
            self.execute("""
                INSERT OR IGNORE INTO users (telegram_id, username, balance, orders)
                VALUES (?, ?, 0, 0)
            """, (telegram_id, username))
            self.commit()
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
            raise

    def add_order(self, telegram_id, order_data):
        try:
            self.execute("""
                INSERT INTO orders (telegram_id, order_id, photo, delivery, link, size, cost_uan, price_rub, price_usdt, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending')
            """, (
                telegram_id,
                order_data['order_id'],
                order_data['photo_path'],
                order_data['delivery'],
                order_data['link'],
                order_data['size'],
                order_data['cost_uan'],
                order_data['price_rub'],
                order_data['price_usdt']
            ))
            self.commit()
        except sqlite3.Error as e:
            print(f"Error adding order: {e}")
            raise

    def get_user_orders(self, telegram_id):
        try:
            self.execute("SELECT * FROM orders WHERE telegram_id = ?", (telegram_id,))
            return self.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching orders: {e}")
            raise

db = DB("justbox.db")

def init_db():
    try:
        db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            username TEXT,
            balance INTEGER DEFAULT 0,
            orders INTEGER DEFAULT 0
        );
        """)

        db.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            order_id INTEGER,
            photo TEXT,
            delivery TEXT,
            link TEXT,
            size TEXT,
            cost_uan TEXT,
            price_rub REAL,
            price_usdt REAL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (telegram_id) REFERENCES users (telegram_id)
        );
        """)

        db.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")