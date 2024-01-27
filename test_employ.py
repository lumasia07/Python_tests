import unittest
from employ import Employee

class TestEmploy(unittest.TestCase):

    def test_email(self):

        print('Set_up\n')
        emp_1 = Employee('Lumasia', 'Stan', 44569)
        emp_2 = Employee('Emma', 'Hayes', 77988)

        self.assertEqual(emp_1.email, 'Lumasia.Stan@email.com')
        self.assertEqual(emp_2.email, 'Emma.Hayes@email.com')

        emp_1.first = 'Vini'
        emp_2.first = 'Inno'

        self.assertEqual(emp_1.email, 'Vini.Stan@email.com')
        self.assertEqual(emp_2.email, 'Inno.Hayes@email.com')

    def test_fullname(self):

        print('test_fullname\n')
        emp_1 = Employee('Lumasia', 'Stan', 44569)
        emp_2 = Employee('Emma', 'Hayes', 77988)
        
        self.assertEqual(emp_1.fullname, "Lumasia Stan")
        self.assertEqual(emp_2.fullname, "Emma Hayes")

        emp_1.first = 'Vini'
        emp_2.first = 'Inno'

        self.assertEqual(emp_1.fullname, "Vini Stan")
        self.assertEqual(emp_2.fullname, "Inno Hayes")

    def test_apply_raise(self):

        print('test raise\n')
        emp_1 = Employee('Lumasia', 'Stan', 44569)
        emp_2 = Employee('Emma', 'Hayes', 77988)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 2228.0)
        self.assertEqual(emp_2.pay, 3899.0)



if __name__ == "__main__":
    unittest.main()


