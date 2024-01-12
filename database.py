import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("task-database.db")
        self.cursor = self.con.corsor()

    def create_task_table(self):
        self.corsor.execute("CREATE TABLE IF NOT EXISTS task(id integer PRIMARY KEY AUTOINCREMENT , YASK VARCHAR(50) NOT NULL, complete BOOLEAN NOT NULL CHECK (completedIN (0,1)))")
        self.con.commit()

    def create_task(self, task, due_date):
        self.cursor.execute("INSERT INTO task(tssk, due_date, completes) VALUES(?,?,?)", (task, due_date, 0))
        self.con.commit()

        created_task = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE task = ? and completed = 0", (task,)).fetchall()
        return created_task[-1]
    
    def get_tasks(self):
        '''Getting all tasks : complete and incomplete '''
        incompleted_tasks = self.cursor.execute("SELECT id, task, due")

    def get_tasks(self):
        incompleted_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE co,pleted = 0").fetchall()
        completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE co,pleted = 1").fetchall()
        return incompleted_tasks, completed_tasks
    
    