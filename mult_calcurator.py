
class Calcurator:
    def cal(self, num1, op, num2):
        match op:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "/":
                result = num1 / num2
            case "*":
                result = num1 * num2
            case "%":
                result = num1 % num2
            case "//":
                result = num1 // num2
            case _:
                result = "잘못된 연산자"
        print(result)
        

input1 = Calcurator()
input1.cal(1, "+", 3)