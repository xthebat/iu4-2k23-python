#include <setjmp.h>
#include <stdarg.h>


#define HUGE_STRING_LEN	8192
#define STRING_MAX 256
#define STRING_INC 256


void CuStringRead(char* str, const char* path);
void CuStringAppend(char* str, const char* text);
void CuStringAppendChar(char* str, char ch);
void CuStringAppendFormat(char* str, const char* format);
void CuStringInsert(char* str, const char* text, int pos);
void CuStringResize(char* str, int newSize);
