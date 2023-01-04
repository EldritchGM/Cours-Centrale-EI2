from Employee import Employee

class Teacher(Employee):
    """
    A class used to represent an Teacher that inherit from Employee
    Attributes
    ----------
    first : str
        the first name of the employee
    last : str
        the last name of the employee
    holiday_left : int
        the number of holiday left in days
    email : srt
        the email generated from first and last name
    teaching_hours : int
        the number of teaching hours

    Methods
    -------
    get_teaching_hours()
        Prints the number of teaching hours
    """
    def __init__(self, first, last, left, teaching_hours):
        super().__init__(first, last, left)
        assert teaching_hours > 0
        teaching_hours = teaching_hours
        
    
    def set_teaching_hours(self, new_value):
        if new_value < 0 :
            raise ValueError('teaching hours must be positive')
        teaching_hours = new_value
        
    def __str__(self):
        return '{0}, teaching hours : {1.teaching_hours}'.format(super().__str__(), self)