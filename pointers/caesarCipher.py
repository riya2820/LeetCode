def caesarCipher(s, k):
    # Write your code here
    #for i in range(97, 123):
    s1 = ""
    #for i in range(97, 123):
            
    for i in range(len(s)):
        if('A'<= s[i] <= 'Z'):
            s1 += chr((ord(s[i])+ k -ord('A'))%26 + ord('A'))
        elif('a'<=s[i]<='z'):
            s1 += chr((ord(s[i])+ k- ord('a'))%26+ ord('a'))
        else:
            s1+= s[i]
    return s1;
  
  
  if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
