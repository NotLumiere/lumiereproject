from .core import db

conn = db.get_conn()

def cek_var():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM variable')
    result = cursor.fetchall()
    cursor.close()
    return result

def get_var(var):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    cur = conn.cursor()
    cur.execute('SELECT value FROM variable WHERE vars = ?', (var,))
    try:
        raw = cur.fetchone()
        cur.close()
        if raw:
            return raw[0]
        else:
            return None
    except Exception as e:
        cur.close()
        print(f"Error getting variable: {e}")
        return None

def set_var(var, value):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    try:
        cek = get_var(var)
        if cek is not None:
            conn.execute('UPDATE variable SET value = ? WHERE vars = ?', (value, var))
        else:
            conn.execute('INSERT INTO variable (vars, value) VALUES (?, ?)', (var, value))
        conn.commit()
    except Exception as e:
        print(f"Error setting variable: {e}")

def del_var(var):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present AyiinXd <https://github.com/AyiinXd>
    """
    try:
        conn.execute('DELETE FROM variable WHERE vars = ?', (var,))
        conn.commit()
    except Exception as e:
        print(f"Error deleting variable: {e}")
