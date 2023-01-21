from __future__ import annotations
import hashlib
from typing import Callable, Any


def main():
    hashtable = DynamicHashTable(11, 0.7, hash_function_generator)
    logged_in_username = None

    while True:
        inp = input()
        inp = inp.split()

        if inp[0] == 'REGISTER':
            [_, username, password] = inp
            assert logged_in_username is None

            if username in hashtable:
                print("Username Already Exist")
                continue
            hashtable[username] = password_hash_code(password)
            print("Register Successful")

        elif inp[0] == 'CHECK_USERNAME':
            [_, username] = inp
            if username in hashtable:
                print("Username Is Registered")
            else:
                print("Username Not Found")
            continue

        elif inp[0] == 'LOGIN':
            [_, username, password] = inp
            hashed_password = password_hash_code(password)

            assert logged_in_username is None
            if username not in hashtable:
                print("Username Not Found")
                continue

            actual_hashed_password = hashtable[username]
            if actual_hashed_password != hashed_password:
                print("Incorrect Password")
                continue

            logged_in_username = username
            print("Login Successful")

        elif inp[0] == 'EDIT_CURRENT':
            [_, edit_mode, new_value] = inp
            assert logged_in_username is not None

            if edit_mode == "USERNAME":
                new_username = new_value
                if new_username in hashtable:
                    print("Username already exist")
                    continue
                hashed_password = hashtable.remove(logged_in_username)
                logged_in_username = new_username
                hashtable[new_username] = hashed_password
                print("Your Account Has Been Updated")
            else:
                hashtable[logged_in_username] = password_hash_code(new_value)
                print("Your Account Has Been Updated")

        elif inp[0] == 'IS_AUTHENTICATED':
            if logged_in_username is not None:
                print(logged_in_username, hashtable[logged_in_username])
                continue
            print("Please Login")

        elif inp[0] == 'UNREGISTER':
            assert logged_in_username is None
            [_, username, password] = inp

            if username not in hashtable:
                print("Username Not Found")
                continue
            stored_hashed_password = hashtable[username]
            if stored_hashed_password != password_hash_code(password):
                print("Incorrect Password")
                continue
            hashtable.remove(username)
            print("Your Account Has Been Deleted")

        elif inp[0] == 'LOGOUT':
            if logged_in_username is None:
                print("You Have Not Been Logged In")
                continue
            logged_in_username = None
            print("You Have Been Logged Out")

        elif inp[0] == 'INSPECT':
            [_, row] = inp
            row = int(row)
            if hashtable._isRowEmpty(row):
                print("Row Is Empty")
                continue
            username, hashed_password = hashtable._getItem(row)
            print(username, hashed_password)
        elif inp[0] == 'COUNT_USERNAME':
            print(len(hashtable))
        elif inp[0] == 'CAPACITY':
            print(hashtable.get_capacity())
        elif inp[0] == 'EXIT':
            break


class PrimeGenerator:
    def __init__(self, initial_prev_prime):
        self.prev_prime = initial_prev_prime
        self.stored_prime_numbers = []

    def peek(self):
        if len(self.stored_prime_numbers) == 0:
            self.generate_next()
        return self.stored_prime_numbers[-1]

    def get_next(self):
        if len(self.stored_prime_numbers) == 0:
            self.generate_next()
        ret = self.stored_prime_numbers.pop()
        self.prev_prime = ret
        return ret

    def generate_next(self):
        start_from = self.prev_prime + 1
        up_to = 2 * self.prev_prime + self.prev_prime.bit_length()
        self.generate(start_from, up_to)

    def generate(self, start_from, up_to):
        primes = self._find_primes(start_from, up_to)  # reversed prime numbers
        self.stored_prime_numbers = list(reversed(tuple(primes)))

    def _find_primes(self, start_from, up_to):
        # sieve of eratosthenes
        arr = [True] * (up_to + 1)  # + 1 karena inklusif
        for i in range(2, len(arr)):
            if not arr[i]:
                continue
            curr = 2*i
            while curr <= up_to:
                arr[curr] = False
                curr = curr + i

        # nyari previous prime
        for i in range(start_from-1, 0, -1):
            if arr[i]:
                self.prev_prime = i
                break

        for i in range(start_from, up_to+1):
            if arr[i]:
                yield i


class DynamicHashTable:
    """
    A fixed-size hashtable data structure with double-hashing collision handling.
    """
    class _RemovedElement:
        pass

    primeGenerator = PrimeGenerator(1)

    class HashtableOverflow(Exception):
        def __init__(self, *args):
            super().__init__(*args)

    def __init__(self,
                 capacity: int,
                 load_factor: float,
                 hash_function_generator: Callable[
                     [DynamicHashTable],
                     tuple[
                         Callable[[Any], int],
                         Callable[[Any], int],
                     ]
                 ]):
        assert capacity >= 1
        self._hash_func_generator = hash_function_generator
        self._set_capacity_with_a_prime_number(capacity)
        self.hashtable = [[None, None] for i in range(self._capacity)]
        self._length = 0
        self._load_factor = load_factor

    def get_capacity(self):
        return self._capacity

    def _set_capacity_with_a_prime_number(self, capacity):
        # Bertrand's postulate. Untuk sembarang bilangan bulat n >= 1, pasti terdapat suatu bilangan prima p
        # sedemikian sehingga n <= p <= 2n. Karena kita ingin mencari bilangan prima p sehingga n <= p,
        # maka kita perlu mencari bilangan prima pertama yang berada pada range [n, 2n], untuk n = current capacity
        self.primeGenerator.generate(capacity, 2*capacity)

        primary_hash_func, secondary_hash_func = self._hash_func_generator(self)
        self._primaryHash = primary_hash_func
        self._secondaryHash = secondary_hash_func
        self._capacity = self.primeGenerator.get_next()

    def _getItem(self, index) -> tuple[Any, Any]:
        return self._getKey(index), self._getValue(index)

    def _getKey(self, index) -> Any:
        return self.hashtable[index][0]

    def _getValue(self, index) -> Any:
        return self.hashtable[index][1]

    def _setKey(self, index, new_key):
        self.hashtable[index][0] = new_key

    def _setValue(self, index, new_value):
        self.hashtable[index][1] = new_value

    def _isRowEmpty(self, index):
        key = self._getKey(index)
        return isinstance(key, self._RemovedElement) or key is None

    def _getIndex(self, key, onlyStopIfNone=True, raiseHashtableOverflow=True) -> int | None:
        primary_hash_value = self._primaryHash(key) % self._capacity
        secondary_hash_value = self._secondaryHash(key) % self._capacity

        # do until
        i = 0
        hash_value = (primary_hash_value + i*secondary_hash_value) % self._capacity
        while True:
            if self._getKey(hash_value) == key:
                break
            if self._getKey(hash_value) is None:
                break
            if not onlyStopIfNone:
                if isinstance(self._getKey(hash_value), self._RemovedElement):
                    break

            i += 1
            hash_value = (primary_hash_value + i*secondary_hash_value) % self._capacity

            if hash_value == primary_hash_value:
                if raiseHashtableOverflow:
                    raise self.HashtableOverflow("Hashtable overflow")
                return None
        return hash_value

    def put(self, key, value):
        if key not in self:
            self._length += 1
            self._check_if_expand_needed()
            index = self._getIndex(key, False)
        else:
            index = self._getIndex(key, True)

        self._setKey(index, key)
        self._setValue(index, value)

    def remove(self, key):
        index = self._getIndex(key)
        if self._isRowEmpty(index):
            raise KeyError
        self._length -= 1
        value = self._getValue(index)

        removed_element_dummy = self._RemovedElement()
        self._setKey(index, removed_element_dummy)
        return value

    def get(self, key):
        index = self._getIndex(key)
        if self._getKey(index) is None:
            raise KeyError
        ret = self._getValue(index)
        return ret

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __contains__(self, key):
        index = self._getIndex(key, True, False)
        if index is None:  # if not found
            return False
        return self._getKey(index) == key

    def __len__(self):
        return self._length

    def items(self):
        for i in range(len(self.hashtable)):
            if self._isRowEmpty(i):
                continue
            yield tuple(self.hashtable[i])

    def _check_if_expand_needed(self):
        if self._length / self._capacity < self._load_factor:
            return
        self._expand()

    def _expand(self):
        self.prev_capacity = self._capacity

        # meskipun new_capacity = current_capacity*2, di dalam constructor, constructor akan secara otomatis
        # mencari bilangan prima berikutnya yang lebih besar dari 2*current_capacity
        new_table = DynamicHashTable(self._capacity*2, self._load_factor, self._hash_func_generator)

        for (key, value) in self.items():
            new_table[key] = value
        self._capacity = new_table._capacity
        self.hashtable = new_table.hashtable
        self._primaryHash = new_table._primaryHash
        self._secondaryHash = new_table._secondaryHash

# Username hashcode
def string_to_int(string: str) -> int:
    sum_ = 0
    for char in string:
        sum_ += ord(char)
    return sum_


def password_hash_code(password: str, shift=6):
    hashed_pwd = hashlib.md5(password.encode())
    return hashed_pwd.hexdigest()

    # mask = 0x_FFFF_FFFF
    # hash = 0
    #
    # for char in password:
    #     assert hash >= 0
    #     hash = ((hash << shift) & mask) | (hash >> (32 - shift))
    #     hash += ord(char)
    # return hash


def hash_function_generator(dynamicHashTable: DynamicHashTable):
    def primary_hash(string: str):
        return string_to_int(string)

    # Misal capacity saat ini (setelah di-expand) adalah p (p merupakan prima).
    # Maka previous_prime_number akan berisi nilai bilangan prima terbesar yang kurang dari p
    previous_prime_number = dynamicHashTable.primeGenerator.prev_prime

    def secondary_hash(string: str):
        key = string_to_int(string)
        return 7 - (key % 7)

    return primary_hash, secondary_hash


"""
if __name__ == "__main__":
    main()

"""

if __name__ == "__main__":
    import sys, io
    oldOut = sys.stdout
    sys.stdout = io.StringIO()

    main()

    path = r"H:\01 Kuliah\01 Dokumen\00 - asisten dosen\10 SDA\01 ngoreksi TP\TP 04\tc\output"
    f = open(f"{path}\\output00.txt", "w")
    print(sys.stdout.getvalue(), file=f)

    sys.stdout = oldOut
    print("done")
#"""