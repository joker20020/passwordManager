from Crypto.Hash import SHA256
from random import randbytes

import PWsql
from PWsql import PWDataBase as DataBase
from password import PWcontroller

class User():
    def __init__(self,name,pw,database,key):
        self.name = name
        self.pw = pw
        self.db = DataBase(database)
        keyGenerator = SHA256.new()
        keyGenerator.update(self.name.encode("utf-8"))
        keyGenerator.update(self.pw.encode("utf-8"))
        keyGenerator.update(bytes.fromhex(key))
        self.controller = PWcontroller(keyGenerator.digest())

    def add_item(self,theme,name,pw,description,path="",Itype="未分类"):
        self.db.create_pw_table(self.name)
        tail,pw = self.controller.encrypt(pw)
        self.db.insert_table(self.name,["THEME","NAME","PASSWORD","DESCRIPTION","TAIL","PATH","TYPE"],[theme,name,pw,description,tail,path,Itype])

    def remove_item(self,theme):
        self.db.create_pw_table(self.name)
        self.db.delete(self.name,THEME = theme)

    def get_item(self,theme):
        self.db.create_pw_table(self.name)
        item = self.db.where(self.name,[],THEME=theme)
        if not len(item):
            return []
        item = item[0]
        try:
            pw = self.controller.decrypt(item[2])
            pw = pw[0:-item[4]].decode("utf-8")
        except:
            pw = ""
            pass
        result = [item[0],item[1],pw,item[3],item[5],item[6]]
        return result

    def get_all(self):
        self.db.create_pw_table(self.name)
        items = self.db.sql_cmd(f"""SELECT THEME,TYPE FROM {self.name} ;
                """)
        if not len(items):
            return []
        result = []
        for item in items:
            result.append([item[0],item[1]])
        return result

    def search(self,theme):
        self.db.create_pw_table(self.name)
        items = self.db.sql_cmd(f"""SELECT * FROM {self.name} 
        WHERE THEME LIKE '%{theme}%';
        """)
        if not len(items):
            return []
        result = []
        for item in items:
            try:
                pw = self.controller.decrypt(item[2])
                pw = pw[0:-item[4]].decode("utf-8")
            except:
                pw = "None"
            result.append([item[0], item[6]])
        return result

    def update(self,theme,**new_data):
        self.db.create_pw_table(self.name)
        try:
            tail,pw = self.controller.encrypt(new_data["PASSWORD"])
        except:
            tail = 0
            pw = "None"
        new_data["PASSWORD"] = pw
        new_data["TAIL"] = tail
        self.db.update(self.name,new_data,THEME=theme)

    def update_type(self,new_type,old_type):
        self.db.create_pw_table(self.name)
        self.db.update(self.name, {"TYPE":new_type}, TYPE=old_type)

class Admin():
    def __init__(self,database):
        self.name = "user"
        self.db = DataBase(database)

    def add_item(self,name, pw):
        self.db.create_user_table(self.name)
        pw = SHA256.new(pw.encode("utf-8")).hexdigest()
        self.db.insert_table(self.name, ["NAME", "PASSWORD", "KEY"],
                             [name, pw, randbytes(16).hex()])

    def remove_item(self, name):
        self.db.create_user_table(self.name)
        self.db.delete(self.name, NAME=name)

    def get_item(self, name):
        self.db.create_user_table(self.name)
        item = self.db.where(self.name, [], NAME=name)
        return item

    def search(self, theme):
        self.db.create_user_table(self.name)
        items = self.db.sql_cmd(f"""SELECT * FROM {self.name} 
        WHERE THEME LIKE '%{theme}%';
        """)
        return items

    def update(self, name, **new_data):
        self.db.create_user_table(self.name)
        self.db.update(self.name, new_data, NAME=name)
    def login(self,name,pw):
        self.db.create_user_table(self.name)
        items = self.db.sql_cmd(f"""SELECT PASSWORD FROM {self.name} 
                WHERE NAME = '{name}';
                """)
        if not len(items):
            return False
        pw = SHA256.new(pw.encode("utf-8")).hexdigest()
        if pw == items[0][0]:
            return True
        else:
            return False

    def new_user(self,name,pw):
        self.db.create_user_table(self.name)
        items = self.db.sql_cmd(f"""SELECT NAME FROM {self.name} 
                        WHERE NAME = '{name}';
                        """)
        if not len(items):
            self.add_item(name,pw)
            return True
        else:
            return False

if __name__ == "__main__":
    a = Admin("./src/db/users.db")
    # print(a.get_item("test123"))
    # a.add_item("test123", "123456")
    # name = input("name:")
    # pw = input("password:")
    # if a.login(name,pw):
    #     u = User(name, pw, "pw.db",a.get_item(name)[0][2])
    #     u.add_item("test2", "test", "test@123456", "This is a test")
    #     # u.update("test2",PASSWORD="123456")
    #     print(u.get_item("test2"))
    #     print(u.search("te"))
    u = User("test123", "123456", "./src/db/pw.db", a.get_item("test123")[0][2])
    u.add_item("test2", "test", "test@123456", "This is a test")
    # u.update("test2",PASSWORD="12333")
    print(u.get_all())
    print(u.get_item("test2"))
