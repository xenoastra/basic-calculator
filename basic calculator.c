#include<iostream> 

int main()
{
    double num1;
    double num2;
    char oper;

    printf("Enter a number: ");
    scanf("%lf", &num1);
    printf("Enter an operator: ");
    scanf("%c", &oper);
    printf("Enter another number: ");
    scanf("%lf", &num2);

   if(oper == '+'){
       printf("%f, num1 + num2");
   } else if(oper == '-'){
       printf("%f, num1 - num2");
   } else if(oper == '*'){
       printf("%f, num1 * num2");
   } else if(oper == '/'){
       printf("%f, num1 / num2");
   } else{
       printf("Invalid operator");
   }

    return 0;
}