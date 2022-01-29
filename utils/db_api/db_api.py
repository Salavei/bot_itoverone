import sqlite3
import datetime


class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add_announcements(self, type_of_services, job_title, job_description, salary, phone, user_id, allow=False):
        with self.connection:
            print(phone)
            return self.cursor.execute(
                "INSERT INTO `tg_my_announcements` (`type_of_services`,`job_title`,`job_description`,"
                "`salary`,`phone`,`allow`, `date_time`, `user_id_id`) VALUES(?,?,?,?,?,?,?,?)",
                (type_of_services, job_title,
                 job_description, salary, phone, allow, datetime.datetime.now(), user_id))

    def get_announcements_all(self, allow=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_announcements` WHERE `allow` = ?", (allow,)).fetchall()

    def get_admin_announcements_all(self, allow=False):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_announcements` WHERE `allow` = ?", (allow,)).fetchall()

    def get_announcements_my(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_announcements` WHERE `user_id_id` = ?",
                                       (user_id,)).fetchall()

    def check_subscriber(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `tg_users` WHERE `tg_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def subscriber_exists(self):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `tg_users`', ).fetchall()
            return len(result)

    def add_subscriber(self, user_id, status=True):
        """Добавляем нового подписчика"""
        nums = self.subscriber_exists()
        print(nums)
        with self.connection:
            return self.cursor.execute("INSERT INTO `tg_users` (`id`,`tg_id`) VALUES(?,?)", (int(nums) + 1, user_id))

    def add_resume(self, name, skills, area_of_residence, phone, user_id, allow=False):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `tg_my_resume` (`name`,`skills`,`area_of_residence`,"
                "`phone`,`allow`, `date_time`, `user_id_id`) VALUES(?,?,?,?,?,?,?)",
                (name, skills,
                 area_of_residence, phone, allow, datetime.datetime.now(), user_id))

    def get_resume_all(self, allow=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_resume` WHERE `allow` = ? ORDER BY `date_time` DESC",
                                       (allow,)).fetchall()

    def update_resume_my(self, name, skills, area_of_residence, phone, user_id, allow=True):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `tg_my_resume` SET `name` = ? ,`skills` = ? ,`area_of_residence` = ?,`phone` = ? ,`allow` = ?, `date_time` = ?, `user_id_id` = ? WHERE `user_id_id` = ?",
                (name, skills,
                 area_of_residence, phone, allow, datetime.datetime.now(), user_id, user_id))

    def get_resume_my(self, user_id: int) -> list:
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_resume` WHERE `user_id_id` = ?", (user_id,)).fetchall()

    def get_resume_for_adm(self, allow=False) -> list:
        with self.connection:
            return self.cursor.execute("SELECT * FROM `tg_my_resume` WHERE `allow` = ?", (allow,)).fetchall()

    def stop_resume(self, user_id, resume_id=None):
        with self.connection:
            take_id = self.cursor.execute("SELECT `id` FROM `tg_users` WHERE `tg_id` =?", (int(user_id),)).fetchall()
            pars = self.cursor.execute("UPDATE `tg_my_resume` SET `allow` = ? WHERE `id` = ?", (0, *take_id[0],))
            return pars

    def confirm_my_resume(self, id_conf: int) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_resume` SET `allow` = ? WHERE `id` =?", (True, id_conf))

    def confirm_announcements(self, id_conf: int) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_announcements` SET `allow` = ? WHERE `id` =?", (True, id_conf))

    def update_announcements(self, id_conf: int, allow) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_announcements` SET `allow` = ? WHERE `id` =?", (allow, id_conf))

    def check_announcements(self, id_resume: int) -> bool:
        with self.connection:
            return \
            self.cursor.execute("SELECT `allow` FROM `tg_my_announcements` WHERE `id` = ?", (id_resume,)).fetchone()[0]
            # return bool(self.cursor)

    def start_my_resume(self, id_resume: int) -> bool:
        with self.connection:
            return self.cursor.execute("SELECT `allow` FROM `tg_my_resume` WHERE `id` = ?", (id_resume,)).fetchone()[0]
            # return bool(self.cursor)

    def update__my_resume(self, id_resume, allow: int) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_my_resume` SET `allow` = ? WHERE `id` =?", (allow, id_resume))

    def why_get_admin(self, ) -> list:
        with self.connection:
            self.cursor.execute('''
                SELECT tg_id FROM tg_users
                WHERE admin = ?
            ''', (True,))
        return [admin[0] for admin in self.cursor.fetchall()]

    def get_admin(self, user_id, allow_admin) -> list:
        with self.connection:
            return self.cursor.execute("UPDATE `tg_users` SET `admin` = ? WHERE `tg_id` =?", (allow_admin, user_id))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
