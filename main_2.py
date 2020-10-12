import hashlib


def get_country_hash(file):
    with open(file, 'rb') as f:
        for line in f:
            hash_line = hashlib.md5(line)
            hash_country_link = hash_line.hexdigest()
            yield hash_country_link


file_for_hash = 'files\links.txt'

if __name__ == '__main__':
    for current_hash in get_country_hash(file_for_hash):
        print(current_hash)
