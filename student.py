class student:
    def __init__(self, first_name=0, last_name=0, SID=0, NID=0, Gender=0):
        self.fname = first_name
        self.lname = last_name
        self.sid = SID
        self.nid = NID
        self.mof = Gender

    def __iter__(self):
        return self

    def getgender(self):
        return self.mof

    def getSID(self):
        return self.sid

    def getNID(self):
        return self.nid

    def fullname(self):
        return (self.fname + ' ' + self.lname)

    def entrance_year(self):
        return int ( self.sid / 10000000 )

    def input_info(self):
        self.fname = input ( "Enter First name : " )
        self.lname = input ( "Enter Last name : " )
        self.sid = input ( "Enter SID : " )
        self.nid = input ( "Enter NID : " )
        self.mof = input ( "Enter Gender (male/female) : " )


def show(stu):
    stu = student ( stu )
    print ( "Name : ", stu.fullname ( ) )
    print ( "Student ID Number : ", stu.getSID ( ) )
    print ( "National ID Number : ", stu.getNID ( ) )
    print ( "Student Gender : ", stu.getgender ( ) )

f = 0
x = (int ( input (
        "HI\nWellcome to student app\nPlease Choose from below:\n1.input information for a student\n2.show all students\n3.Exit\n" ) ))
stus = list ( student ( ) )
stus.append ( student ( ) )
f += 1
stus[ f ].input_info ( )
show ( stus[ f ] )
print ( stus )
