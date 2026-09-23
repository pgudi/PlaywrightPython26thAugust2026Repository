from fixtures.conftest import setup_module

class TestUser:
    def test_create_user(self,setup_module):
        print("The User demoUser has created successfully!!")
    
    def test_modify_user(self,setup_module):
        print("The User demoUser has modified successfully!!")

    def test_delete_user(self,setup_module):
        print("The User demoUser has deleted successfully!!")


class TestEmployee:
    def test_create_employee(self,setup_module):
        print("The employee demoEmployee has created successfully!!")
        
    def test_modify_employee(self,setup_module):
        print("The employee demoEmployee has modified successfully!!")

    def test_delete_employee(self,setup_module):
        print("The employee demoEmployee has deleted successfully!!")