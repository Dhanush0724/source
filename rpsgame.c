///Basic Beginner c program 
/// ROck paper Scissors game 
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int R=1;
    int P=2;
    int S=3;
    int i;
    int Pscore =0;
    int Bscore =0;
    int choice; 
    srand(time(NULL));
    printf("HI!!!! Have a nice day\nHere your opponent will be played by computer(BOT)\n welcome to game choose the option \n");
   
    printf("Rock=1\nPaper= 2\nScissors= 3\n");
    for(i=0;i<5;i++){
        printf("Enter your choice:");
        scanf("%d",&choice);
            int BOT=rand()%3+1;
            if(choice==1){
                if(BOT==1){
                    printf("Draw\n");
                }
                if(BOT==2){
                    printf("BOT Wins!\n");
                    Bscore= Bscore + 1;
                }
                if(BOT==3){
                    printf("Player Wins\n");
                    Pscore = Pscore + 1;
                }
               
                
            }
              else  if(choice==2){
                    if(BOT==2){
                        printf("Draw\n");
                    }
                    if(BOT==3){
                        printf("Player Wins!\n");
                        Pscore = Pscore + 1;
                    }
                    if(BOT==1){
                        printf("BOT Wins!\n");
                        Bscore= Bscore + 1;
                    }
                    
                }
                else if(choice==3){
                    if(BOT==3){
                        printf("Draw\n");
                    }
                    if(BOT==2){
                        printf("BOT Wins!\n");
                        Bscore= Bscore + 1;
                    }
                    if(BOT==1){
                        printf("Player Wins!\n");
                        Pscore = Pscore + 1;

                    }
                    
                }
        else{
            printf("Wrong Answer\n");
        }

            }
            if(Bscore > Pscore ){
                printf("BOT wins %d to %d\n",Bscore,Pscore);
            }
            else if(Bscore < Pscore ){
                printf("Player wins %d to %d\n",Pscore,Bscore);
            }
           else if(Bscore = Pscore ){
               printf("Player BOT draw %d to %d\n",Pscore,Bscore);
            }
            printf("Thank you for playing game");
            



    return 0;
}
//programmed by dhanush...
