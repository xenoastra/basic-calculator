#include <stdio.h>
#include <string.h>

void calc(){

int input;
while (input <= 5){
  printf("\n------------------------------------------------------");
  printf("\nWelcome to the calculator program!");
  printf("\nPlease choose the operation you desire by entering the appropriate number:\n");
  printf("\n1. addition\n2. subtraction\n3. multiplication\n4. division\n5. exit\n");
  printf("------------------------------------------------------");
  printf("\n\nEnter a number: ");
  int input;
  double num1;
  double num2;
  scanf("%d", &input);
  
    if(input == 1){
        printf("Enter the first number: ");
         scanf("%lf", &num1);
         printf("Enter another number: ");
         scanf("%lf", &num2);
         printf("%f", num1 + num2);
      }
    else if(input == 2){
         printf("Enter the first number: ");
         scanf("%lf", &num1);
         printf("Enter another number: ");
         scanf("%lf", &num2);
         printf("%f", num1 - num2);
     }
    else if(input == 3){
         printf("Enter the first number: ");
         scanf("%lf", &num1);
         printf("Enter another number: ");
         scanf("%lf", &num2);
         printf("%f", num1 * num2);
     }
    else if(input == 4){
         printf("Enter the first number: ");
         scanf("%lf", &num1);
         printf("Enter another number: ");
         scanf("%lf", &num2);
         printf("%f", num1 / num2);
     }
    else if (input == 5){
      printf("done\n");
      exit(1);
     }
    else{
      printf("invalid, enter a number from 1 to 5");
    }
}

}

int main(){
  calc();
    return 0;
}



