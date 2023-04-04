// example for parser
// define всегда на одной строке если только нет знака \
// остальное заканчивается знаком ;
#define FIRST   12
#define SECOND  FIRST * 2
#define THIRD   (1 << 10)

#define SOME_LONG_VAL   FIRST + SECOND +\
                        23 + THIRD
#define u16     uint16_t

typedef int         t_variable;
typedef int         t_int_arr[10];
typedef const char* t_cptr_string;
typedef int*        t_int_ptr;
typedef void*       t_ptr_void;
typedef u16         t_some_bytes[100];


void void_func(void);
int  int_func
              int a, int b,
              int c, int d
              );

int* ptr_int_func(int* ptr_int, const char* p_string);

u16 def_type_no_names(t_ptr_void, t_int_ptr);
u16 u16_ret_(void*, ...);
u16 func_ptr(const t_int_ptr* pcplx_arr, u16 (*pfsqrt)(u32));

static void do_static_func(...);
extern t_int_arr extern_func(register int some, long long int just_some);
volatile char volatile_func();
uint16_t create(register int, long int);


// deviant input
int func_1(...);char keke(void);#define SOME 10
