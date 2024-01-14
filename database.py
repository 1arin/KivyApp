import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("task-database.db")
        self.cursor = self.con.cursor()

    def create_task_table(self):
        self.corsor.execute("CREATE TABLE IF NOT EXISTS tasks (id integer PRIMARY KEY AUTOINCREMENT , task varchar(50) NOT NULL, due_date varchar(50) completed BOOLEAN NOT NULL CHECK (completed IN (0,1)))")
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
    
    #Updating the tasks
    def mark_task_as_completed(self, taskid):
        '''Mark tasks as completed'''
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ? ", (taskid,))
        self.con.commit()

    def mark_task_as_incompleted(self, taskid):
        '''Mark tasks as incompleted'''
        self.cursor.execute("UPDATE tasks SET completed = 0 WHERE id = ? ", (taskid,))
        self.con.commit()

        #return the task text
        task_text = self.cursor.execute("SELECT task FRPM tasks WHERE id = ?",(taskid,)).fetchall()
        return task_text[0][0]
    
    # Deleting the task
    def delete_task(self, taskid):
        '''Delete  a task'''
        self.cursor.execute("DELETE FROM tasks WHRER id = ?", (taskid,))
        self.con.commit()

    # close the connection
    def close_db_connect(self):
        self.con.close()