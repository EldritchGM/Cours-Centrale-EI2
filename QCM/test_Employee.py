import pytest, Employee

class TestEmployee:

    def test_init1(self, employee1):
        assert employee1.first == "Romain"
        assert employee1.last == "LUCAS"
        assert employee1.holiday_left == 36
        assert employee1.email == "Romain.LUCAS@ec-nantes.fr"
    
    def test_fullname1(self, employee1):
        assert employee1.fullname() == "Romain LUCAS"
    
    def test_newHoliday1(self, employee1):
        employee1.newHoliday(24)
        assert employee1.holiday_left == 60

    def test_str1(self, employee1):
        assert str(employee1) == "Romain LUCAS Romain.LUCAS@ec-nantes.fr, jours restants : 36"

    @pytest.mark.xfail
    def test_init2(self, employee2):
        assert employee2.first == "Romain"
        assert employee2.last == "LUCAS"
        assert employee2.holiday_left == 36
        assert employee2.email == "Romain.LUCAS@ec-nantes.fr"
    
    @pytest.mark.xfail
    def test_fullname2(self, employee2):
        assert employee2.fullname() == "Romain LUCAS"
    
    @pytest.mark.xfail
    def test_newHoliday2(self, employee2):
        employee2.newHoliday(24)
        assert employee2.holiday_left == 60

    @pytest.mark.xfail
    def test_str2(self, employee2):
        assert str(employee2) == "Romain LUCAS Romain.LUCAS@ec-nantes.fr, jours restants : 36"

    @pytest.mark.xfail
    def test_init3(self, employee3):
        assert employee3.first == "Romain"
        assert employee3.last == "LUCAS"
        assert employee3.holiday_left == 36
        assert employee3.email == "Romain.LUCAS@ec-nantes.fr"
    
    @pytest.mark.xfail
    def test_fullname3(self, employee3):
        assert employee3.fullname() == "Romain LUCAS"
    
    @pytest.mark.xfail
    def test_newHoliday3(self, employee3):
        employee3.newHoliday(24)
        assert employee3.holiday_left == 60

    @pytest.mark.xfail
    def test_str(self, employee3):
        assert str(employee3) == "Romain LUCAS Romain.LUCAS@ec-nantes.fr, jours restants : 36"

@pytest.fixture()
def employee1():
    return Employee.Employee("Romain", "LUCAS", 36)

@pytest.fixture()
def employee2():
    return Employee.Employee("Romain", "LUCAS", "36")

@pytest.fixture()
def employee3():
    return Employee.Employee(24, 7, 2001)