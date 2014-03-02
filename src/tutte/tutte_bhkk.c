/*****************************************************************************
*
*  Name:         tutte_bhkk.c
* 
*  Description:  Calculates a small graph's Tutte polynomial 
*                based on the algorithm in "Computing the Tutte polynomial 
*                in vertex-exponential time", Andreas Björklund, 
*                Thore Husfeldt, Petteri Kaski, Mikko Koivisto,
*                Proceedings 49th Annual IEEE Symposium on Foundations of 
*                Computer Science (FOCS) 2008.
*
*  Input:        The number of vertices n <= MAXN followed by an 
*                n x n space-delimited 0/1 matrix
*                describing the adjacency matrix of the graph.
*
*  Output:       The coefficients of the Tutte polynomial 
*                in rectangle format.
*
*  Version:      1.0
*
*  Revision history:  2010-11-17  1.0
*
******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include <ctype.h>
#include <limits.h> /* INT_MAX, LONG_MAX, etc. */

#include <gmp.h> /* GNU multiple-precision arithmetic library, gmplib.org */

#define MAXN 30
#define MAXM (MAXN*(MAXN-1)/2)

typedef unsigned long int scalar_t; /* Scalars must be unsigned. */
#define SCALAR_MAX ULONG_MAX

int verbose = 0;
FILE *verb_out;

/******************************************************* Common subroutines. */

#define ERROR(...) error(__FILE__,__LINE__,__func__,__VA_ARGS__);

static void error(const char *fn, int line, const char *func,
                  const char *format, ...)
{
    va_list args;
    va_start(args, format);
    fprintf(stderr,
            "ERROR [file = %s, line = %d]\n"
            "%s: ",
            fn,
            line,
            func);
    vfprintf(stderr, format, args);
    fprintf(stderr, "\n");
    va_end(args);
    abort();
}

static int min(int a, int b)
{
    if(a < b)
        return a;
    return b;
}

static int max(int a, int b)
{
    if(a > b)
        return a;
    return b;
}

/******************************************************** Memory allocation. */

#define MALLOC(x) malloc_wrapper(x)
#define FREE(x) free_wrapper(x)

int malloc_balance = 0;

static void *malloc_wrapper(size_t size)
{
    if(verbose) 
        fprintf(verb_out, 
                "malloc_wrapper: allocating %lld bytes [balance %d]\n",
                (long long int) size,
                malloc_balance);
    void *p = malloc(size);
    if(p == NULL)
        ERROR("malloc fails");
    malloc_balance++;
    return p;
}

static void free_wrapper(void *p)
{
    free(p);
    malloc_balance--;
    if(verbose) 
        fprintf(verb_out, 
                "free_wrapper: released allocated memory [balance %d]\n",
                malloc_balance);
}

/****************************************************** Arithmetic in GF(p). */

static void scalar_modmult(scalar_t *d, scalar_t a, scalar_t b, scalar_t mod)
{
    *d = (a*b) % mod;
}

static void scalar_modexp(scalar_t *d, scalar_t a, scalar_t ex, scalar_t mod)
{
    if (ex == 0) {
        *d = 1;
    } else {
        if (ex == 1) {
            *d = a;
        } else {
            scalar_t t;
            scalar_modexp(&t, a, ex>>1, mod);
            if (ex&1) {
                scalar_t tt;
                scalar_modmult(&tt, t, t, mod);
                scalar_modmult(d, tt, a, mod);
            } else {
                scalar_modmult(d, t, t, mod);
            }
        }
    }
}

/* Only works for a prime modulus. */

static scalar_t scalar_modinverse(scalar_t val, scalar_t mod) 
{
    scalar_t tmp;
    scalar_modexp(&tmp,
                  val % mod,
                  mod-2, 
                  mod);
    return tmp;
}

/************************* Polynomial arithmetic with coefficients in GF(p). */

typedef scalar_t poly_t;

/* Globals. */

static scalar_t poly_modulus;
static int poly_maxdeg;

#define POLY_AREF_N(p,j) ((p)+(j)*(MAXN+2))
#define POLY_AREF_M(p,j) ((p)+(j)*(MAXM+2))

#define POLY_N(c) poly_t c[MAXN+2]
#define POLY_M(c) poly_t c[MAXM+2]
#define POLY_ARRAY_N(p,c) poly_t p[(c)*(MAXN+2)]
#define POLY_ARRAY_M(p,c) poly_t p[(c)*(MAXM+2)]
#define POLY_ARRAY_N_SIZE(c) (sizeof(scalar_t)*(c)*(MAXN+2))
    
static void poly_set_modulus(scalar_t m)
{
    poly_modulus = m;  
}

static void poly_set_max_degree(int d)
{
    poly_maxdeg = d;
}

static void poly_copy(poly_t *d, poly_t *a)
{
    scalar_t *ac = a+1;
    scalar_t *dc = d+1; 
    *d = *a;
    for (int i = 0; i <= (int) *a; i++)
        dc[i] = ac[i];
}

static void poly_zero(poly_t *d)
{
    d[0] = 0;
    d[1] = 0;
}

static void poly_add(poly_t *d, poly_t *a, poly_t *b)
{
    scalar_t *dc = d+1;
    scalar_t *ac = a+1;
    scalar_t *bc = b+1;
    int dd = min(max(*a,*b),poly_maxdeg);
    for (int i = 0; i <= dd; i++) {
        scalar_t t = (((int) *a >= i) ? ac[i] : 0)
                     +(((int) *b >= i) ? bc[i] : 0);
        if (t >= poly_modulus)
            t -= poly_modulus;
        dc[i] = t;
    }  
    *d = dd;
    while (*d > 0 && dc[*d] == 0) 
        (*d)--;
}

static void poly_set_monomial(poly_t *d, int exp, scalar_t val)
{
    scalar_t *dc = d+1;
    dc[exp] = val % poly_modulus; 
    for (int i = *d + 1; i < exp; i++)
        dc[i] = 0;
    *d = max(*d,exp);
}

static void poly_mult(poly_t *d, poly_t *a, poly_t *b)
{
    scalar_t *dc = d+1;
    scalar_t *ac = a+1;
    scalar_t *bc = b+1;
    *d = min(*a + *b, poly_maxdeg);
    for (int i = 0; i <= (int) *d; i++)
        dc[i] = 0;
    
    for (int i = 0 ; i <= (int) *a; i++) {
        if (ac[i]) {
            int t = min(*b,poly_maxdeg-i);
            for (int j = 0; j <= t; j++) {
                if (bc[j]) {
                    scalar_t p = (ac[i]*bc[j]) % poly_modulus;
                    scalar_t q = dc[i+j] + p;
                    if(q >= poly_modulus)
                        q -= poly_modulus;
                    dc[i+j] = q;
                }
            }
        }
    }
    while (*d > 0 && dc[*d] == 0) 
        (*d)--;
}

static void poly_mult_scalar(poly_t *d, poly_t *a, scalar_t val)
{
    val = val % poly_modulus;  
    if(val == 0) {
        d[0] = 0;
        d[1] = 0;
    } else {
        scalar_t *dc = d+1;
        scalar_t *ac = a+1;
        *d = *a;
        for (int i = 0; i <= (int) *a; i++)
            dc[i] = (ac[i]*val) % poly_modulus;
    }
}

static void poly_div_scalar(poly_t *d, scalar_t val)
{
    scalar_t ival = scalar_modinverse(val, poly_modulus);
    if(ival == 0)
        ERROR("division by zero");
    scalar_t *dc = d+1;
    for (int i = 0; i <= (int) *d; i++)
        dc[i] = (dc[i]*ival) % poly_modulus;
}

static void poly_rip(scalar_t *d, poly_t *a, int degree)
{
    scalar_t *ac = a+1;
    if (degree <= (int) *a)
        *d = ac[degree];
    else
        *d = 0;  
}

/********************************************* Tutte polynomial computation. */

/* Globals. */

int n, m;
int E[MAXN][MAXN];

scalar_t gmodulus; 

int *num_edges;
int *num_vertices;
poly_t *pi_1;

scalar_t pu[MAXN];
scalar_t p[MAXN];
scalar_t mp[MAXM+1][MAXN];
scalar_t pval;
scalar_t pvalplus1pow[MAXM+1];

POLY_ARRAY_M(lagr, MAXM+1);
POLY_ARRAY_N(lagr_intra, MAXN+1);
POLY_ARRAY_M(parts, MAXN);
POLY_ARRAY_N(parts_intra, MAXM);
POLY_ARRAY_M(xm1, MAXM+1);

/* Number of vertices and edges in induced subgraphs. */

static void calc_num_verts_edges(void)
{
    int X;
    for (X = 0; X < (1<<n); X++) {
        int i, j;
        int cnt = 0;
        int Y = X;
        while (Y) {
            cnt += (Y&1);
            Y >>= 1;
        }
        num_vertices[X] = cnt;
        cnt = 0;
        for (i = 0; i < n; i++)
            if (X & (1<<i))
                for (j = 0; j < n; j++)
                    if (X & (1<<j))
                        cnt += E[i][j];
        num_edges[X] = cnt / 2;
    }  
}

/* Number of connected components in input graph. */

int num_comp;
int compv[MAXN][MAXN];
int compsize[MAXN];
int compvis[MAXN];

static void compdfs(int v) {
    if (!compvis[v]) {
        compv[num_comp][compsize[num_comp]++] = v;
        compvis[v] = 1;
        for (int i = 0; i < n; i++)
            if (E[v][i])
                compdfs(i);
    }
}  

static int num_components(void)
{
    num_comp = 0;
    for (int i = 0; i < n; i++) {
        compsize[i] = 0;
        compvis[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        if (!compvis[i]) {
            compdfs(i);
            num_comp++;
        }
    }
    return num_comp;
}

/* Computes the Laplacian of a component of the input graph. */

static mpq_t *init_component_laplacian(int u, int *s)
{
    int nn = compsize[u];
    int *q = &compv[u][0];
    mpq_t *l = MALLOC(sizeof(mpq_t)*nn*nn);
    for(int i = 0; i < nn; i++) {
        for(int j = 0; j < nn; j++) {
            mpq_init(l[i*nn+j]);
            if(i == j) {
                int c = 0;
                for(int k = 0; k < nn; k++)
                    if(E[q[i]][q[k]])
                        c++;
                mpq_set_si(l[i*nn+j], c, 1);
            } else {
                if(E[q[i]][q[j]])
                    mpq_set_si(l[i*nn+j], -1, 1);
                else
                    mpq_set_si(l[i*nn+j], 0, 1);
            }
        }
    }
    *s = nn;
    return l;
}

static void clear_laplacian(int u, mpq_t *l)
{
    for(int i = 0; i < u; i++)
        for(int j = 0; j < u; j++)
            mpq_clear(l[i*u+j]);
    FREE(l);
}

/* Computes the determinant of an s x s rational matrix "a". */

static void det(int s, mpq_t *a, mpq_t d)
{
    mpq_t f, g;
    mpq_init(f);
    mpq_init(g);
    int pivotrow[s]; 
    int sgn = 0;
    for(int i = 0; i < s; i++)
        pivotrow[i] = i;    
    for(int j = 0; j < s; j++) {
        /* Find pivot row in column j. */
        {
        int i;
        for(i = j; i < s; i++) {
            int ii = pivotrow[i];
            if(mpq_cmp_ui(a[ii*s+j], 0, 1) != 0) {
                pivotrow[i] = pivotrow[j];
                pivotrow[j] = ii;
                if(i != j)
                    sgn++;
                break;
            }
        }
        if(i == s) {
            /* No pivot -- zero determinant. */
            mpq_set_ui(d, 0, 1);
            goto detdone;
        }
        }   
        /* Zero out non-used rows in column j
           by scaling the pivot row. */
        {
        int y = pivotrow[j];
        for(int i = j+1; i < s; i++) {
            int ii = pivotrow[i];
            if(mpq_cmp_ui(a[ii*s+j], 0, 1) != 0) {
                mpq_div(f, a[ii*s+j], a[y*s+j]);
                for(int k = 0; k < s; k++) {
                    mpq_mul(g, f, a[y*s+k]);
                    mpq_sub(a[ii*s+k], a[ii*s+k], g);
                }
            }
        }
        }       
    }
    /* Get the determinant. */
    mpq_set_ui(d, 1, 1);
    for(int j = 0; j < s; j++)
        mpq_mul(d, d, a[pivotrow[j]*s+j]);
    if(sgn % 2)
        mpq_neg(d, d);
detdone:
    mpq_clear(g);
    mpq_clear(f);
}

/* Computes the number of spanning trees of a connected 
   graph given by a Laplacian. */
  
static void get_num_spanning_trees(int u, mpq_t *l, mpz_t ns)
{
    int s = u-1;
    if(s == 0) {
        mpz_set_ui(ns, 1);
        return;
    }
    mpq_t *q = MALLOC(sizeof(mpq_t)*s*s);
    for(int i = 0; i < s; i++) {
        for(int j = 0; j < s; j++) {
            mpq_init(q[i*s+j]);
            mpq_set(q[i*s+j], l[i*u+j]);
        }
    }
    mpq_t d;
    mpq_init(d);
    det(s, q, d);
    if(mpz_cmp_ui(mpq_denref(d),1) != 0)
        ERROR("nonintegral determinant");
    mpz_set(ns, mpq_numref(d));
    mpq_clear(d);
    for(int i = 0; i < s; i++)
        for(int j = 0; j < s; j++)
            mpq_clear(q[i*s+j]);
    FREE(q);
}

/* In-place update. */

static void update(int X, int i)
{
    while (X & (1<<i)) {
        poly_add(POLY_AREF_N(pi_1, X), 
                 POLY_AREF_N(pi_1, X), 
                 POLY_AREF_N(pi_1, X^(1<<i)));
        update(X^(1<<i), i+1);
        i++;
    }
}

/* Main iteration. */

static void subset_sieve(void)
{
    int X;
    int i, j;  
    for (i = 0; i < n; i++) 
        pu[i] = 0;
  
    for (X = 0; X < (1<<n); X++) { 
        int nX, mX;
        POLY_N(beta);
        POLY_ARRAY_N(betapow, 2);
        
        scalar_t part;
        
        nX = num_vertices[X];   
        mX = num_edges[X];
         
        poly_zero(POLY_AREF_N(pi_1,X));
        poly_set_monomial(POLY_AREF_N(pi_1,X),nX,pvalplus1pow[mX]);
        poly_copy(beta, POLY_AREF_N(pi_1,X));
        
        for (i = 0; i < n; i++)
            if (X & (1<<i))
                poly_add(beta, 
                         beta, 
                         POLY_AREF_N(pi_1,X^(1<<i)));
        
        poly_copy(POLY_AREF_N(betapow, 1), 
                  beta);
        
        for (j = 1; j < n; j++) { /* Loop over Potts' states (j+1) */
            poly_mult(POLY_AREF_N(betapow,(1-(j&1))), 
                      POLY_AREF_N(betapow,(j&1)), 
                      beta);
            poly_rip(&part, 
                     POLY_AREF_N(betapow,(1-(j&1))), 
                     n);
            if ((n^nX)&1)
              pu[j]=(pu[j]-part+gmodulus) % gmodulus;
            else
              pu[j]=(pu[j]+part) % gmodulus;
        }
   
        if (nX != n) 
            update(X, 0);
    }
}

/* Test primality by trial division. */

static int isprime(scalar_t z)
{
    if(z < 2)
        return 0;
    for(scalar_t q = 2; q*q <= z; q++)
        if(z % q == 0)
            return 0;
    return 1;
}

/* Main procedure. */

static void solve(FILE *out)
{    
    int i, j, v, cmp;
    mpz_t a, b, c, d, e, N;
    mpz_t tutte_coeff[MAXN][MAXM+1];
    scalar_t tutte_coeff_mod[MAXN][MAXM+1];

    /* Initialize multiple-precision integers. */
    mpz_init(a);
    mpz_init(b);
    mpz_init(c);
    mpz_init(d);    
    mpz_init(e);    
    mpz_init(N);
    for (i = 0; i < n; i++) {
        for (j = 0; j <= m; j++) {
            mpz_init(tutte_coeff[i][j]);
            mpz_set_si(tutte_coeff[i][j], 0);
        }
    }

    /* Allocate globals. */
    {
    int pow_2_n = 1<<n;
    num_vertices = MALLOC(sizeof(int)*pow_2_n);
    num_edges = MALLOC(sizeof(int)*pow_2_n);
    pi_1 = MALLOC(POLY_ARRAY_N_SIZE(pow_2_n));
    }

    if(verbose)
        fprintf(verb_out, 
                "solve: tabulating induced subgraphs\n");
    
    calc_num_verts_edges();
    cmp = num_components();
    if(verbose)
        fprintf(verb_out, "solve: number of components = %d\n", cmp);

    /* Calculate the number of maximal spanning forests. */
    mpz_t num_max_spanning_forests;
    mpz_init(num_max_spanning_forests);
    mpz_set_ui(num_max_spanning_forests, 1);
    {
    mpz_t num_spanning_trees;
    mpz_init(num_spanning_trees);
    for(int k = 0; k < cmp; k++) {
        int s;      
        mpq_t *l = init_component_laplacian(k, &s);
        get_num_spanning_trees(s, l, num_spanning_trees);
        clear_laplacian(s, l);
        mpz_mul(num_max_spanning_forests, 
                num_max_spanning_forests, 
                num_spanning_trees);
    }
    mpz_clear(num_spanning_trees);
    if(verbose) {
        fprintf(verb_out, "solve: number of maximal spanning forests = ");
        mpz_out_str(verb_out, 10, num_max_spanning_forests);
        fprintf(verb_out, "\n");
    }
    }
 
    /* Determine the moduli to be used. */  
    scalar_t modtab[MAXM];
    int nmod = 0;
    {
    mpz_t max_tutte_coeff;  
    mpz_init(max_tutte_coeff);
    /* No coefficient is larger than the number of 
       spanning trees of G, which is at most n^{n-2},
       the number of labeled trees on n vertices
       (Cayley's Theorem). */
    mpz_set(max_tutte_coeff, num_max_spanning_forests);
    mpz_set_ui(a, SCALAR_MAX);
    mpz_sqrt(a, a);
    scalar_t maxz = mpz_get_ui(a);
    mpz_set_si(N, 1);
    scalar_t z;
    if(verbose)
        fprintf(verb_out, 
                "solve: moduli = ");
    for(z = maxz; z > (scalar_t) m; z--) {
        /* Modulus must be greater than m for Lagrange polynomials --
         * otherwise a divide by zero will occur. */
        if(isprime(z)) {
            if(verbose)
                fprintf(verb_out, 
                        "%llu", 
                        (unsigned long long int) z);
            modtab[nmod++] = z;         
            mpz_mul_ui(N, N, z);
            if(mpz_cmp(N, max_tutte_coeff) > 0)
                break;
            if(verbose)
                fprintf(verb_out, " ");
        }
    }
    if(z <= (scalar_t) m)
        ERROR("not enough moduli");
    if(verbose)
        fprintf(verb_out, "\n");
    mpz_clear(max_tutte_coeff);
    }
    
    
    /* Compute the coefficients modulo each modulus. */

    for(int u = 0; u < nmod; u++) {
        if(verbose)
            fprintf(verb_out, 
                    "solve: solving for modulus %llu\n", 
                    (unsigned long long int) modtab[u]);
        gmodulus = modtab[u];
        poly_set_modulus(gmodulus);
        poly_set_max_degree(n);
  
        for (v = 1; v <= m-n+cmp+1; v++) { /* Loop over v-assignments. */
            scalar_t tmp,tmp2;
            if(verbose)
                fprintf(verb_out, 
                        "solve: evaluating at v = %d\n", 
                        v);
            
            /* Calculate pvalplus1pow powers. */
            pval = v;
            pvalplus1pow[0] = 1;
            for (i = 1; i <= m; i++)
                pvalplus1pow[i] = (pvalplus1pow[i-1]*(v+1)) % gmodulus;
             
            subset_sieve();
            
            /* Copy result for use later. */
            for (i = 1; i < n; i++)
                mp[v][i] = pu[i];
        
            /* Build trivial hyperbola contribution. */
            scalar_modexp(&tmp,v+1,m,gmodulus); 
            mp[v][0] = tmp;
            
            
            /* Move from modular Potts to Tutte on hyperbolas. */
            scalar_modexp(&tmp2,scalar_modinverse(v,gmodulus),n-cmp,gmodulus);       
            for (i = 0; i < n; i++) { 
                scalar_modexp(&tmp,scalar_modinverse(i+1,gmodulus),cmp,gmodulus); 
                tmp=(tmp2*tmp) % gmodulus; 
                mp[v][i]=(mp[v][i]*tmp) % gmodulus;
            }
        }
               
        
        /* Lagrange interpolation. */
        
        for (v = 1;v <= m-n+cmp+1; v++) { 
          /* For each y-value i.e. fixed v above, 
             Lagrange-interpolate for x. */   
          scalar_t vinvers=scalar_modinverse(v,gmodulus);
          /* Compute Lagrange polynomials. */
          for (i = 0; i < n; i++) {
            scalar_t xi=((i+1+v)*vinvers) % gmodulus;
            
            poly_zero(POLY_AREF_N(lagr_intra, i));
            poly_set_monomial(POLY_AREF_N(lagr_intra, i), 0, 1);
            for (j = 0; j < n; j++) {
                if (i != j) {
                    scalar_t xj=((j+1+v)*vinvers) % gmodulus;
                    POLY_N(t);
                    POLY_N(tt);
                    poly_zero(t);  
                    poly_set_monomial(t, 0, gmodulus-xj);
                    poly_set_monomial(t, 1, 1);
                    poly_div_scalar(t, (xi-xj+gmodulus) % gmodulus);
                    poly_copy(tt, POLY_AREF_N(lagr_intra, i));
                    poly_mult(POLY_AREF_N(lagr_intra, i), tt, t);
                }
            }
          }  
        
          /* Interpolate. */ 
          poly_zero(POLY_AREF_N(parts_intra, v-1)); // -1
          
          for (j = 0; j < n; j++) {
              POLY_N(t);
              poly_mult_scalar(t,
                               POLY_AREF_N(lagr_intra, j),
                               mp[v][j]);
              poly_add(POLY_AREF_N(parts_intra, v-1), // -1
                       POLY_AREF_N(parts_intra, v-1), // -1
                       t);
          }
        }
      
        if(verbose)
            fprintf(verb_out, 
                    "solve: interpolating modular coefficients\n");
        
        poly_set_max_degree(m);
        
        /* Calculate Lagrange polynomials. */
        for (i = 0; i <= m-n+cmp; i++) { // 0
            scalar_t xi=i+2;
            poly_zero(POLY_AREF_M(lagr, i));
            poly_set_monomial(POLY_AREF_M(lagr, i), 0, 1);
            for (j = 0; j <= m-n+cmp; j++) { // 0
                if (i != j) {
                    scalar_t xj=j+2;
                    POLY_M(t);
                    POLY_M(tt);
                    poly_zero(t);  
                    poly_set_monomial(t, 0, gmodulus-xj);
                    poly_set_monomial(t, 1, 1);
                    poly_div_scalar(t, (xi-xj+gmodulus) % gmodulus);
                    poly_copy(tt, POLY_AREF_M(lagr, i));
                    poly_mult(POLY_AREF_M(lagr, i), tt, t);
                }
            }
        }
        
        /* Interpolate. */ 
        for (i = 0; i < n; i++) {
            poly_zero(POLY_AREF_M(parts, i));
            
            for (j = 0; j <= m-n+cmp; j++) {
                POLY_N(t);
                scalar_t val;
                poly_rip(&val,POLY_AREF_N(parts_intra,j),i);
                poly_mult_scalar(t,
                                 POLY_AREF_M(lagr, j),
                                 val);
                poly_add(POLY_AREF_M(parts, i),
                         POLY_AREF_M(parts, i),
                         t);
            }
        }
        
        for (i = 0; i < n; i++)  
            for (j = 0; j <= m; j++) {
                scalar_t val;
                poly_rip(&val, POLY_AREF_M(parts, i), j);
                tutte_coeff_mod[i][j] = val;
            }

        if(verbose)
            fprintf(verb_out, 
                    "solve: updating coefficients\n");

        /* Update coefficients based on modular
         * coefficients and the Chinese Remainder Theorem. */
        mpz_set_ui(a, gmodulus);
        mpz_divexact(b, N, a);
        mpz_gcdext(e, c, d, a, b);
        if(mpz_cmp_ui(e, 1) != 0)
            ERROR("invalid moduli");
        mpz_mul(e, b, d);
        for (i = 0; i < n; i++) {
            for (j = 0; j <= m; j++) {
                mpz_mul_ui(a, e, tutte_coeff_mod[i][j]);
                mpz_add(tutte_coeff[i][j], 
                        tutte_coeff[i][j],
                        a);
                mpz_fdiv_qr(a, tutte_coeff[i][j], 
                            tutte_coeff[i][j], N);
            }
        }
    }

    /* Check that the sum of coefficients is equal to 
       the number of spanning trees. */
    {
    mpz_set_ui(a, 0);
    for (i = 0; i < n; i++)
        for (j = 0; j <= m; j++)
            mpz_add(a, a, tutte_coeff[i][j]);
    if(mpz_cmp(a, num_max_spanning_forests) != 0)
        ERROR("coefficients fail maximal spanning forest test");
    if(verbose)
        fprintf(verb_out, 
                "solve: coefficients pass maximal spanning forest test\n");
    }
    mpz_clear(num_max_spanning_forests);

    /* Check that the number of spanning subgraphs is 2^m. */
    {
    mpz_t two_pow_m;  
    mpz_init(two_pow_m);
    mpz_ui_pow_ui(two_pow_m, 2, m);
    mpz_set_ui(a, 0);
    for (i = 0; i < n; i++) {
        for (j = 0; j <= m; j++) {
            mpz_ui_pow_ui(b, 2, i+j);
            mpz_mul(b, b, tutte_coeff[i][j]);
            mpz_add(a, a, b);
        }
    }
    if(mpz_cmp(a, two_pow_m) != 0)
        ERROR("coefficients fail spanning subgraph test");
    mpz_clear(two_pow_m);
    if(verbose)
        fprintf(verb_out, 
                "solve: coefficients pass spanning subgraph test\n");
    }
    
    /* Output coefficients of the Tutte polynomial in rectangle 
       format after removal of rightmost zeros. */
    {
    if(verbose)
        fprintf(verb_out, 
                "solve: writing coefficients to output\n");
    int last[n+1];
    last[n-cmp+1] = 0;
    for (i = n-cmp; i >= 0; i--) {
        int k;
        for (k = m; 
             k > last[i+1] && mpz_cmp_ui(tutte_coeff[i][k], 0) == 0;
             k--)
            ;
        last[i] = k;
    }
    for (i = 0; i < n-cmp+1; i++) {
        for (j = 0; j <= last[i]; j++) {
            mpz_out_str(out, 10, tutte_coeff[i][j]);
            if(j < last[i])
                fprintf(out, " ");
        }
        fprintf(out, "\n");
    }
    fprintf(out, "\n");
    }   

    /* Free globals. */
    {
      FREE(pi_1);
      FREE(num_edges);
      FREE(num_vertices);
    }

    /* Release multiple-precision integers. */
    for (i = 0; i < n; i++)
        for (j = 0; j <= m; j++)
            mpz_clear(tutte_coeff[i][j]);
    mpz_clear(N);
    mpz_clear(e);
    mpz_clear(d);
    mpz_clear(c);
    mpz_clear(b);
    mpz_clear(a);

}

static void skipws(FILE *in)
{
    int c;
    do {
        c = fgetc(in);
        if(c == EOF)
            break;
    } while(isspace(c));
    if(c != EOF)
        ungetc(c, in);
}

/* Program entry point. */

int main(int argc, char **argv)
{
    int ap = 1;
    while(ap < argc) {
        if(!strcmp(argv[ap], "-v")) {
            verbose = 1;
            verb_out = stderr;
            ap++;
            continue;
        }
        break;
    }
    const char *fn;
    FILE *in;
    if(ap >= argc) {
        fn = "stdin";
        in = stdin;
        if(verbose)
            fprintf(verb_out, 
                    "main: no input file given -- reading from stdin\n");
    } else {
        fn = argv[ap];
        in = fopen(fn, "r");
        if(in == NULL)
            ERROR("error opening \"%s\" for input", fn);
        if(verbose)
            fprintf(verb_out, "main: reading input from \"%s\"\n", fn);
    }
    while (!feof(in)) {
        skipws(in);
        if(fscanf(in, "%d", &n) != 1 || n < 0)
            ERROR("parse error reading \"%s\"", fn);
        if(n > MAXN)
            ERROR("MAXN exceeded");
        m = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                if(fscanf(in, "%d", &E[i][j]) != 1 || 
                   E[i][j] < 0 || 
                   E[i][j] > 1 ||
                   (i == j && E[i][j] != 0) ||
                   (i > j && E[i][j] != E[j][i]))
                    ERROR("parse error reading \"%s\"", fn);
                m += E[i][j];
            }
        m /= 2;
        if(verbose)
            fprintf(verb_out, 
                    "main: input graph has %d vertices and %d edges\n", 
                    n, m);
        solve(stdout);
        skipws(in);
    }
    if(verbose)
        fprintf(verb_out, "main: closing input\n");
    fclose(in);
    return 0;
}
