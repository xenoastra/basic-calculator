#include <stdio.h>
int main (void){
        double num1;
        double num2;
        char operator[100] = "";
        double result;

        printf("Enter a number: ");
        scanf("%le", &num1);
        printf("Enter a second number: ");
        scanf("%le", &num2);
        printf("Enter a mathematical operator (+ - / *): ");
        scanf("%s", operator);


        if (operator == "+"){
                result = num1 + num2 ;
                printf("The result is %f \n" , result);
        }
        if (operator == "-"){
                result = (num2 - num1);
                printf("The result is %f \n" , result);

        }
        if (operator == "*"){
                result = (num1 * num2);
                printf("The result is %f \n" , result);

        }
        if(operator == "/"){
                result = (num2 / num1);
                printf("The result is %f \n" , result);

        }
        else{
                printf("Enter a valid operator ");
        }

return 0;



}
