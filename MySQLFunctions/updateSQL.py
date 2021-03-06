import mysql.connector as sql
from DBandTables.ConnectionToDB import DatabaseConnection
from Classes.Objects import *

def updateStudent(Student):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Students SET FirstName = %s, LastName = %s, " \
			   "MiddleInitial = %s, Suffix = %s, PreferredName = %s, " \
			   "DateOfBirth = %s, Gender = %s, Race = %s, Address = %s, " \
			   "City = %s, State = %s, Zip = %s, Email = %s, " \
			   "PhoneNumber = %s, DisabilityInfo = %s, HealthConditions = " \
			   "%s, Siblings %s, SchoolName = %s, SchoolDistrict = %s, " \
			   "SchoolType = %s, GradeInFall = %s, ExpectedHighSchool = %s, " \
			   "ExpectedGradYear = %s, GT = %s, ELL = %s, UserName = %s, " \
			   "Password = %s WHERE StudentID = %s"
		vals = (Student.FirstName, Student.LastName, Student.MiddleInitial, Student.Suffix, Student.PreferredName, Student.DateOfBirth, Student.Gender, Student.Race, Student.Address, Student.City, Student.State, Student.Zip, Student.Email, Student.PhoneNumber, Student.DisabilityInfo, Student.HealthConditions, Student.Siblings, Student.SchoolName, Student.SchoolDistrict, Student.SchoolType, Student.GradeInFall, Student.ExpectedHighSchool, Student.ExpectedGradYear, Student.GT, Student.ELL, Student.UserName, Student.Password, Student.id)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateApplicant(Applicant):
	try:
		db = DatabaseConnection()
		c = db.cursor()

		aB = Applicant.ApproversFirstName + " " + Applicant.ApproversLastName
		stmt = "UPDATE Students SET AcceptedStatus = %s, ApprovedBy = %s WHERE StudentID = %s"
		var1 = str(Applicant.AcceptedStatus)
		var2 = Applicant.StudentID
		vals = (var1, aB, var2[0])

		c.execute(stmt, vals)

		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateParent(Parent):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Parents SET FirstName = %s, LastName = %s, Address = %s, " \
			   "City = %s, State = %s, Zip = %s, Email = %s, " \
			   "CellPhoneNumber = %s, WorkPhoneNumber = %s, HomePhoneNumber = " \
			   "%s WHERE ParentID = %s AND StudentID = %s"
		vals = (Parent.StudentID, Parent.FirstName, Parent.LastName, Parent.Address, Parent.City, Parent.State, Parent.Zip, Parent.Email, Parent.CellPhoneNumber, Parent.WorkPhoneNumber, Parent.HomePhoneNumber, Parent.ParentID, Parent.StudentID)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateMentor(oldMentor, newMentor):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Mentor SET InstructorID = %s, StudentID = %s WHERE InstructorID = %s AND StudentID = %s"
		vals = (newMentor.InstructorID, newMentor.StudentID, oldMentor.InstructorID, oldMentor.InstructorID)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateInstructor(Instructor):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Instructors SET FirstName = %s, LastName = %s, " \
			   "UserName = %s, Password = %s WHERE StudentID = %s"
		vals = (Instructor.FirstName, Instructor.LastName, Instructor.UserName, Instructor.Password, Instructor.InstructorID)
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateClass(Class):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Classes SET ClassName = %s, InstructorID = %s, " \
			   "Session = %s, Level = %s, " \
			   "TimeSlot = %s, Building = %s, RoomNumber = %s, Capacity = %s, " \
			   "NumberOfStudentsRegistered = %s, NumberOfStudentsWaitListed = %s WHERE ClassID = %s"
		vals = (Class.InstructorID, Class.Session, Class.Level, Class.TimeSlot, Class.Building, Class.RoomNumber, Class.Capacity, Class.NumberOfStudentsRegistered, Class.NumberOfStudentsWaitListed, Class.ClassID)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateTake(oldTake, Take):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Takes SET ClassID = %s WHERE StudentID = %s AND ClassID = %s"
		vals = (Take.ClassID, Take.StudentID, oldTake.ClassID)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateAdditionalInfo(AdditionalInfo):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE AdditionalInfo SET Status = %s, FundingStatus = %s, " \
			   "GrantName = %s, NationalClearingHouse = %s WHERE StudentID = %s"
		vals = (AdditionalInfo.Status, AdditionalInfo.FundingStatus, AdditionalInfo.GrantName, AdditionalInfo.NationalClearingHouse, AdditionalInfo.StudentID)
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateEditedStudent(Student1):
	try:
		db = DatabaseConnection()
		c = db.cursor()

		stmt = "UPDATE Students SET FirstName = %s, LastName = %s, " \
			   "MiddleInitial = %s, Suffix = %s, PreferredName = %s, " \
			   "DateOfBirth = %s, Gender = %s, Race = %s, Address = %s, " \
			   "City = %s, State = %s, Zip = %s, Email = %s, " \
			   "PhoneNumber = %s, DisabilityInfo = %s, HealthConditions = %s," \
			   "Siblings = %s, SchoolName = %s, SchoolDistrict = %s, " \
			   "SchoolType = %s, GradeInFall = %s, ExpectedHighSchool = %s, " \
			   "ExpectedGradYear = %s, GT = %s, ELL = %s " \
			   "WHERE UserName = %s"
		vals = (Student1.FirstName, Student1.LastName, Student1.MiddleInitial,
				Student1.Suffix, Student1.PreferredName, Student1.DateOfBirth, Student1.Gender, Student1.Race,
				Student1.Address, Student1.City, Student1.State, Student1.Zip, Student1.Email, Student1.PhoneNumber,
				Student1.DisabilityInfo, Student1.HealthConditions, Student1.Siblings, Student1.SchoolName,
				Student1.SchoolDistrict, Student1.SchoolType, Student1.GradeInFall, Student1.ExpectedHighSchool,
				Student1.ExpectedGradYear, Student1.GT, Student1.ELL, Student1.UserName)

		c.execute(stmt, vals)

		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)


def updateEditClass(EditCourse, courseid):
	try:
		db = DatabaseConnection()
		c = db.cursor()

		print(courseid)

		var = "'" + courseid + "'"

		stmt = "UPDATE Classes SET ClassName = %s, Classes.Session = %s, Classes.Level = %s, TimeSlot = %s, " \
			   "Building = %s, RoomNumber = %s, Capacity = %s WHERE ClassID = '" + courseid + "'"


		vals = (EditCourse.className, EditCourse.session, EditCourse.level, EditCourse.timeSlot, EditCourse.building,
				EditCourse.roomNumber, EditCourse.capacity)

		print(courseid[0])
		print(vals)
		c.execute(stmt, vals)

		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updatePersonnelProfile(firstName, lastName, username):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		stmt = "UPDATE Instructors SET FirstName = %s, LastName = %s WHERE UserName = %s"
		vals = (firstName, lastName, username)
		c.execute(stmt, vals)
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def studentUpdateProfile(Student2, username):
	try:
		db = DatabaseConnection()
		c = db.cursor()

		stmt = "UPDATE Students SET FirstName = %s, LastName = %s, " \
			   "MiddleInitial = %s, Suffix = %s, PreferredName = %s, " \
			   "DateOfBirth = %s, Gender = %s, Race = %s, Address = %s, " \
			   "City = %s, State = %s, Zip = %s, Email = %s, " \
			   "PhoneNumber = %s, DisabilityInfo = %s, HealthConditions = %s," \
			   "Siblings = %s, SchoolName = %s, SchoolDistrict = %s, " \
			   "SchoolType = %s, GradeInFall = %s, ExpectedHighSchool = %s, " \
			   "ExpectedGradYear = %s, GT = %s, ELL = %s " \
			   "WHERE UserName = %s"
		vals = (Student2.FirstName, Student2.LastName, Student2.MiddleInitial,
				Student2.Suffix, Student2.PreferredName, Student2.DateOfBirth, Student2.Gender, Student2.Race,
				Student2.Address, Student2.City, Student2.State, Student2.Zip, Student2.Email, Student2.PhoneNumber,
				Student2.DisabilityInfo, Student2.HealthConditions, Student2.Siblings, Student2.SchoolName,
				Student2.SchoolDistrict, Student2.SchoolType, Student2.GradeInFall, Student2.ExpectedHighSchool,
				Student2.ExpectedGradYear, Student2.GT, Student2.ELL, username)

		c.execute(stmt, vals)

		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateTake2(courseid, studentid):
	try:
		db = DatabaseConnection()
		c = db.cursor()

		stmt = "UPDATE Takes SET IsDeleted = '0' WHERE StudentID = %s AND ClassID = %s"
		vals = (studentid, courseid)

		c.execute(stmt, vals)

		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)