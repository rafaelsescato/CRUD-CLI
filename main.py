# coding = UTF-8

from os import system

from src.student import Student
from src.course import Course
from src.dao_mysql import StudentDAO, CourseDAO

def menu():
    return """
    \r.=====================================================================.
    \r|  -----------------------------------------------------------------  |    
    \r|             ALUNO               |             CURSO                 |
    \r|  -----------------------------------------------------------------  |  
    \r|  [1] Cadastrar Aluno            |  [5] Cadastrar Curso              |
    \r|  [2] Exibir Alunos              |  [6] Exibir Cursos                |
    \r|  [3] Alterar Cadastro de Aluno  |  [7] Alterar Cadastro de Curso    |
    \r|  [4] Remover Aluno              |  [8] Remover Curso                |
    \r|  -----------------------------------------------------------------  |
    \r|                              [9] Sair                               |
    \r|_____________________________________________________________________|
    \n\r>: """

def read_option():
    while True:
        system("cls")
        student = Student()
        course  = Course()
        option  = str(input(menu()))
        if option in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            
            system("cls")
            
            if(option == "1"):
                print("ALUNOS")
                print("-"*20)
                StudentDAO().read()
                
                print("CURSOS")
                print("-"*20)
                CourseDAO().read()
                
                print("DADOS DE CADASTRO")
                print("-"*20)
                student.set_id_student(input("ID: "))
                student.set_name(input("Nome: "))
                student.set_email(input("Email: "))
                student.set_address(input("Endereço: "))
                student.set_city(input("Cidade: "))
                student.set_uf(input("UF: "))
                student.set_id_course(input("Curso_ID: "))
                StudentDAO().create(student)
    
            elif(option == "2"):
                StudentDAO().read()
            
            elif(option == "3"):
                print("ALUNOS")
                print("-"*20)
                StudentDAO().read()
                
                print("CURSOS")
                print("-"*20)
                CourseDAO().read()
                
                print("DIGITE O ID DO ALUNO QUE DESEJA ATUALIZAR, EM SEGUIDA ATUALIZE AS INFORMAÇÕES")
                print("-"*20)
                student.set_id_student(input("ID: "))
                student.set_name(input("Nome: "))
                student.set_email(input("Email: "))
                student.set_address(input("Endereço: "))
                student.set_city(input("Cidade: "))
                student.set_uf(input("UF: "))
                student.set_id_course(input("Curso_ID: "))
                StudentDAO().update(student)
                             
            elif(option == "4"):
                print("ALUNOS")
                print("-"*20)
                StudentDAO().read()
                
                print("DIGITE O ID DO ALUNO QUE DESEJA REMOVER")
                print("-"*20)
                student.set_id_student(input("ID: "))
                StudentDAO().delete(student)
            
            elif(option == "5"):
                print("CURSOS")
                print("-"*20)
                CourseDAO().read()
                
                print("DADOS DE CADASTRO")
                print("-"*20)
                course.set_id_course(input("ID: "))
                course.set_description(input("Nome: "))
                course.set_price(input("Preço: "))
                course.set_period(input("Periodo: "))
                CourseDAO().create(course)
            
            elif(option == "6"):
                CourseDAO().read()
            
            elif(option == "7"):
                print("CURSOS")
                print("-"*20)
                CourseDAO().read()

                print("DIGITE O ID DO CURSO QUE DESEJA ATUALIZAR, EM SEGUIDA ATUALIZE AS INFORMAÇÕES")
                print("-"*20)
                course.set_id_course(input("ID: "))
                course.set_description(input("Nome: "))
                course.set_price(input("Preço: "))
                course.set_period(input("Periodo: "))
                CourseDAO().update(course)
            
            elif(option == "8"):
                print("CURSOS")
                print("-"*20)
                CourseDAO().read()

                print("DIGITE O ID DO CURSO QUE DESEJA REMOVER")
                print("-"*20)
                course.set_id_course(input("ID: "))
                CourseDAO().delete(course)
            
            elif(option == "9"):
                break

            system("pause")
    
if __name__ == "__main__":
    read_option()