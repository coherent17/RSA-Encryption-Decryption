CC = python
OBJ = RSA_Encryption RSA_Decryption

Encryption_testcase1 = 3165580559 200003 RSA
Encryption_testcase2 = 2449500764025883 9800003 201812

Decryption_testcase1 = 221 5 89,99
Decryption_testcase2 = 12902023 4723267 2967605,9078654,5068419,5068419,406642,1905121,10620281,406642,9727012,5068419,10073213

all:$(OBJ)

RSA_Encryption:RSA_Encryption.py
	echo "$(Encryption_testcase1)" | $(CC) $<
	echo "$(Encryption_testcase2)" | $(CC) $<

RSA_Decryption:RSA_Decryption.py
	echo "$(Decryption_testcase1)" | $(CC) $<
	echo "$(Decryption_testcase2)" | $(CC) $<
