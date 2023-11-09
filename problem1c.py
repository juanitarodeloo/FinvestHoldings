#rbac and abac hybrid - implemented by a capabilities list
#requires attributes, policy model, archirecture model
#policies are usually written in the perspective of the object that needs protecting, and the privileges
#available to subjects
from enum import Enum, auto

class Role(Enum):
    CLIENT = auto()
    PREMIUM_CLIENT = auto()
    FINANCIAL_PLANNER = auto()
    FINANCIAL_ADVISOR = auto()
    INVESTMENT_ANALYST = auto()
    TECHNICAL_SUPPORT = auto()
    TELLER = auto()
    COMPLIANCE_OFFICERS = auto()

class Resource(Enum):
    ACCOUNT_BALANCE = auto()
    INVESTMENT_PORTFOLIO = auto()
    FA_CONTACT_DETAILS = auto()
    IA_CONTACT_DETAILS = auto()
    MONEY_MARKET_INST = auto()
    PRIV_CONS_INST = auto()
    DERIVATIVES_INST = auto()
    CLIENT_ACCOUNT_ACCESS = auto()

class Permission(Enum):
    READ = auto()
    WRITE = auto()


    

capabilities_list = {
    Role.CLIENT: {
        Resource.ACCOUNT_BALANCE: [Permission.READ],
        Resource.INVESTMENT_PORTFOLIO: [Permission.READ],
        Resource.FA_CONTACT_DETAILS: [Permission.READ]
    }
} 

def can_access(role, resource, capability):
    if role in capabilities_list and resource in capabilities_list[role]:
        return capability in capabilities_list[role][resource]

    return False
#test
user1 = Role.CLIENT
print("Client can view of their account balance details: ", can_access(user1,Resource.ACCOUNT_BALANCE,Permission.READ))
print("Client can modify their account balance details: ", can_access(user1,Resource.ACCOUNT_BALANCE,Permission.WRITE))



