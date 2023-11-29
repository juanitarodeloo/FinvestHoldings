from enum import Enum, auto

class Role(Enum):
    """Role defines all roles (employees and clients) in Finvest Holding"""
    CLIENT = 1
    PREMIUM_CLIENT = 2
    FINANCIAL_PLANNER = 3
    FINANCIAL_ADVISOR = 4
    INVESTMENT_ANALYST = 5
    TECHNICAL_SUPPORT = 6
    TELLER = 7
    COMPLIANCE_OFFICER = 8

class Resource(Enum):
    """Resources defines all resources that have access rights in Finvest Holdings"""
    ACCOUNT_BALANCE = auto()
    INVESTMENT_PORTFOLIO = auto()
    FA_CONTACT_DETAILS = auto()
    IA_CONTACT_DETAILS = auto()
    MONEY_MARKET_INST = auto()
    PRIV_CONS_INST = auto()
    DERIVATIVES_TRADING = auto()
    INTEREST_INST = auto()
    CLIENT_ACCOUNT_ACCESS = auto()
    SYSTEM_OFF_HOURS = auto()
    SYSTEM_ON_HOURS = auto()

class Permission(Enum):
    """Permissions define permissions to resources in Finvest Holdings"""
    READ = auto()
    WRITE = auto()
    ACCESS = auto()
    

class AccessControl:
    """AccessControl holds the capabilities list and functions that grab information from it"""

    def __init__(self):
        self.capabilities_list = {
            Role.CLIENT: {
                Resource.ACCOUNT_BALANCE: [Permission.READ],
                Resource.INVESTMENT_PORTFOLIO: [Permission.READ],
                Resource.FA_CONTACT_DETAILS: [Permission.READ],
                Resource.SYSTEM_OFF_HOURS: [Permission.ACCESS],
                Resource.SYSTEM_ON_HOURS: [Permission.ACCESS]
            },
            Role.PREMIUM_CLIENT: {
                Resource.ACCOUNT_BALANCE: [Permission.READ],
                Resource.INVESTMENT_PORTFOLIO: [Permission.READ, Permission.WRITE],
                Resource.FA_CONTACT_DETAILS: [Permission.READ],
                Resource.IA_CONTACT_DETAILS: [Permission.READ],
                Resource.SYSTEM_OFF_HOURS: [Permission.ACCESS],
                Resource.SYSTEM_ON_HOURS: [Permission.ACCESS]
            },
            Role.FINANCIAL_PLANNER: {
                Resource.ACCOUNT_BALANCE: [Permission.READ],
                Resource.INVESTMENT_PORTFOLIO: [Permission.READ, Permission.WRITE],
                Resource.MONEY_MARKET_INST: [Permission.READ],
                Resource.PRIV_CONS_INST: [Permission.READ],
                Resource.SYSTEM_OFF_HOURS: [Permission.ACCESS],
                Resource.SYSTEM_ON_HOURS: [Permission.ACCESS]
            },
            Role.FINANCIAL_ADVISOR: {
                Resource.ACCOUNT_BALANCE: [Permission.READ],
                Resource.INVESTMENT_PORTFOLIO: [Permission.READ, Permission.WRITE],
                Resource.PRIV_CONS_INST: [Permission.READ],
                Resource.SYSTEM_OFF_HOURS: [Permission.ACCESS],
                Resource.SYSTEM_ON_HOURS: [Permission.ACCESS]
            },
            Role.INVESTMENT_ANALYST: {
                Resource.ACCOUNT_BALANCE: [Permission.READ],
                Resource.INVESTMENT_PORTFOLIO: [Permission.READ, Permission.WRITE],
                Resource.MONEY_MARKET_INST: [Permission.READ],
                Resource.DERIVATIVES_TRADING: [Permission.READ],
                Resource.INTEREST_INST: [Permission.READ],
                Resource.PRIV_CONS_INST: [Permission.READ],
                Resource.SYSTEM_OFF_HOURS: [Permission.ACCESS],
                Resource.SYSTEM_ON_HOURS: [Permission.ACCESS]
            },
            Role.TECHNICAL_SUPPORT:{
                Resource.ACCOUNT_BALANCE: [Permission.READ],
                Resource.INVESTMENT_PORTFOLIO: [Permission.READ],
                Resource.CLIENT_ACCOUNT_ACCESS: [Permission.ACCESS],
                Resource.SYSTEM_OFF_HOURS: [Permission.ACCESS],
                Resource.SYSTEM_ON_HOURS: [Permission.ACCESS]
            },
            Role.TELLER: {
                Resource.SYSTEM_ON_HOURS: [Permission.ACCESS]
            },
            Role.COMPLIANCE_OFFICER: {
                Resource.INVESTMENT_PORTFOLIO: [Permission.READ],
                Resource.SYSTEM_OFF_HOURS: [Permission.ACCESS]
            }

        } 

    def get_role_values(self):
        """Returns the values associated with the roles [1, 2, 3, 4, 5, 6, 7, 8]"""
        return [role.value for role in Role]

    def get_role_name(self, role_number):
        """Returns the item name associated with the given role number """
        for role in Role:
            if role.value == role_number:
                return role
        return None

    def print_role_capabilities(self, role):
        """Prints the capabilities that the given role has on all resources."""
        if role in self.capabilities_list:
            role_capabilities = self.capabilities_list[role]
            for resource, permissions in role_capabilities.items():
                permission_names = [permission.name for permission in permissions]
                print(f"Resource: {resource.name}, Permissions: {', '.join(permission_names)}")


    def can_access(self, role, resource, capability):
        """Returns true if the given role has the given capability on the given resource. Returns False otherwise."""
        if role in self.capabilities_list and resource in self.capabilities_list[role]:
            return capability in self.capabilities_list[role][resource]

        return False
    