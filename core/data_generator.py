import asyncio
import hashlib

from random import getrandbits


def get_message() -> dict[str, str]:
    """
    :return: {"data": string, "control_sum": string}
    """
    data = get_random_bin_string()
    control_sum = get_hash(data)
    message = {
        "data": data,
        "control_sum": control_sum
    }
    return message


def get_random_bin_string() -> str:
    """
    :return: binary representation of a random 32-bit number
    """
    return bin(getrandbits(32))[2:]


def get_hash(data: str) -> str:
    """
    :return: hash sum of given string
    """
    h = hashlib.sha256()
    h.update(data.encode('utf-8'))
    return h.hexdigest()
