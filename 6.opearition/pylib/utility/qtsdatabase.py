#coding=utf-8

class QtsDatabase(object) :
    def Connect(self):pass
    def Close(self):pass
    def Exist(self, sql):pass
    def Execute(self, sql,commit=True):pass
    def Query(self,sql):pass
    def Connected(self):pass
    def Commit(self):pass

    def Clear(self,table):
        self.Execute("DELETE FROM {0}".format(table))

    def QueryAll(self,table,fields=None):
        s_fields = ''
        if fields != None :
            for field in fields :
                if s_fields == '' :
                    s_fields = field
                else :
                    s_fields += ',' + field
        if s_fields == '' :
            s_fields = '*'
        return self.Query("SELECT {0} FROM {1}".format(s_fields,table))