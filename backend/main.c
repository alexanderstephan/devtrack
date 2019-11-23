#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <time.h>
#include <X11/Xlib.h>

FILE *output_file;

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
  new_node->next=NULL;
  return new_node;
}

data_t * new_node(char *act){
  return create_new_node(act, time(NULL));
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

data_t * insert_and_append(data_t * head, data_t * to_insert){
  fprintf(output_file, "%i %s\n", to_insert->timestamp, to_insert->act);
  fflush(output_file);
  return insert_event(head, to_insert);
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

int open_socket(){
  int listener_d=socket(PF_INET, SOCK_STREAM, 0);
  return listener_d;
}

void bind_to_local_port(int socket, int port){
  struct sockaddr_in name;
  name.sin_family=PF_INET;
  name.sin_port=(in_port_t)htons(port);
  name.sin_addr.s_addr=htonl(INADDR_ANY);
  int reuse=1;
  setsockopt(socket, SOL_SOCKET, SO_REUSEADDR, (char *) &reuse, sizeof(int));
  int c=bind(socket, (struct sockaddr *) &name, sizeof(name));
}

int split_string(char str[], char delim[], char *str_array[]){
  //char *str_array[64];
  int counter=0;
  char *ptr=strtok(str, delim);
  while(ptr!=NULL){
    if(*ptr==' ')
      ptr++;
    str_array[counter]=ptr;
    counter++;
    ptr=strtok(NULL, delim);
  }
  return counter;
}

int main(int argv, char** args){
  
  char file_to_open[128];
  sprintf(file_to_open,"/home/confringe/Hackatum/%i", get_current_day());
  output_file=fopen(file_to_open, "a");
  //printf("%s\n", file_to_open);
  //data_t * head=insert_and_append(NULL, create_new_node("Hello World", 12));
  data_t * head=NULL;
  //data_t * toin=create_new_node("Hello World2", 14);
  //printf("%s\n", toin->act);
  //head=insert_and_append(head, toin);
  //head=insert_and_append(head, new_node("LOLOL"));
  //print_list(head);

  
  FILE *fp;
  char last_string[256]="";
  char path[256];

  fp = popen("while true; do wmctrl -l | grep $(printf '%x' $(xdotool getwindowfocus)) && sleep 1; done", "r");
  if (fp == NULL) {
    printf("Failed to run command\n" );
    exit(1);
  }

  while (fgets(path, sizeof(path), fp) != NULL) {
    path[strlen(path)-1]='\0';
    if(strcmp(path+19, last_string))
      head=insert_and_append(head, new_node(path+19));
    strcpy(last_string, path+19);
    print_list(head);
  }
  

  /* struct sockaddr_storage client_addr; */
  /* unsigned int address_size=sizeof(client_addr); */
  /* int listener=open_socket(); */
  /* bind_to_local_port(listener, 6699); */

  /* listen(listener, 10); */
  
  /* int tempconn; */
  
  /* while(1){ */
  /*   tempconn=accept(listener, (struct sockaddr *) &client_addr, &address_size); */
  /* } */

    

  return 0;
}
