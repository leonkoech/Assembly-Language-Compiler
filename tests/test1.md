# Tests

Below are some of the tests cases I did for the compiler.

Jump to:
1. [Java](#java)
2. [c](#c)


## java

### Test case one

```
public static void main(String[] args) {

    System.out.println("Sum of these numbers: "+sum);
}
```

### Test case two

```
public class AddTwoNumbers {

   public static void main(String[] args) {
        
      int num1 = 5;
      int num2 = 15;
      int sum = num1 + num2;

      System.out.println("Sum of these numbers: "+sum);
   }
}
```

### Test case three

```
package jcompiler;
import java.util.Scanner;
public class javac{
 public static void main(String[] args)
 {
 @SuppressWarnings("resource")
Scanner console = new Scanner(System.in);

 int number;
 char choice;
 int evenSum = 0;
 int oddSum = 0;

 do
 {
 System.out.print("Enter the number ");
 number = console.nextInt();

 /* determines an interger if it is even by dividing it by */
 /* two and find if it has no remainder thus even */
 if( number % 2 == 0)
 {
     evenSum += number;
 }
 /* check if the integer is not even then its odd(has a remainder) */
 else
 {
 oddSum += number;
 }

 System.out.print("Do you want to continue y/n? ");
 choice = console.next().charAt(0);

 /* prompts the user to choose where to enter another integer */
 }while(choice=='y' || choice == 'Y');

 System.out.println("Sum of even numbers: " + evenSum);
 System.out.println("Sum of odd numbers: " + oddSum);
 }
}
```
### Test case four

```
public class IfExample {  
public static void main(String[] args) {  
    /* defining an 'age' variable  */
    int age=20;  
    /* checking the age */  
    if(age>18){  
        System.out.print("Age is greater than 18");  
    }  
}  
}  
```

### Test case five

```
class PalindromeExample{  
 public static void main(String args[]){  
  int r,sum=0,temp;    
  int n=454;
  /* It is the number variable to be checked for palindrome */ 
  
  temp=n;    
  while(n>0){    
   r=n%10;  /* getting remainder  */
   sum=(sum*10)+r;    
   n=n/10;    
  }    
  if(temp==sum)    
   System.out.println("palindrome number ");    
  else    
   System.out.println("not palindrome");    
}  
}  
```

### Test case six

```
class FibonacciExample1{  
public static void main(String args[])  
{    
 int n1=0,n2=1,n3,i,count=10;    
 System.out.println(n1+'-'+n2);/*printing 0 and 1    */
    
 for(i=2;i<count;++i)/* loop starts from 2 because 0 and 1 are already printed    */
 {    
  n3=n1+n2;    
  System.out.println("-"+n3);    
  n1=n2;    
  n2=n3;    
 }    
  
}}
```

### Test case seven

```
class Bike{  
  void run(){System.out.println("running");}  
}  
class Splendor extends Bike{  
  void run(){System.out.println("running safely with 60km");}  
  public static void main(String args[]){  
    Bike b = new Splendor();/* upcasting */  
    b.run();  
  }  
}  
```
### Test case eight

```
class Dog{  
 private void eat(){System.out.println("dog is eating...");}  
  
 public static void main(String args[]){  
  Dog d1=new Dog();  
  d1.eat();  
 }  
}  
```

### Test case nine

```
class Animal{  
 void eat(){System.out.println("animal is eating...");}  
}  
  
class Dog extends Animal{  
 void eat(){System.out.println("dog is eating...");}  
  
 public static void main(String args[]){  
  Animal a=new Dog();  
  a.eat();  
 }  
} 
```

### Test case ten

```
class Simple1{  
 public static void main(String args[]){  
 Simple1 s=new Simple1();  
 System.out.println(s instanceof Simple1);/* true  */
 }  
}  
```
### Test case eleven

```
abstract class Bike{  
  abstract void run();  
}  
class Honda4 extends Bike{  
void run(){System.out.println("running safely");}  
public static void main(String args[]){  
 Bike obj = new Honda4();  
 obj.run();  
}  
}
```

### Test case twelve

```
abstract class Calculate  
{  
    abstract int multiply(int a, int b);  
}  
   
public class Main  
{  
    public static void main(String[] args)  
    {  
        int result = new Calculate()  
        {      
            @Override  
            int multiply(int a, int b)  
            {  
                return a*b;  
            }  
        }.multiply(12,32);  
        System.out.println("result = "+result);  
    }  
} 
```
 
### Test case thirteen

```
class TestExceptionPropagation1{  
  void m(){  
    int data=50/0;  
  }
  void n(){  
    m();  
  }  
  void p(){  
   try{  
    n();  
   }catch(Exception e){System.out.println("exception handled");}  
  }  
  public static void main(String args[]){  
   TestExceptionPropagation1 obj=new TestExceptionPropagation1();  
   obj.p();  
   System.out.println("normal flow...");  
  }  
}
```
### Test case fourteen

```
public class DeprecatedTest 
    { 
        @Deprecated
        public void Display() 
        { 
            System.out.println("Deprecatedtest display()"); 
        } 
    
        public static void main(String args[]) 
        { 
            DeprecatedTest d1 = new DeprecatedTest(); 
            d1.Display(); 
        } 
    } 
```

### Test case fifteen

```
class Base 
{ 
     public void Display() 
     { 
         System.out.println("Base display()"); 
     } 
       
     public static void main(String args[]) 
     { 
         Base t1 = new Derived(); 
         t1.Display(); 
     }      
} 
class Derived extends Base 
{ 
     @Override
     public void Display() 
     { 
         System.out.println("Derived display()"); 
     } 
} 
```

### Test case sixteen

```
package source; 
/* A Java program to demonstrate user defined annotations */
import java.lang.annotation.Documented; 
import java.lang.annotation.Retention; 
import java.lang.annotation.RetentionPolicy; 
  
/* user-defined annotation */
@Documented
@Retention(RetentionPolicy.RUNTIME) 
@ interface TestAnnotation 
{ 
    String Developer() default "Rahul";  
    String Expirydate(); 
} /* will be retained at runtime */
  
/* Driver class that uses @TestAnnotation */
public class Test 
{ 
    @TestAnnotation(Developer="keons", Expirydate="04-27-2020") 
    void fun1() 
    { 
        System.out.println("Test method 1"); 
    } 
  
    @TestAnnotation(Developer="koech", Expirydate="05-05-2021") 
    void fun2() 
    { 
        System.out.println("Test method 2"); 
    } 
      
    public static void main(String args[]) 
    { 
        System.out.println("Hello"); 
    } 
} 
```


## c

### Test case one

```
/*
  Hello world
 */
print("Hello, World!\n");
```
### Test case two

```
#include<stdio.h>    
int main()    
{    
 int n1=0,n2=1,n3,i,number;    
 printf("Enter the number of elements:");    
 scanf("%d",&number);    
 printf("\n%d %d",n1,n2);/* printing 0 and 1    */
 for(i=2;i<number;++i)/* loop starts from 2 because 0 and 1 are already printed   */ 
 {    
  n3=n1+n2;    
  printf(" %d",n3);    
  n1=n2;    
  n2=n3;    
 }  
  return 0;  
 }  
 ```

### Test case three

```
int n,r,sum=0,temp;    
printf("enter the number=");    
scanf("%d",&n);    
temp=n;    
while(n>0)    
{    
r=n%10;    
sum=(sum*10)+r;    
n=n/10;    
}    
if(temp==sum){   
printf("palindrome number ");    
else    
printf("not palindrome");   
return 0;  
}  
```
### Test case four

* negative test *

```
/*
  All lexical tokens - not syntactically correct, but that will
  have to wait until syntax analysis
 */
/* Print   */  print    /* Sub     */  -
/* Putc    */  putc     /* Lss     */  <
/* If      */  if       /* Gtr     */  >
/* Else    */  else     /* Leq     */  <=
/* While   */  while    /* Geq     */  >=
/* Lbrace  */  {        /* Eq      */  ==
/* Rbrace  */  }        /* Neq     */  !=
/* Lparen  */  (        /* And     */  &&
/* Rparen  */  )        /* Or      */  ||
/* Uminus  */  -        /* Semi    */  ;
/* Not     */  !        /* Comma   */  ,
/* Mul     */  *        /* Assign  */  =
/* Div     */  /        /* Integer */  42
/* Mod     */  %        /* String  */  "String literal"
/* Add     */  +        /* Ident   */  variable_name
/* character literal */  '\n'
/* character literal */  '\\'
/* character literal */  ' '
```

### Test case five

```
/*** test printing, embedded \n and comments with lots of '*' ***/
print(42);
print("\nHello World\nGood Bye\nok\n");
print("Print a slash n - \\n.\n");
```

### Test case six

```
count = 1;
while (count < 10) {
    print("count is: ", count, "\n");
    count = count + 1;
}
```

### Test case seven

```
/* 100 Doors */
i = 1;
while (i * i <= 100) {
    print("door ", i * i, " is open\n");
    i = i + 1;
}
```

### Test case eight

```
a = (-1 * ((1 * (5 * 15)) / 10));
printf(a, "\n");
b = -a;
printf(b, "\n");
printf(-b, "\n");
printf(-(1), "\n");
```

### Test case nine

```
#include<stdio.h>  
int main(){    
int n,i,m=0,flag=0;    
printf("Enter the number to check prime:");    
scanf("%d",&n);    
m=n/2;    
for(i=2;i<=m;i++)    
{    
if(n%i==0)    
{    
printf("Number is not prime");    
flag=1;    
break;    
}    
}    
if(flag==0)    
printf("Number is prime");     
return 0;  
 }   
```

### Test case ten 

```
/* Compute the gcd of 1071, 1029:  21 */
 
a = 1071;
b = 1029;
 
while (b != 0) {
    new_a = b;
    b     = a % b;
    a     = new_a;
}
print(a);
```

### Test case eleven

```
/* 12 factorial is 479001600 */
 
n = 12;
result = 1;
i = 1;
while (i <= n) {
    result = result * i;
    i = i + 1;
}
print(result);
```

### Test case twelve

```
/* fibonacci of 44 is 701408733 */
 
n = 44;
i = 1;
a = 0;
b = 1;
while (i < n) {
    w = a + b;
    a = b;
    b = w;
    i = i + 1;
}
print(w, "\n");
```

### Test case thirteen

```
/* FizzBuzz */
i = 1;
while (i <= 100) {
    if (!(i % 15))
        print("FizzBuzz");
    else if (!(i % 3))
        print("Fizz");
    else if (!(i % 5))
        print("Buzz");
    else
        print(i);
 
    print("\n");
    i = i + 1;
}
```

### Test case fourteen

```
/* 99 bottles */
bottles = 99;
while (bottles > 0) {
    print(bottles, " bottles of beer on the wall\n");
    print(bottles, " bottles of beer\n");
    print("Take one down, pass it around\n");
    bottles = bottles - 1;
    print(bottles, " bottles of beer on the wall\n\n");
}
```

### Test case fifteen

```
/*
 Simple prime number generator
 */
count = 1;
n = 1;
limit = 100;
while (n < limit) {
    k=3;
    p=1;
    n=n+2;
    while ((k*k<=n) && (p)) {
        p=n/k*k!=n;
        k=k+2;
    }
    if (p) {
        print(n, " is prime\n");
        count = count + 1;
    }
}
print("numbers are: ",count, "\n");
```

### Test case sixteen

```
#include<stdio.h>    
void printFibonacci(int n){    
    static int n1=0,n2=1,n3;    
    if(n>0){    
         n3 = n1 + n2;    
         n1 = n2;    
         n2 = n3;    
         printf("%d ",n3);    
         printFibonacci(n-1);    
    }    
}    
int main(){    
    int n;    
    printf("Enter the number of elements: ");    
    scanf("%d",&n);    
    printf("Fibonacci Series: ");    
    printf("%d %d ",0,1);    
    printFibonacci(n-2);//n-2 because 2 numbers are already printed    
  return 0;  
 }   
 ```