#String ends with? KATA
#My solution - terrible
#def solution(text, ending):
 #   l = len(ending)
  #  if ending == fw:
        #return True
    #else:
       # return False
# best soultion
#def solution(string, ending):
    #return string.endswith(ending)

#jaden kata
#best solution
# def to_jaden_case(string):
#     return " ".join(word.capitalize() for word in string.split())
# answer due to help of AI

#Tribonacci Sequence
# def tribonacci(signature, n):
#     if n == 1:
#         return [signature[0]]
#     elif n == 0:
#         return []
#     elif n == 2:
#         answer = signature[:2]
#         return answer
#     else:
#         for i in range(n):
#             if len(signature) < n:
#                 l = signature[i] + signature[i+1] + signature[i+2]
#                 signature.append(l)
#             else:
#                 return signature
# tribonacci([1, 1, 1], 2)


# def tribonacci(signature, n):
#     for i in range(n):
#         if len(signature) < n:
#             l = signature[i] + signature[i+1] + signature[i+2]
#             signature.append(l)
#         else:
#             return signature