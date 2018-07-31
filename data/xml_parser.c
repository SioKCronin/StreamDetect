/* Check expat for specific parsing */

int Depth;

void

start(void *data, const char *el, const char **attr) {
    
    int i;

    for (i = 0; i < Depth; i++)

        printf(" ");

    printf("%s", el);

    for (i = 0
