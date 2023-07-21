from sql import DataBase

RESERVED_THEME = "reserved for saving types can not be used"
class PWDataBase(DataBase):
    def __init__(self,file_path,*params):
        super().__init__(file_path,*params)
        self.init_type = False

    def create_pw_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
        THEME TEXT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        DESCRIPTION TEXT,
        TAIL INTEGER NOT NULL,
        PATH TEXT,
        TYPE TEXT NOT NULL
        );
        """.format(name))
        if (not self.init_type) and not len(self.where(name,[],THEME=RESERVED_THEME)):
            self.insert_table(name,["THEME","NAME","PASSWORD","DESCRIPTION","TAIL","PATH","TYPE"],[RESERVED_THEME,"None","afeea6ac1a93fbab1e3638d1e9e35c67","None",0,"None","未分类,"])
            self.init_type = True
        self.connection.commit()

if __name__ == "__main__":
    db = PWDataBase("test.db")
    db.create_pw_table("test")
    # db.insert_table("test",["THEME","NAME","PASSWORD","DESCRIPTION","TAIL","PATH","TYPE"],[RESERVED_THEME," None","None","None",0,"None","未分类,"])
    print(db.where("test",[],THEME=RESERVED_THEME))



