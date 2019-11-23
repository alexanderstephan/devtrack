#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <time.h>

//FILE *output_file;

typedef struct linkedList{
  int timestamp;
  char act[128];
  struct linkedList *next;
} data_t;

data_t * create_new_node(char *act, int timestamp){
  data_t * new_node=NULL;
  new_node=malloc(sizeof(data_t));
  if(!new_node)
    return NULL;
  strcpy(new_node->act, act);
  new_node->timestamp=timestamp;
  return new_node;
}

data_t * insert_event(data_t * head, data_t * to_insert){
  if(!head)
    return to_insert;
  if(to_insert->timestamp>=head->timestamp){
    to_insert->next=head;
    return to_insert;
  }
  head->next=insert_event(head->next, to_insert);
  return head;
}

void insert_and_append(data_t * head, data_t * to_insert){
  insert_event(head, to_insert);
  /* fprintf(output_file, "%i %s\n", to_insert->act, to_insert->timestamp); */
  /* fflush(output_file); */
}

void print_list(data_t * head){
  if(head->next){
    print_list(head->next);
  }
  printf("%i %s\n", head->timestamp, head->act);
}

int get_current_day(){
  time_t s;
  struct tm *info;
  s=time(NULL);
  info=localtime(&s);
  info->tm_sec=0;
  info->tm_min=0;
  info->tm_hour=0;
  int ret=mktime(info);
  return ret;
  //return mktime(info);
}

int main(int argv, char* args){
  char file_to_open[128];
  sprintf(file_to_open,"/home/confringe/Hackatum/%i", get_current_day());
  FILE *output_file=fopen(file_to_open, "a");
  printf("%s\n", file_to_open);
  data_t * head=create_new_node("Hello World", 12);
  head=insert_event(head, create_new_node("Hello World2", 14));
  print_list(head);
}
