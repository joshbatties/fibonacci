class Fibonacci:
    def iterative(self, n):
        #Complexity: O(n), n is the input number
        if n == 0:
            return 0 
        elif n == 1 :
            return 1
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    
    def recursive(self, n):
        #Complexity: O(2^n), n is the input number
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.recursive(n - 1) + self.recursive(n - 2)


fib_instance = Fibonacci()
print(fib_instance.iterative(10))
print(fib_instance.recursive(10))