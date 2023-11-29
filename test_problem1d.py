import unittest
import sys
from io import StringIO

from problem1d import *

class TestAccessControl(unittest.TestCase):

    def setUp(self):
        self.access_control = AccessControl()

    def test_get_role_values(self):
        """Tests get_role_values()"""
        role_values = self.access_control.get_role_values()
        self.assertEqual(role_values, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_get_role_name(self):
        """Tests get_role_name() with different valid role numbers"""
        role_name = self.access_control.get_role_name(1)
        self.assertEqual(role_name, Role.CLIENT)

        role_name = self.access_control.get_role_name(2)
        self.assertEqual(role_name, Role.PREMIUM_CLIENT)

        role_name = self.access_control.get_role_name(7)
        self.assertEqual(role_name, Role.TELLER)

        role_name = self.access_control.get_role_name(99)
        self.assertIsNone(role_name)
        

    def test_print_role_capabilities(self): #TODO: should I test every role?
        """Tests print_role_capabilities()"""
        #redirect stdout to capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.access_control.print_role_capabilities(Role.CLIENT)

        #reset redirect.
        sys.stdout = sys.__stdout__

        expected_output = "Resource: ACCOUNT_BALANCE, Permissions: READ\n" \
                          "Resource: INVESTMENT_PORTFOLIO, Permissions: READ\n" \
                          "Resource: FA_CONTACT_DETAILS, Permissions: READ\n" \
                          "Resource: SYSTEM_OFF_HOURS, Permissions: ACCESS\n" \
                          "Resource: SYSTEM_ON_HOURS, Permissions: ACCESS\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_can_access(self):
        """Tests can_access() with true and false conditions for each role"""
        #true conditions
        result = self.access_control.can_access(Role.CLIENT, Resource.ACCOUNT_BALANCE, Permission.READ)
        self.assertTrue(result)

        result = self.access_control.can_access(Role.PREMIUM_CLIENT, Resource.INVESTMENT_PORTFOLIO,Permission.WRITE)
        self.assertTrue(result)
        
        result = self.access_control.can_access(Role.FINANCIAL_PLANNER, Resource.MONEY_MARKET_INST,Permission.READ)
        self.assertTrue(result)

        result = self.access_control.can_access(Role.FINANCIAL_ADVISOR, Resource.PRIV_CONS_INST,Permission.READ)
        self.assertTrue(result)

        result = self.access_control.can_access(Role.INVESTMENT_ANALYST, Resource.INTEREST_INST, Permission.READ)
        self.assertTrue(result)

        result = self.access_control.can_access(Role.TECHNICAL_SUPPORT, Resource.CLIENT_ACCOUNT_ACCESS, Permission.ACCESS)
        self.assertTrue(result)

        result = self.access_control.can_access(Role.TELLER, Resource.SYSTEM_ON_HOURS, Permission.ACCESS)
        self.assertTrue(result)

        result = self.access_control.can_access(Role.COMPLIANCE_OFFICER, Resource.INVESTMENT_PORTFOLIO, Permission.READ)
        self.assertTrue(result)

        #false conditions:
        result = self.access_control.can_access(Role.CLIENT, Resource.ACCOUNT_BALANCE, Permission.WRITE)
        self.assertFalse(result)

        result = self.access_control.can_access(Role.PREMIUM_CLIENT, Resource.MONEY_MARKET_INST, Permission.READ)
        self.assertFalse(result)
        
        result = self.access_control.can_access(Role.FINANCIAL_PLANNER, Resource.CLIENT_ACCOUNT_ACCESS,Permission.ACCESS)
        self.assertFalse(result)

        result = self.access_control.can_access(Role.FINANCIAL_ADVISOR, Resource.PRIV_CONS_INST, Permission.WRITE)
        self.assertFalse(result)

        result = self.access_control.can_access(Role.INVESTMENT_ANALYST, Resource.MONEY_MARKET_INST,Permission.WRITE)
        self.assertFalse(result)

        result = self.access_control.can_access(Role.TECHNICAL_SUPPORT, Resource.INVESTMENT_PORTFOLIO,Permission.WRITE)
        self.assertFalse(result)

        result = self.access_control.can_access(Role.TELLER, Resource.SYSTEM_OFF_HOURS, Permission.ACCESS)
        self.assertFalse(result)
        
        result = self.access_control.can_access(Role.COMPLIANCE_OFFICER, Resource.INVESTMENT_PORTFOLIO,Permission.WRITE)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()