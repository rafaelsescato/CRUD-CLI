# coding = UTF-8

import mysql.connector

class FactoryConnection:

    def get_connection(self):
        try:
            config = {
            "user":     "root",
            "password": "@mYsQl#",
            # "password": "",
            "host":     "127.0.0.1",
            "database": "db",
            }

            if mysql.connector.__version_info__ > (2, 1) and mysql.connector.HAVE_CEXT:
                config["use_pure"] = False

            return mysql.connector.connect(**config)

        except Exception as e:
            return print("\n", e, "\n")

class StudentDAO:
    database = None
    cursor   = None

    def create(self, student):
        try:
            self.database = FactoryConnection().get_connection()
            self.cursor   = self.database.cursor()

            values = (
                student.get_id_student(),
                student.get_name(),
                student.get_email(),
                student.get_address(),
                student.get_city(),
                student.get_uf(),
                student.get_id_course()
            )

            sql = (""
                "insert into student "
                "(id_student, _name, email, address, city, uf, id_course) "
                "values(%s, %s, %s, %s, %s, %s, %s)"
            "")

            self.cursor.execute(sql, values)
            self.database.commit()
            self.database.close()
            
            print("\nCadastrado com sucesso!!\n")

        except Exception as e:
            return print("\n", e, "\n")

    def read(self):
        try:
            self.database = FactoryConnection().get_connection()
            self.cursor   = self.database.cursor()
            
            sql = (""
                "select concat('id: ',id_student,'    nome: ', _name)"
                "from student order by _name"
            "")

            sql = (""
                "select concat_ws(', ',"
                "concat('ID: ', id_student),"
                "_name,"
                "email,"
                "address,"
                "city,"
                "uf,"
                "concat('Curso_ID: ', id_course))"
                "from student order by _name"
            "")

            self.cursor.execute(sql)

            for row in self.cursor:
                print(str(row).strip("\[\]\(\)\,\'"))

            self.database.commit()
            self.database.close()

            print("\n")

        except Exception as e:
            return print("\n", e, "\n")

    def update(self, student):
        try:
            self.database = FactoryConnection().get_connection()
            self.cursor   = self.database.cursor()
            
            values = (
                student.get_name(),
                student.get_email(),
                student.get_address(),
                student.get_city(),
                student.get_uf(),
                student.get_id_course(),
                student.get_id_student()
            )

            sql = (""
                "update student set "
                "_name = %s, "
                "email = %s, "
                "address = %s, "
                "city = %s, "
                "uf = %s, "
                "id_course = %s "
                "where id_student = %s" 
            "")

            self.cursor.execute(sql, values)
            self.database.commit()
            self.database.close()

            print("\nAtualizado com sucesso!!\n")

        except Exception as e:
            return print("\n", e, "\n")

    def delete(self, student):
        try:
            self.database = FactoryConnection().get_connection()
            self.cursor   = self.database.cursor()
            
            sql = (""
                "delete from student "
                "where id_student = {}".format(student.get_id_student())
            )
            
            self.cursor.execute(sql)
            self.database.commit()
            self.database.close()

            print("\nRemovido com sucesso!!\n")

        except Exception as e:
            return print("\n", e, "\n")

class CourseDAO:
    database = None
    cursor   = None

    def create(self, course):
        try:
            self.database = FactoryConnection().get_connection()
            self.cursor   = self.database.cursor()

            values = (
                course.get_id_course(),
                course.get_description(),
                course.get_price(),
                course.get_period()
            )

            sql = (""
                "insert into course "
                "(id_course, description, price, period) "
                "values(%s, %s, %s, %s)"
            "")

            self.cursor.execute(sql, values)
            self.database.commit()
            self.database.close()
            
            print("\nCadastrado com sucesso!!\n")

        except Exception as e:
            return print("\n", e, "\n")

    def read(self):
        try:
            self.database = FactoryConnection().get_connection()
            self.cursor   = self.database.cursor()
            
            sql = (""
                "select concat_ws(', ',"
                "concat('ID: ', id_course),"
                "description,"
                "price,"
                "period)"
                "from course order by description"
            "")

            self.cursor.execute(sql)

            for row in self.cursor:
                print(str(row).strip("\[\]\(\)\,\'"))

            self.database.commit()
            self.database.close()

            print("\n")

        except Exception as e:
            return print("\n", e, "\n")

    def update(self, course):
        try:
            self.database = FactoryConnection().get_connection()
            self.cursor   = self.database.cursor()
            
            values = (
                course.get_description(),
                course.get_price(),
                course.get_period(),
                course.get_id_course()
            )

            sql = (""
                "update course set "
                "description = %s, "
                "price = %s, "
                "period = %s "
                "where id_course = %s" 
            "")

            self.cursor.execute(sql, values)
            self.database.commit()
            self.database.close()

            print("\nAtualizado com sucesso!!\n")

        except Exception as e:
            return print("\n", e, "\n")

    def delete(self, course):
        try:
            self.database = FactoryConnection().get_connection()
            self.cursor   = self.database.cursor()
            
            sql = (""
                "delete from course "
                "where id_course = {}".format(course.get_id_course())
            )
            
            self.cursor.execute(sql)
            self.database.commit()
            self.database.close()

            print("\nRemovido com sucesso!!\n")

        except Exception as e:
            return print("\n", e, "\n")