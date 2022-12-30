import mysql.connector
import dbconfig as cfg

class DigiCert:
    connection=""
    cursor =    ''
    host=       ''
    user=       ''
    password=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
        
    def createdatabase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql="create database "+ self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.closeAll()


    def createJobsTable(self):
        cursor = self.getcursor()
        sql = "CREATE TABLE jobs (id INT AUTO_INCREMENT PRIMARY KEY, Role VARCHAR(250), Company VARCHAR(250), YEAR_START INT, YEAR_END VARCHAR (100), Description VARCHAR (1000))"
        
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll()
    
    def createEducationTable(self):
        cursor = self.getcursor()
        sql="create table education (id int NOT NULL AUTO_INCREMENT,school varchar (200),course varchar (200),award varchar (100), year_start int, year_end int,primary key (id))"
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll()


    def createEducationRoW(self, values):
        
       cursor = self.getcursor()
       sql= "insert into education (school, course, award, year_start, year_end) values (%s, %s, %s,%s ,%s);"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.closeAll()
       return newid

    def createJobsRow(self, values):
            
       cursor = self.getcursor()
       sql= "insert into jobs (Role, Company, YEAR_START, YEAR_END, Description) values (%s, %s, %s, %s, %s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.closeAll()
       return newid
   
    def countschool(self,school):
        cursor = self.getcursor()
        sql="select count(*) from education where school like %s"
        values = (school, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        count = result[0]
        
        self.closeAll()
        return count
    
   


run = DigiCert()

if __name__ == "__main__":
    run.createdatabase()
    run.createJobsTable()
    run.createEducationTable()
    
    dataEducation = ('Salerno', 'Secondary School', 'Leaving Cert', 2009 ,2014)
    run.createEducationRoW(dataEducation)
    dataEducation = ('NUIG', 'BSC Microbiology', 'Second Class Honors',2014 ,2018)
    run.createEducationRoW(dataEducation)
    dataEducation = ('NUIG', 'MSC Biotechnology', 'Frist Class Honors',2018 ,2019)
    run.createEducationRoW(dataEducation)
    dataEducation = ('Labware', 'Instrument Interface Integration', 'Certificate',2019 ,2019)
    run.createEducationRoW(dataEducation)
    dataEducation = ('Labware', 'ELN Method Execution', 'Certificate', 2019 ,2019)
    run.createEducationRoW(dataEducation)
    dataEducation = ('Labware', 'Administration 1 ', 'Certificate', 2020 ,2020)
    run.createEducationRoW(dataEducation)
    dataEducation = ('Labware', 'Administration 2 ', 'Certificate', 2021 ,2021)
    run.createEducationRoW(dataEducation)

    
    dataJobs = ("Waitress ", "Papa Rich", 2018, 2019, " Wait on Tables, Take Orders, Great Customer Service ")
    run.createJobsRow(dataJobs)
    dataJobs = (" Researcher ", "WestWay Health", 2018, 2019, "Research Novel Forms of Antibiotics")
    run.createJobsRow(dataJobs)
    dataJobs = ("Laboraotry Business System Analyst", "Takeda", 2019, 2021, "LIMS-, MODA-, EMPOWER - System Administrator. Qualified Trainer. Responsible for testing and validating systems")
    run.createJobsRow(dataJobs)
    dataJobs = ("Senior Assocaite LabOps Developer ", "Pfizer", 2022, "current", "Database Migration management, Product Owner of LIMS system, System Implementation ")
    run.createJobsRow(dataJobs)

    count = run.countschool('Labware')
    print ("The number of completed courses from Labware are:", count)

   
    print("Run Check ")