def encrypt(message: str, shift: int) -> str:
	res = ""
	for i in range(shift):
		res += message[i::shift]
	return res

# TODO: Complete Part B and C
def decrypt(message: str, shift: int) -> str:
	return message
a = input("Enter message to encrypt: ")
shift = int(input("Enter shift: "))
print(encrypt(a, shift))
print(decrypt(encrypt(a,4),4))