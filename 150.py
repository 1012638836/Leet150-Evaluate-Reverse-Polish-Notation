class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = [];
        for i in range(0,len(tokens)):
            if tokens[i] != "+" and tokens[i] != "-" and tokens[i] != "*" and tokens[i] != "/":
                result.append(int(tokens[i]));
            else:
                op1 = result.pop();op2 = result.pop();
                if(tokens[i] == "+"):
                    result.append(op1 + op2);
                elif(tokens[i] == "-"):
                    result.append(op2 - op1);
                elif(tokens[i] == "*"):
                    result.append(op1 * op2);
                else:
                    if(op1*op2 < 0):
                        result.append(-((-op2)//op1));
                    else:
                        result.append(op2//op1);
        return result[0];