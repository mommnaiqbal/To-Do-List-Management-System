from database import Database


class Todo:

    def __init__(self):
        self.db = Database()
        self.db.create_table()

    # Add Task
    def add_task(self, title, description, due_date, priority):
        query = """
        INSERT INTO tasks(title, description, due_date, priority)
        VALUES(?, ?, ?, ?)
        """
        self.db.execute(query, (title, description, due_date, priority))
        print("\n✅ Task added successfully!\n")

    # View All Tasks
    def view_tasks(self):
        tasks = self.db.fetchall("SELECT * FROM tasks")

        if not tasks:
            print("\nNo tasks found.\n")
            return

        print("\n========== TO-DO LIST ==========\n")

        for task in tasks:
            print(f"ID          : {task[0]}")
            print(f"Title       : {task[1]}")
            print(f"Description : {task[2]}")
            print(f"Due Date    : {task[3]}")
            print(f"Priority    : {task[4]}")
            print(f"Status      : {task[5]}")
            print("-" * 40)

    # Update Task
    def update_task(self, task_id, title, description, due_date, priority):
        query = """
        UPDATE tasks
        SET title=?,
            description=?,
            due_date=?,
            priority=?
        WHERE id=?
        """

        self.db.execute(
            query,
            (title, description, due_date, priority, task_id)
        )

        print("\n✅ Task updated successfully!\n")

    # Delete Task
    def delete_task(self, task_id):
        self.db.execute(
            "DELETE FROM tasks WHERE id=?",
            (task_id,)
        )

        print("\n🗑️ Task deleted successfully!\n")

    # Mark Complete
    def mark_complete(self, task_id):
        self.db.execute(
            "UPDATE tasks SET status='Completed' WHERE id=?",
            (task_id,)
        )

        print("\n✅ Task marked as completed!\n")

    # Search Task
    def search_task(self, keyword):

        tasks = self.db.fetchall(
            """
            SELECT *
            FROM tasks
            WHERE title LIKE ?
            """,
            ('%' + keyword + '%',)
        )

        if not tasks:
            print("\nNo matching task found.\n")
            return

        print("\nSearch Results\n")

        for task in tasks:
            print(task)

    # Filter by Status
    def filter_status(self, status):

        tasks = self.db.fetchall(
            "SELECT * FROM tasks WHERE status=?",
            (status,)
        )

        if not tasks:
            print(f"\nNo {status} tasks.\n")
            return

        print(f"\n{status} Tasks\n")

        for task in tasks:
            print(task)

    # Close Database
    def close(self):
        self.db.close()
