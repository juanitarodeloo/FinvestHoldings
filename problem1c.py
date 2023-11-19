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
    SYSTEM_OFF_HOURS = auto() #everyone should have this resource exept tellers
    SYSTEM_ON_HOURS = auto() #everyone should have access to this

class Permission(Enum):
    """Permissions define permissions to resources in Finvest Holdings"""
    READ = auto()
    WRITE = auto()
    ACCESS = auto()
    

class AccessControl:
    """AccessControl holds the capabilities list and functions that grab information from it"""

    def __init__(self):
        self.capabilities_list = { #maps roles to resources and the capabilities they have with that resource
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
                Resource.ACCOUNT_BALANCE: [Permission.READ], #assuming client information includes these two resources
                Resource.INVESTMENT_PORTFOLIO: [Permission.READ],
                Resource.CLIENT_ACCOUNT_ACCESS: [Permission.ACCESS],
                Resource.SYSTEM_OFF_HOURS: [Permission.ACCESS],
                Resource.SYSTEM_ON_HOURS: [Permission.ACCESS]
            },
            Role.TELLER: {
                Resource.SYSTEM_ON_HOURS: [Permission.ACCESS]
            },
            Role.COMPLIANCE_OFFICER: {
                Resource.INVESTMENT_PORTFOLIO: [Permission.READ], #I think this is what validate mods to this means
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


# #tests
# user1 = Role.CLIENT
# print("Client can view of their account balance details (Expected: True), Actual: ", 
#       can_access(user1,Resource.ACCOUNT_BALANCE,Permission.READ))
# print("Client can modify their account balance details: (Expected: False), Actual: ", 
#       can_access(user1,Resource.ACCOUNT_BALANCE,Permission.WRITE), "\n")

# user2 = Role.TELLER
# print("Teller has access to a system during on hours (Expected: True), Actual: ", 
#       can_access(user2, Resource.SYSTEM_ON_HOURS, Permission.ACCESS))
# print("Teller has access to a system during off hours (Expected: False), Actual: ", 
#       can_access(user2, Resource.SYSTEM_OFF_HOURS, Permission.ACCESS), "\n")

# user3 = Role.PREMIUM_CLIENT
# print("Premium Client can modify their investment portfolio (Expected: True), Actual: ", 
#       can_access(user3,Resource.INVESTMENT_PORTFOLIO,Permission.WRITE))
# print("Premium Client can view money market instruments: (Expected: False), Actual: ", 
#       can_access(user1,Resource.MONEY_MARKET_INST,Permission.READ), "\n")

# user4 = Role.FINANCIAL_PLANNER
# print("Financial planner can view money market instruments (Expected: True), Actual: ", 
#       can_access(user4,Resource.MONEY_MARKET_INST,Permission.WRITE))
# print("Financial planner can request access to a client's account: (Expected: False), Actual: ", 
#       can_access(user4,Resource.CLIENT_ACCOUNT_ACCESS,Permission.ACCESS), "\n")

# user5 = Role.FINANCIAL_ADVISOR
# print("Financial advisor can view private consumer instruments (Expected: True), Actual: ", 
#       can_access(user5, Resource.PRIV_CONS_INST,Permission.READ))
# print("Financial advisor can modify a private consumer instruments (Expected: False), Actual: ", 
#       can_access(user5, Resource.PRIV_CONS_INST,Permission.WRITE), "\n")

# user5 = Role.FINANCIAL_ADVISOR
# print("Financial advisor can view private consumer instruments (Expected: True), Actual: ", 
#       can_access(user5, Resource.PRIV_CONS_INST,Permission.READ))
# print("Financial advisor can modify a private consumer instruments (Expected: False), Actual: ", 
#       can_access(user5, Resource.PRIV_CONS_INST,Permission.WRITE), "\n")

# user6 = Role.INVESTMENT_ANALYST
# print("Investment analyst can view interest instruments (Expected: True), Actual: ", 
#       can_access(user6, Resource.INTEREST_INST, Permission.READ))
# print("Investment analyst can modify a money market instrument (Expected: False), Actual: ", 
#       can_access(user6, Resource.MONEY_MARKET_INST,Permission.WRITE), "\n")

# user7 = Role.TECHNICAL_SUPPORT
# print("Technical support can request access to a client's account (Expected: True), Actual: ", 
#       can_access(user7, Resource.CLIENT_ACCOUNT_ACCESS, Permission.ACCESS))
# print("Technical support can modify a client's investment portfolio (Expected: False), Actual: ", 
#       can_access(user7, Resource.INVESTMENT_PORTFOLIO,Permission.WRITE), "\n")

# user8 = Role.COMPLIANCE_OFFICER
# print("Compliance officers can validate modifications to investment portfolios (Expected: True), Actual: ", 
#       can_access(user8, Resource.INVESTMENT_PORTFOLIO, Permission.READ))
# print("Compliance officers can modify a client's investment portfolio (Expected: False), Actual: ", 
#       can_access(user8, Resource.INVESTMENT_PORTFOLIO,Permission.WRITE), "\n")


