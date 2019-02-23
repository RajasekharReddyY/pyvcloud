# Resource elements names and order

# CustomOrgLdapSettings
LDAP_CUSTOM_SETTINGS = [
    'HostName',
    'Port',
    'IsSsl',
    'IsSslAcceptAll',
    'SearchBase',
    'UserName',
    'AuthenticationMechanism',
    'IsGroupSearchBaseEnabled',
    'ConnectorType',
    {'UserAttributes':[
        'ObjectClass',
        'ObjectIdentifier',
        'UserName',
        'Email',
        'FullName',
        'GivenName',
        'Surname',
        'Telephone',
        'GroupMembershipIdentifier',
        'GroupBackLinkIdentifier'
    ]},
    {'GroupAttributes':[
        'ObjectClass',
        'ObjectIdentifier',
        'GroupName',
        'Membership',
        'MembershipIdentifier',
        'BackLinkIdentifier'
    ]},
    'UseExternalKerberos'
]

# OrgLdapSettings
ORG_LDAP_SETTINGS = [
    'OrgLdapMode',
    {'CustomOrgLdapSettings': LDAP_CUSTOM_SETTINGS }
]