#include <stdio.h>
#include <X11/Xlib.h>
#include <tkPort.h>

int get_property_value(Display* display, Window window,char *propname, long max_length,
                       unsigned long *nitems_return, unsigned char **prop_return);

int main() {
    printf("Hello, World!\n");
    Display * disp = XOpenDisplay(NULL);
    printf("%i\n", (int) disp);
    Window window;
    Atom atom;
    int test;
    printf("moin\n");
    //for(;;){
        XGetInputFocus(disp, &window, &test);
        XTextProperty name;
        XGetWMName(disp, window, &name);
        char ** list;
        int n;
        XTextPropertyToStringList(&name, &list, &n);
        for (int i = 0; i <n ; ++i) {
            printf("%s\n", list[i]);
        }
        sleep(5);
        XGetInputFocus(disp, &window, &test);
//        XTextProperty name;
        XGetWMName(disp, window, &name);
//        char ** list;
//        int n;
        XTextPropertyToStringList(&name, &list, &n);
        for (int i = 0; i <n ; ++i) {
            printf("%s\n", list[i]);
       // }
    }

//    atom = XInternAtom(disp, "WM_NAME", 1);
//    printf("%i\n", atom);
//    unsigned long length;
//    unsigned char * val;
//    get_property_value(disp, window, "WM_NAME",100000 , &length, &val );
//    printf("%s", val[0]);
    //atom=XListProperties(disp, window, &test );

    printf("moin2\n");
    XCloseDisplay(disp);
    return 0;
}
