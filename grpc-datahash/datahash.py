from hashlib import md5, sha256


def hash_md5(data):
    result = md5(data.encode()).hexdigest()
    return result


def hash_sha256(data):
    result = sha256(data.encode()).hexdigest()
    return result
