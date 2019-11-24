#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <time.h>

void bind_to_local_port(int socket, int port){
  struct sockaddr_in name;
  name.sin_family=PF_INET;
  name.sin_port=(in_port_t)htons(port);
  name.sin_addr.s_addr=htonl(INADDR_ANY);
  int reuse=1;
  if(setsockopt(socket, SOL_SOCKET, SO_REUSEADDR, (char *) &reuse, sizeof(int))==-1)
    printf("Can't set reuse option");
  int c=bind(socket, (struct sockaddr *) &name, sizeof(name));
  if(c==-1)
    printf("Error binding to port");
}

int open_socket(){
  int listener_d=socket(PF_INET, SOCK_STREAM, 0);
  if(listener_d==-1)
    printf("Failed to set up listener");
  return listener_d;
}

int main(){
  struct sockaddr_storage client_addr;
  unsigned int address_size=sizeof(client_addr);
  int listener=open_socket();
  bind_to_local_port(listener, 6699);

  listen(listener, 10);
  
  int tempconn;
  
  while(1){
    tempconn=accept(listener, (struct sockaddr *) &client_addr, &address_size);
    char *s="Hello World!\n";
    printf("Thing: %i\n", send(tempconn, s, strlen(s), 0));
  }

}
