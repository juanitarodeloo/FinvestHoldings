from enum import Enum, auto

class Role(Enum):
    CLIENT = auto()
    PREMIUM_CLIENT = auto()
    FINANCIAL_PLANNER = auto()
    FINANCIAL_ADVISOR = auto()
    INVESTMENT_ANALYST = auto()
    TECHNICAL_SUPPORT = auto()
    TELLER = auto()
    COMPLIANCE_OFFICER = auto()
   

class Resource(Enum):
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
    READ = auto()
    WRITE = auto()
    ACCESS = auto()
    

capabilities_list = { #maps roles to resources and the capabilities they have with that resource
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


def can_access(role, resource, capability):
    if role in capabilities_list and resource in capabilities_list[role]:
        return capability in capabilities_list[role][resource]

    return False


#tests
user1 = Role.CLIENT
print("Client can view of their account balance details (Expected: True), Actual: ", 
      can_access(user1,Resource.ACCOUNT_BALANCE,Permission.READ))
print("Client can modify their account balance details: (Expected: False), Actual: ", 
      can_access(user1,Resource.ACCOUNT_BALANCE,Permission.WRITE), "\n")

user2 = Role.TELLER
print("Teller has access to a system during on hours (Expected: True), Actual: ", 
      can_access(user2, Resource.SYSTEM_ON_HOURS, Permission.ACCESS))
print("Teller has access to a system during off hours (Expected: False), Actual: ", 
      can_access(user2, Resource.SYSTEM_OFF_HOURS, Permission.ACCESS), "\n")

user3 = Role.PREMIUM_CLIENT
print("Premium Client can modify their investment portfolio (Expected: True), Actual: ", 
      can_access(user3,Resource.INVESTMENT_PORTFOLIO,Permission.WRITE))
print("Premium Client can view money market instruments: (Expected: False), Actual: ", 
      can_access(user1,Resource.MONEY_MARKET_INST,Permission.READ), "\n")

user4 = Role.FINANCIAL_PLANNER
print("Financial planner can view money market instruments (Expected: True), Actual: ", 
      can_access(user4,Resource.MONEY_MARKET_INST,Permission.WRITE))
print("Financial planner can request access to a client's account: (Expected: False), Actual: ", 
      can_access(user4,Resource.CLIENT_ACCOUNT_ACCESS,Permission.ACCESS), "\n")

user5 = Role.FINANCIAL_ADVISOR
print("Financial advisor can view private consumer instruments (Expected: True), Actual: ", 
      can_access(user5, Resource.PRIV_CONS_INST,Permission.READ))
print("Financial advisor can modify a private consumer instruments (Expected: False), Actual: ", 
      can_access(user5, Resource.PRIV_CONS_INST,Permission.WRITE), "\n")

user5 = Role.FINANCIAL_ADVISOR
print("Financial advisor can view private consumer instruments (Expected: True), Actual: ", 
      can_access(user5, Resource.PRIV_CONS_INST,Permission.READ))
print("Financial advisor can modify a private consumer instruments (Expected: False), Actual: ", 
      can_access(user5, Resource.PRIV_CONS_INST,Permission.WRITE), "\n")

user6 = Role.INVESTMENT_ANALYST
print("Investment analyst can view interest instruments (Expected: True), Actual: ", 
      can_access(user6, Resource.INTEREST_INST, Permission.READ))
print("Investment analyst can modify a money market instrument (Expected: False), Actual: ", 
      can_access(user6, Resource.MONEY_MARKET_INST,Permission.WRITE), "\n")

user7 = Role.TECHNICAL_SUPPORT
print("Technical support can request access to a client's account (Expected: True), Actual: ", 
      can_access(user7, Resource.CLIENT_ACCOUNT_ACCESS, Permission.ACCESS))
print("Technical support can modify a client's investment portfolio (Expected: False), Actual: ", 
      can_access(user7, Resource.INVESTMENT_PORTFOLIO,Permission.WRITE), "\n")

user8 = Role.COMPLIANCE_OFFICER
print("Compliance officers can validate modifications to investment portfolios (Expected: True), Actual: ", 
      can_access(user8, Resource.INVESTMENT_PORTFOLIO, Permission.READ))
print("Compliance officers can modify a client's investment portfolio (Expected: False), Actual: ", 
      can_access(user8, Resource.INVESTMENT_PORTFOLIO,Permission.WRITE), "\n")


