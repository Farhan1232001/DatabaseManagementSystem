import tkinter
from tkinter import *
from tkcalendar import *
import pymysql
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr

class studentRecords:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record System")
        self.root.geometry("1350x800+0+0")

        # Create notebook with tabs (ie window with tabs)
        notebook = ttk.Notebook(self.root)
        self.TabControl1 = ttk.Frame(notebook)
        self.TabControl2 = ttk.Frame(notebook)
        #self.TabControl3 = ttk.Frame(notebook)
        notebook.add(self.TabControl1, text="School System")
        notebook.add(self.TabControl2, text="Student Details")
        notebook.grid()

        # All variables that'll be used
        # ============================== Variables ============================================
        self.StudentID = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.Address = StringVar()
        self.PostCode = StringVar()
        self.Gender = StringVar()
        self.DOB = StringVar()
        self.Mobile = StringVar()
        self.Email = StringVar()
        self.ParentGuidance = StringVar()
        self.pgFirstName = StringVar()
        self.pgSurname = StringVar()
        self.pgAddress = StringVar()
        self.pgWorkPhone = StringVar()
        self.pgMobile = StringVar()
        self.pgEmail = StringVar()
        self.Course = StringVar()
        self.CourseCode = StringVar()
        self.Faculty = StringVar()
        self.Dean = StringVar()
        self.Head_of_School = StringVar()
        self.ProgramLeader = StringVar()
        self.CourseTutor = StringVar()
        self.Building = StringVar()
        self.HomeStudent = StringVar()
        self.Oversea = StringVar()
        self.Accommodation = StringVar()
        self.ExchangeProg = StringVar()
        self.Scholarship = StringVar()
        
        self.BA = StringVar()
        self.BSc = StringVar()
        self.MA = StringVar()
        self.MSc = StringVar()
        self.PhD = StringVar()
        
        self.DataScience = StringVar()
        self.EventDrivenPro = StringVar()
        self.ObjectOriented = StringVar()
        self.Spreadsheet = StringVar()
        self.SystemAnalysis = StringVar()
        self.InformationTechnology = StringVar()
        self.DigitalGraphics = StringVar()
        
        self.English = StringVar()
        self.Games = StringVar()
        self.Animation = StringVar()
        self.Database = StringVar()
        self.Maths = StringVar()
        self.AddMaths = StringVar()
        self.Physics = StringVar()
        self.Media = StringVar()
        self.GraphicsDesign = StringVar()

        self.ScoreMaths = StringVar()
        self.ScoreEnglish = StringVar()
        self.ScoreBiology = StringVar()
        self.ScoreComputing = StringVar()
        self.ExamNo = StringVar()
        self.ScoreChemistry = StringVar()
        self.ScorePhysics = StringVar()
        self.ScoreAddMaths = StringVar()
        self.ScoreBusiness = StringVar()
        self.TotalScore = StringVar()
        self.Average = StringVar()
        self.Ranking = StringVar()
        self.TaxPeriod = StringVar()
        self.iDate = StringVar()
        
        self.Module1 = StringVar()
        self.Module2 = StringVar()
        self.Module3 = StringVar()
        self.Module4 = StringVar()
        self.Module5 = StringVar()
        self.Module6 = StringVar()
        self.Module7 = StringVar()
        self.Module8 = StringVar()
        self.Ranking = StringVar()
        self.TotalScore = StringVar()
        self.ResultDate = StringVar()
        
        self.Subject1 = StringVar()
        self.Subject2 = StringVar()
        self.Subject3 = StringVar()
        self.Subject4 = StringVar()
        self.Subject5 = StringVar()
        self.Subject6 = StringVar()
        self.Subject7 = StringVar()
        self.Subject8 = StringVar()
        # ============================== Frames ===============================================

        MainFrame = Frame (self.TabControl1 ,bd=10, width =1350, height=700, relief=RIDGE)
        MainFrame.grid(padx=5, pady=10)

        Tab2Frame = Frame (self.TabControl2 ,bd=10, width =1350, height=700, relief=RIDGE)
        Tab2Frame.grid(padx=10)

        TopFrame3 = Frame (MainFrame ,bd=10, width =1340, height=500, relief=RIDGE)
        TopFrame3.grid()

        RightFramel = Frame (TopFrame3 ,bd=5, width =320, height=400, padx=2, bg="cadetblue" , relief=RIDGE)
        RightFramel.pack (side=RIGHT, pady=1)

        InnerRightFrame = Frame (RightFramel ,bd=5, width =310, height=300, padx=2, relief=RIDGE)
        InnerRightFrame .pack(side=TOP, pady=2)

        CalendarFrame = Frame (InnerRightFrame ,bd=5, width =310, height=300, padx=2, relief=RIDGE)
        CalendarFrame .pack(side=TOP,pady=1)


        UnitsFrame = Frame (InnerRightFrame ,bd=5, width =310, height=300, padx=2,relief=RIDGE)
        UnitsFrame.pack(side=TOP, pady=1)

        ResultFrame = Frame (InnerRightFrame ,bd=5, width =330, height=50, padx=2, relief=RIDGE)
        ResultFrame.pack (side=TOP, pady=1)

        ResultFrameLeft = Frame (ResultFrame ,bd=0, width =130, height=50, padx=2, relief=RIDGE)
        ResultFrameLeft.grid(row=0, column=0, pady=1)

        ResultFrameRight = Frame (ResultFrame ,bd=0, width =200, height=50, padx=2, relief=RIDGE)
        ResultFrameRight.grid(row=0, column=1)


        UnitNo = Frame (UnitsFrame ,bd=0, width =50, height=300, padx=2, relief=RIDGE)
        UnitNo.grid (row=0, column=0, pady=2)

        UnitSubject = Frame (UnitsFrame ,bd=1, width =210, height=300, padx=2, pady=4, relief=RIDGE)
        UnitSubject .grid(row=0,column=1,pady=2)

        UnitScore = Frame (UnitsFrame ,bd=0, width =50, height=300, padx=2, pady=3, relief=RIDGE)
        UnitScore .grid(row=0,column=2,pady=1)

        LeftFrame = Frame (TopFrame3 ,bd=5, width =1340, height=400, padx=2,bg="cadetblue" ,relief=RIDGE)
        LeftFrame.pack (side=RIGHT, pady=0)

        CourseFrame = Frame (LeftFrame ,bd=5, width =600, height=180, padx=4 ,relief=RIDGE)
        CourseFrame.pack (side=TOP, pady=2)

        LeftFrame2 = Frame (LeftFrame ,bd=5, width =600, height=180, padx=2,bg="cadetblue" ,relief=RIDGE)
        LeftFrame2.pack (side=TOP)

        StudentStatusFrame = Frame (LeftFrame2 ,bd=5, width =300, height=170, padx=2 ,relief=RIDGE)
        StudentStatusFrame.pack (side=LEFT)

        DegreeFrame = Frame (LeftFrame2 ,bd=5, width =300, height=170, padx=2 ,relief=RIDGE)
        DegreeFrame.pack (side=RIGHT)

        ButtonFrame = Frame (LeftFrame ,bd=5, width =320, height=50, padx=3,relief=RIDGE)
        ButtonFrame.pack(side=LEFT, pady=3)


        RightFrame2 = Frame(TopFrame3, bd=5, width=300, height=400, padx=2, bg="cadetblue", relief=RIDGE)
        RightFrame2.pack(side=LEFT, pady=5)
        StudentFrame = Frame(RightFrame2, bd=5, width=280, height=50, padx=2, relief=RIDGE)
        StudentFrame.pack(side=TOP, pady=3)
        ParentFrame = Frame(RightFrame2, bd=5, width=280, height=50, padx=3, relief=RIDGE)
        ParentFrame.pack(side=TOP)

        TopFrame11 = Frame(Tab2Frame, bd=10, width=1340, height=60, relief=RIDGE)
        TopFrame11.grid(row=0, column=0)
        TopFrame12 = Frame(Tab2Frame, bd=10, width=1340, height=100, relief=RIDGE)
        TopFrame12.grid(row=1, column=0)

        TopFrame12a = Frame(TopFrame12, bd=10, width=1000, height=100, relief=RIDGE)
        TopFrame12a.grid(row=1, column=1)
        TopFrame12b = Frame(TopFrame12, bd=10, width=340, height=100, relief=RIDGE)
        TopFrame12b.grid(row=1, column=0)
        # =====================================================================================
        self.lblStudentID = Label(StudentFrame, font=('arial', 12, 'bold'), text="Student ID", bd=7, anchor="w", justify=LEFT)
        self.lblStudentID.grid(row=0, column=0, sticky = W, padx=5, pady=5)
        self.txtStudentID = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable = self.StudentID)
        self.txtStudentID.grid(row=0, column=1)

        self.lblStudentname = Label(StudentFrame, font=('arial', 12, 'bold'), text="First name", bd=7, anchor="w", justify=LEFT)
        self.lblStudentname.grid(row=1, column=0, sticky = W, padx=5, pady=5)
        self.txtStudentname = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable = self.Firstname)
        self.txtStudentname.grid(row=1, column=1)

        self.lblSurname = Label(StudentFrame, font=('arial', 12, 'bold'), text="Surname", bd=7, anchor="w", justify=LEFT)
        self.lblSurname.grid(row=2, column=0, sticky = W, padx=5, pady=5)
        self.txtSurname = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable = self.Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(StudentFrame, font=('arial', 12, 'bold'), text="Address", bd=7, anchor="w", justify=LEFT)
        self.lblAddress.grid(row=3, column=0, sticky = W, padx=5, pady=5)
        self.txtAddress = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable = self.Address)
        self.txtAddress.grid(row=3, column=1)

        self.lblPostCode = Label(StudentFrame, font=('arial', 12, 'bold'), text="PostCode", bd=7, anchor="w", justify=LEFT)
        self.lblPostCode.grid(row=4, column=0, sticky = W, padx=5, pady=5)
        self.txtPostCode = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable = self.PostCode)
        self.txtPostCode.grid(row=4, column=1)

        self.lblGender = Label(StudentFrame, font=('arial', 12, 'bold'), text="Gender", bd=7, anchor="w", justify=LEFT)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5)
        self.cboGender = ttk.Combobox(StudentFrame, textvariable=self.Gender, width=23, font=('arial', 12, 'bold'), state='readonly')
        self.cboGender['value'] = ('', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1)

        self.lblDOB = Label(StudentFrame, font=('arial', 12, 'bold'), text="DOB", bd=7, anchor="w", justify=LEFT)
        self.lblDOB.grid(row=6, column=0, sticky = W, padx=5, pady=5)
        self.txtDOB = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable = self.DOB)
        self.txtDOB.grid(row=6, column=1)

        self.lblMobile = Label(StudentFrame, font=('arial', 12, 'bold'), text="Mobile", bd=7, anchor="w", justify=LEFT)
        self.lblMobile.grid(row=7, column=0, sticky = W, padx=5, pady=5)
        self.txtMobile = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable = self.Mobile)
        self.txtMobile.grid(row=7, column=1)

        self.lblEmail = Label(StudentFrame, font=('arial', 12, 'bold'), text="Email", bd=7, anchor="w", justify=LEFT)
        self.lblEmail.grid(row=8, column=0, sticky = W, padx=5, pady=5)
        self.txtEmail = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable = self.Mobile)
        self.txtEmail.grid(row=8, column=1)
        # =====================================================================================

        self.lblParentGuidance = Label(ParentFrame, font=('arial', 12, 'bold'), text="Parent or Guardian", bd=7, anchor="w", justify=LEFT)
        self.lblParentGuidance.grid(row=0, column=0, sticky=W, padx=5)
        self.cboParentGuidance = ttk.Combobox(ParentFrame, textvariable=self.ParentGuidance, width=16, font=('arial', 12, 'bold'), state='readonly')
        self.cboParentGuidance['value'] = ('', 'Mother', 'Father', 'Brother', 'Sister', 'Guidance')
        self.cboParentGuidance.current(0)
        self.cboParentGuidance.grid(row=0, column=1)

        self.lblStudentname = Label(ParentFrame, font=('arial', 12, 'bold'), text="First name", bd=7, anchor="w", justify=LEFT)
        self.lblStudentname.grid(row=1, column=0, sticky = W, padx=5, pady=5)
        self.txtStudentname = Entry(ParentFrame, font=('arial', 12, 'bold'), bd=5, width=17, justify='left', textvariable = self.pgFirstName)
        self.txtStudentname.grid(row=1, column=1)

        self.lblSurname = Label(ParentFrame, font=('arial', 12, 'bold'), text="Surname", bd=7, anchor="w", justify=LEFT)
        self.lblSurname.grid(row=2, column=0, sticky = W, padx=5, pady=5)
        self.txtSurname = Entry(ParentFrame, font=('arial', 12, 'bold'), bd=5, width=17, justify='left', textvariable = self.pgSurname)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(ParentFrame, font=('arial', 12, 'bold'), text="Address", bd=7, anchor="w", justify=LEFT)
        self.lblAddress.grid(row=3, column=0, sticky = W, padx=5, pady=5)
        self.txtAddress = Entry(ParentFrame, font=('arial', 12, 'bold'), bd=5, width=17, justify='left', textvariable = self.pgAddress)
        self.txtAddress.grid(row=3, column=1)

        self.lblWorkPhone = Label(ParentFrame, font=('arial', 12, 'bold'), text='Work Phone No', bd=5)
        self.lblWorkPhone.grid(row=4, column=0, sticky=W, padx=5)
        self.txtWorkPhone = Entry(ParentFrame, font=('arial', 12, 'bold'), text="Mobile", bd=5)
        self.txtWorkPhone.grid(row=4, column=1)

        self.lblMobile = Label(ParentFrame, font=('arial', 12, 'bold'), text='Mobile', bd=5)
        self.lblMobile.grid(row=5, column=0)
        self.txtMobile = Entry(ParentFrame, font=('arial', 12, 'bold'), textvariable=self.pgMobile, width=17)
        self.txtMobile.grid(row=5, column=1)

        self.lblEmail = Label(ParentFrame, font=('arial', 12, 'bold'), text='Email', bd=5)
        self.lblEmail.grid(row=6, column=0)
        self.txtEmail = Entry(ParentFrame, font=('arial', 12, 'bold'), textvariable=self.pgEmail, width=17)
        self.txtEmail.grid(row=6, column=1, pady=3)







if __name__ == "__main__":
    root = Tk()
    application = studentRecords(root)
    root.mainloop()