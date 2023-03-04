import re

email_regex = re.compile(r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9,-]+\.[a-zA-Z]{2,})')


def validate_email(text):
    matches = email_regex.search(text)
    if matches is None:
        is_valid_email, local_part, domain_part = False, None, None
    else:
        is_valid_email, local_part, domain_part = True, matches.group(1), matches.group(2)
    return is_valid_email, local_part, domain_part


def censor(regex, text):
    return regex.sub('****', text)


if __name__ == '__main__':
    addresses = [
        'anonymous@gmail.com',
        'thanos.alev@gmail.com',
        'thanos.alev@outlook.com',
        'name.surname',
        '@gmail.com',
        'me.com'
    ]

# Check for address validity and extract mail domains
for addr in addresses:
    msg = 'Address {} '.format(addr)
    is_valid, _, domain = validate_email(addr)
    if is_valid:
        print('Address {} is valid and pertains to domain {}'.format(addr, domain))
    else:
        print('Address {} is not valid'.format(addr))


# censor thanos.alev
censored_addresses = []
censorship_regex = re.compile(r'(thanos\.alev)')
for addr in addresses:
    censored_addresses.append(censor(censorship_regex, addr))
print('Censored list: {}'.format(censored_addresses))


