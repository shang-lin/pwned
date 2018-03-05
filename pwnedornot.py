#!/usr/bin/env python3

""" Checks if a password has been pwned using the haveibeenpwned.com API.
"""

import getpass
import hashlib
import requests

def get_matching_list(hash_prefix):
    """ Queries the haveibeenpwned password range API.
    :param: hash_prefix: First five letters of the SHA1 hash of the password to check.
    :return: Text list returned by the API.
    """
    r = requests.get('https://api.pwnedpasswords.com/range/{}'.format(hash_prefix))
    if r.status_code != 200:
        raise Exception('Status code {}'.format(r.status_code))
    return r.text


def find_match(hash):
    """ Looks for a password hash from haveibeenpwned.com 
    that matches thes provided hash.
    :param: hash: SHA1 hash
    :return: Tuple containing the matching hash and number of times
    it has been compromised.
    """

    print('Finding match for {}'.format(hash))
    matches = get_matching_list(hash[:5])
    compare_str = hash[5:].upper()
    for line in matches.split('\r\n'):
        (potential_match, count) = line.split(':')
        if potential_match == compare_str:
            return (potential_match, count)
    return ('', 0)

def main():
    password = getpass.getpass()
    hash = hashlib.sha1(password.encode('utf-8')).hexdigest()
    match = find_match(hash)
    if match == ('', 0):
        print('This password has not been compromised.')
    else:
        print('This password has been compromised {} times.'.format(match[1]))


if __name__ == "__main__":
    main()
