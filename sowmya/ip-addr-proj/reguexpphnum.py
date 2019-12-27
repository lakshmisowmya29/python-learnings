"""
1. Length 10 bytes
2. All numbers should not be same
3. Number should not start with 0 to 5
"""

#1. Length 10 bytes
def check_length(pnum):
	if(len(snum) != 10):
		return False
		
	return True

#2. All numbers should not be same
def is_all_numbers_same(pnum):

    for i in range (1,len(pnum)):
        if (pnum[0]==pnum[i]):
            return False            
	return True

#3. Number should not start with 0 to 5
def is_started_with_valid_degits(pnum):


	
	return True
	
def is_valid_phone_number(pnum):
	if (check_length(snum) == False):
		return False

	if (is_all_numbers_same(snum) == False):
		return False

	if (is_started_with_valid_degits(snum) == False):
		return False
		
	return True

def main():
	pnum = "9902096750"
    pnum = "0000000000"
	
	retval = is_valid_phone_number(pnum)
	if(retval == True):
		print (f"{pnum}: is valid")
	else:
		print (f"{pnum}: is valid")
	
if (_name_ == "_main_"):
	main()