import re

class CalculatorException(Exception):
    pass

class Calculator(object):
    def read(self) :
        '''read input from stdin'''
        return input('> ')
    def helperEval(self,listOfTokens):
        partResult=[]
        xr=iter(range(0,len(listOfTokens)))
        for i in xr:
            if listOfTokens[i] == '*':
                loperand=int(partResult.pop())
                roperand=int(listOfTokens[i+1])
                partResult.append(str(loperand*roperand))
                next(xr)
            elif listOfTokens[i]=='/':
                loperand=int(partResult.pop())
                roperand=int(listOfTokens[i+1])
                partResult.append(str(loperand/roperand))
                next(xr)
            else:
                partResult.append(listOfTokens[i])
        listOfTokens=partResult
        xr=iter(range(0,len(listOfTokens)))
        partResult=[]
        for i in xr:
            if listOfTokens[i]=='+':
                loperand=int(partResult.pop())
                roperand=int(listOfTokens[i+1])
                partResult.append(str(loperand+roperand))
                next(xr)
            elif listOfTokens[i]=='-':
                loperand=int(partResult.pop())
                roperand=int(listOfTokens[i+1])
                partResult.append(str(loperand-roperand))
                next(xr)
            else:
                partResult.append(listOfTokens[i])
        return partResult[0]
    
    def eval(self, string) :
        '''evaluates an infix arithmetic expression '''
        #TODO implement me
        l = re.findall("[0-9]+|\+|\-|\*|\(|\)|\/|\n", string)
        lindexPara=[]
        lindexPara.append([])
        index=0
        insidePara=0
        for i in range(0,len(l)):
            if(l[i]=='('):
                insidePara=1
            elif(l[i]==')'):
                insidePara=0
                lindexPara[index]=self.helperEval(lindexPara[index])
                index+=1
                lindexPara.append([])
            else:
                if insidePara:
                    lindexPara[index].append(l[i])
                if not insidePara:
                    lindexPara[index]=(l[i])
                    index+=1
                    lindexPara.append([])
        lindexPara.pop()
        result=self.helperEval(lindexPara)
        if '.' in result:
            return float(result)
        else:
            return int(result)
        pass
    def loop(self) :
        """read a line of input, evaluate and print it
        repeat the above until the user types 'quit'. """
        line = self.read()
        while line!="quit":
            print(f"{self.eval(line)}")
            line=self.read()
        #TODO implement me
        pass

if __name__ == '__main__':
    calc = Calculator()
    calc.loop()