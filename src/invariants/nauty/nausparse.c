/*****************************************************************************
*                                                                            *
*  Sparse-graph-specific auxiliary source file for version 2.4 of nauty.     *
*                                                                            *
*   Copyright (2004-2010) Brendan McKay.  All rights reserved.               *
*   Subject to waivers and disclaimers in nauty.h.                           *
*                                                                            *
*   CHANGE HISTORY                                                           *
*       26-Oct-04 : initial creation                                         *
*       23-Nov-06 : dispatch uses targetcell_sg, not bestcell_sg             *
*        8-Dec-06 : add adjacencies_sg                                       *
*                                                                            *
*****************************************************************************/

#define TMP

/*   #define ONE_WORD_SETS  not sure about this!  See notes.txt.  */
#include "nausparse.h"

    /* macros for hash-codes: */
#define MASH(l,i) ((((l) ^ 065435) + (i)) & 077777)
    /* : expression whose long value depends only on long l and int/long i.
	 Anything goes, preferably non-commutative. */

#define CLEANUP(l) ((int)((l) % 077777))
    /* : expression whose value depends on long l and is less than 077777
	 when converted to int then short.  Anything goes. */

#if  MAXM==1
#define M 1
#else
#define M m
#endif

#define ACCUM(x,y)   x = (((x) + (y)) & 077777)

static int fuzz1[] = {037541,061532,005257,026416};
static int fuzz2[] = {006532,070236,035523,062437};

#define FUZZ1(x) ((x) ^ fuzz1[(x)&3])
#define FUZZ2(x) ((x) ^ fuzz2[(x)&3])

/* aproto: header new_nauty_protos.h */

dispatchvec dispatch_sparse =
  {isautom_sg,testcanlab_sg,updatecan_sg,refine_sg,refine_sg,cheapautom_sg,
   targetcell_sg,nausparse_freedyn,nausparse_check,init_sg,NULL};

#if !MAXN
DYNALLSTAT(short,vmark1,vmark1_sz);
DYNALLSTAT(short,vmark2,vmark2_sz);
DYNALLSTAT(shortish,work1,work1_sz);
DYNALLSTAT(shortish,work2,work2_sz);
DYNALLSTAT(shortish,work3,work3_sz);
DYNALLSTAT(shortish,work4,work4_sz);
#else
static short vmark1[MAXN];
static short vmark2[MAXN];
static shortish work1[MAXN];
static shortish work2[MAXN];
static shortish work3[MAXN];
static shortish work4[MAXN];
#endif

static short vmark1_val = 32000;
#define MARK1(i) vmark1[i] = vmark1_val
#define UNMARK1(i) vmark1[i] = 0
#define ISMARKED1(i) (vmark1[i] == vmark1_val)
#define ISNOTMARKED1(i) (vmark1[i] != vmark1_val)

static short vmark2_val = 32000;
#define MARK2(i) vmark2[i] = vmark2_val
#define UNMARK2(i) vmark2[i] = 0
#define ISMARKED2(i) (vmark2[i] == vmark2_val)
#define ISNOTMARKED2(i) (vmark2[i] != vmark2_val)

#if !MAXN
#define RESETMARKS1 {if (vmark1_val++ >= 32000) \
    {size_t ii; for (ii=0;ii<vmark1_sz;++ii) vmark1[ii]=0; vmark1_val=1;}}
#define PREPAREMARKS1(nn) preparemarks1(nn)
#define RESETMARKS2 {if (vmark2_val++ >= 32000) \
    {size_t ii; for (ii=0;ii<vmark2_sz;++ii) vmark2[ii]=0; vmark2_val=1;}}
#define PREPAREMARKS2(nn) preparemarks2(nn)
#else
#define RESETMARKS1 {if (vmark1_val++ >= 32000) \
    {size_t ii; for (ii=0;ii<MAXN;++ii) vmark1[ii]=0; vmark1_val=1;}}
#define PREPAREMARKS1(nn)
#define RESETMARKS2 {if (vmark2_val++ >= 32000) \
    {size_t ii; for (ii=0;ii<MAXN;++ii) vmark2[ii]=0; vmark2_val=1;}}
#define PREPAREMARKS2(nn)
#endif

/*****************************************************************************
*                                                                            *
*  preparemarks1(N) and preparemarks2(N)                                     *
*  make vmarks array large enough to mark 0..N-1 and such that               *
*  the next RESETMARKS command will work correctly                           *
*                                                                            *
*****************************************************************************/

static void
preparemarks1(size_t nn)
{
#if !MAXN
	size_t oldsize;
	short *oldpos;

	oldsize = vmark1_sz;
	oldpos = vmark1;
	DYNALLOC1(short,vmark1,vmark1_sz,nn,"preparemarks");
	if (vmark1_sz != oldsize || vmark1 != oldpos) vmark1_val = 32000;
#endif
}

static void
preparemarks2(size_t nn)
{
#if !MAXN
	size_t oldsize;
	short *oldpos;

	oldsize = vmark2_sz;
	oldpos = vmark2;
	DYNALLOC1(short,vmark2,vmark2_sz,nn,"preparemarks");
	if (vmark2_sz != oldsize || vmark2 != oldpos) vmark2_val = 32000;
#endif
}

/*****************************************************************************
*                                                                            *
*  isautom_sg(g,perm,digraph,m,n) = TRUE iff perm is an automorphism of g    *
*  (i.e., g^perm = g).  Symmetry is assumed unless digraph = TRUE.           *
*                                                                            *
*****************************************************************************/

boolean
isautom_sg(graph *g, permutation *p, boolean digraph, int m, int n)
{
	int *v,*d,*e;
	int i,j,pi,di;
	int vi,vpi;

	SG_VDE(g,v,d,e);

	PREPAREMARKS1(n);

	for (i = 0; i < n; ++i)
	if (p[i] != i || digraph)
	{
	    pi = p[i];
	    di = d[i];
	    if (d[pi] != di) return FALSE;

	    vi = v[i];
	    vpi = v[pi];
	    RESETMARKS1;
	    for (j = 0; j < di; ++j)
		MARK1(p[e[vi+j]]);
	    for (j = 0; j < di; ++j)
		if (ISNOTMARKED1(e[vpi+j]))
		    return FALSE;
	}

	return TRUE;
}

/*****************************************************************************
*                                                                            *
* aresame_sg(g1,g2) = TRUE iff g1 and g2 are identical as labelled digraphs  *
*                                                                            *
*****************************************************************************/

boolean
aresame_sg(sparsegraph *g1, sparsegraph *g2)
{
	int *v1,*d1,*e1;
	int *v2,*d2,*e2;
	int n,i,j,di;
	int vi;

	n = g1->nv;
	if (g2->nv != n || g2->nde != g1->nde) return FALSE;

	SG_VDE(g1,v1,d1,e1);
	SG_VDE(g2,v2,d2,e2);

	PREPAREMARKS1(n);

	for (i = 0; i < n; ++i)
	{
	    di = d1[i];
	    if (d2[i] != di) return FALSE;

	    vi = v1[i];
	    RESETMARKS1;
	    for (j = 0; j < di; ++j)
		MARK1(e1[vi+j]);
	    vi = v2[i];
	    for (j = 0; j < di; ++j)
		if (ISNOTMARKED1(e2[vi+j]))
	    	    return FALSE;
	}

	return TRUE;
}

/*****************************************************************************
*                                                                            *
*  testcanlab_sg(g,canong,lab,samerows,m,n) compares g^lab to canong,        *
*  using an ordering which is immaterial since it's only used here.  The     *
*  value returned is -1,0,1 if g^lab <,=,> canong.  *samerows is set to      *
*  the number of rows (0..n) of canong which are the same as those of g^lab. *
*                                                                            *
*****************************************************************************/

int
testcanlab_sg(graph *g, graph *canong, int *lab, int *samerows, int m, int n)
{
	int *v,*d,*e;
	int *cv,*cd,*ce;
	int i,j,di,dli;
	int vi,vli,k;
	int mina;

        SG_VDE(g,v,d,e);
	SG_VDE(canong,cv,cd,ce);

#if !MAXN
	DYNALLOC1(shortish,work1,work1_sz,n,"testcanlab_sg");
#endif
#define INVLAB work1

	PREPAREMARKS1(n);

	for (i = 0; i < n; ++i) INVLAB[lab[i]] = i;

	for (i = 0; i < n; ++i)
	{
         /* compare g[lab[i]]^INVLAB to canong[i] */
	    vi = cv[i];
	    di = cd[i];
	    vli = v[lab[i]];
	    dli = d[lab[i]];

	    if (di != dli)
	    {
		*samerows = i;
	        if (di < dli) return -1;
		return 1;
	    }

	    RESETMARKS1;
	    mina = n;
	    for (j = 0; j < di; ++j)
		MARK1(ce[vi+j]);
	    for (j = 0; j < di; ++j)
	    {
		k = INVLAB[e[vli+j]];
		if (ISMARKED1(k))  UNMARK1(k);
		else if (k < mina) mina = k;
	    }
	    if (mina != n)
	    {
		*samerows = i;
	        for (j = 0; j < di; ++j)
	        {
		    k = ce[vi+j];
		    if (ISMARKED1(k) && k < mina) return -1;
	        }
	        return 1;
	    }
	}

	*samerows = n;
	return 0;
}

/*****************************************************************************
*                                                                            *
*  updatecan_sg(g,canong,lab,samerows,m,n) sets canong = g^lab, assuming     *
*  the first samerows vertices of canong are ok already.  Also assumes       *
*  contiguity and ample space in canong.                                     *
*                                                                            *
*****************************************************************************/

void
updatecan_sg(graph *g, graph *canong, permutation *lab,
                                               int samerows, int m, int n)
{
	int *v,*d,*e;
	int *cv,*cd,*ce;
	int i,j;
	int vli,dli,k;

	SG_VDE(g,v,d,e);
	SG_VDE(canong,cv,cd,ce);

#if !MAXN
	DYNALLOC1(shortish,work1,work1_sz,n,"testcanlab_sg");
#endif
#define INVLAB work1

	PREPAREMARKS1(n);

	((sparsegraph*)canong)->nv = n;
	((sparsegraph*)canong)->nde = ((sparsegraph*)g)->nde;

	for (i = 0; i < n; ++i) INVLAB[lab[i]] = i;

	if (samerows == 0) k = 0;
	else               k = cv[samerows-1]+cd[samerows-1];

	for (i = samerows; i < n; ++i)
	{
	    cv[i] = k;
	    cd[i] = dli = d[lab[i]];
	    vli = v[lab[i]];
	    for (j = 0; j < dli; ++j)
		ce[k++] = INVLAB[e[vli+j]];
	}
}

/*****************************************************************************
*                                                                            *
*  sortindirect(x,n,z) - sort x[0..n-1] according to z[x[i]] values          *
*                                                                            *
*****************************************************************************/

static void
sortindirect(int *x, int n, shortish *z)
{
    int i,j,h,xi;
    shortish iw;

    j = n / 3;
    h = 1;
    do
        h = 3 * h + 1;
    while (h < j);

    do
    {
        for (i = h; i < n; ++i)
        {
	    xi = x[i];
            iw = z[xi];
            for (j = i; z[x[j-h]] > iw; )
            {
                x[j] = x[j-h];
                if ((j -= h) < h) break;
            }
            x[j] = xi;
        }
        h /= 3;
    }
    while (h > 0);
}

/*****************************************************************************
*                                                                            * 
*  sortshortish(x,n) - sort x[0..n-1] according to numerical values          *
*                                                                            *
*****************************************************************************/

static void
sortshortish(shortish *x, int n)
{
    int i,j,h;
    shortish xi;

    j = n / 3;
    h = 1;
    do
        h = 3 * h + 1;
    while (h < j);

    do
    {
        for (i = h; i < n; ++i)
        {
	    xi = x[i];
            for (j = i; x[j-h] > xi; )
            {
                x[j] = x[j-h];
                if ((j -= h) < h) break;
            }
            x[j] = xi;
        }
        h /= 3;
    }
    while (h > 0);
}

/*****************************************************************************
*                                                                            * 
*  sortints(x,n) - sort x[0..n-1] according to numerical values              *
*                                                                            *
*****************************************************************************/

static void
sortints(int *x, int n)
{
    int i,j,h;
    int xi;

    j = n / 3;
    h = 1;
    do
        h = 3 * h + 1;
    while (h < j);

    do
    {
        for (i = h; i < n; ++i)
        {
	    xi = x[i];
            for (j = i; x[j-h] > xi; )
            {
                x[j] = x[j-h];
                if ((j -= h) < h) break;
            }
            x[j] = xi;
        }
        h /= 3;
    }
    while (h > 0);
}

/*****************************************************************************
*                                                                            *
*  init_sg(graph *gin, graph **gout, graph *hin, graph **hout,               *
*          int *lab, int *ptn, set *active, optionblk *options,              *
*          int *status, int m, int n)                                       *
*  Initialse routine for dispatch vector.  This one just makes sure          *
*  that *hin has enough space.                                               *
*                                                                            *
*****************************************************************************/

void
init_sg(graph *gin, graph **gout, graph *hin, graph **hout, int *lab,
	int *ptn, set *active, struct optionstruct *options, int *status,
	int m, int n)
{
    	sparsegraph *sg,*sh;

	if (options->getcanon)
	{
	    sg = (sparsegraph*)gin;
	    sh = (sparsegraph*)hin;
	    SG_ALLOC(*sh,sg->nv,sg->nde,"init_sg");
	}
	*status = 0;
}

/*****************************************************************************
*                                                                            *
*  distvals(sparsegraph *sg, int v0, shortish *dist, int n) sets dist[i]     *
*  to the distance from v0 to i, for each i, or to n if there is no such     *
*  distance.  work4[] is used as a queue.                                    *
*                                                                            *
*****************************************************************************/

void
distvals(sparsegraph *g, int v0, shortish *dist, int n)
{
	int *v,*d,*e;
	int i,head,tail;
	int vi,di,j,k;

	SG_VDE(g,v,d,e);
#if !MAXN
	DYNALLOC1(shortish,work4,work4_sz,n,"distvals");
#endif
#define QUEUE work4

	for (i = 0; i < n; ++i) dist[i] = n;

	QUEUE[0] = v0;
	dist[v0] = 0;

	head = 0;
	tail = 1;
	while (tail < n && head < tail)
	{
	    i = QUEUE[head++];
	    vi = v[i];
	    di = d[i];
	    for (j = 0; j < di; ++j)
	    {
		k = e[vi+j];
		if (dist[k] == n)
		{
		    dist[k] = dist[i] + 1;
		    QUEUE[tail++] = k;
		}
	    }
	}
}

/*****************************************************************************
*                                                                            *
*  refine_sg(g,lab,ptn,level,numcells,count,active,code,m,n) performs a      *
*  refinement operation on the partition at the specified level of the       *
*  partition nest (lab,ptn).  *numcells is assumed to contain the number of  *
*  cells on input, and is updated.  The initial set of active cells (alpha   *
*  in the paper) is specified in the set active.  Precisely, x is in active  *
*  iff the cell starting at index x in lab is active.                        *
*  The resulting partition is equitable if active is correct (see the paper  *
*  and the Guide).                                                           *
*  *code is set to a value which depends on the fine detail of the           *
*  algorithm, but which is independent of the labelling of the graph.        *
*  count is used for work space.                                             *
*                                                                            *
*****************************************************************************/

void
refine_sg(graph *g, int *lab, int *ptn, int level, int *numcells,
       permutation *count, set *active, int *code, int m, int n)
{
	int i,j,k,l,v1,v2,v3,isplit;
	shortish w1,w2,w3;
	long longcode;
	int *v,*d,*e;
	int size,bigsize,bigpos;
	int nactive,hitcells;
	int lj,vi,di,splitv;
	boolean trivsplit;

	SG_VDE(g,v,d,e);

#if !MAXN
	DYNALLOC1(shortish,work1,work1_sz,n,"refine_sg");
	DYNALLOC1(shortish,work2,work2_sz,n,"refine_sg");
	DYNALLOC1(shortish,work3,work3_sz,n,"refine_sg");
	DYNALLOC1(shortish,work4,work4_sz,n,"refine_sg");
#endif
#define CELLSTART work1
#define ACTIVE    work2
#define HITS      work3
#define HITCELL   work4

	PREPAREMARKS1(n);
	PREPAREMARKS2(n);

	longcode = *numcells;

     /* Set ACTIVE[0..nactive-1] = queue of active cell starts */

	nactive = 0;
        for (i = -1; (i = nextelement(active,m,i)) >= 0;)
	    ACTIVE[nactive++] = i;

	if (nactive == 0)
	{
	    *code = CLEANUP(longcode);
	    return;
	}

     /* Set CELLSTART[i] = starting point in lab[] of nontrivial cell
        containing i, or n if i is a singleton */

	for (i = 0; i < n; )
	{
	 /* Just here, i is a cell starting position */
	    if (ptn[i] <= level)
	    {
		CELLSTART[lab[i]] = n;
	        ++i;
	    }
	    else
	    {
		j = i;
		do
		{
		    CELLSTART[lab[i]] = j;
		} while (ptn[i++] > level);
	    }
	}

	if (level <= 2 && nactive == 1 && ptn[ACTIVE[0]] <= level
		       && *numcells <= n/8)
	{
	    isplit = ACTIVE[--nactive];
	    DELELEMENT(active,isplit);
    
	    distvals((sparsegraph*)g,lab[isplit],HITS,n);

	    for (v1 = 0; v1 < n; )
	    {
		if (ptn[v1] <= level)
		{
		    ++v1;
		    continue;
		}

		longcode = MASH(longcode,v1);
		w1 = HITS[lab[v1]];

		v2 = v1+1;
		while (ptn[v2-1] > level && HITS[lab[v2]] == w1) ++v2;

		if (ptn[v2-1] <= level)
		{
		    v1 = v2;
		    continue;
		}

		w2 = NAUTY_INFINITY;
		v3 = j = v2;

		do
		{
		    lj = lab[j];
		    w3 = HITS[lj];
		    if (w3 == w1)
		    {
		        lab[j] = lab[v3];
			lab[v3] = lab[v2];
			lab[v2] = lj;
			++v2;
			++v3;
		    }
		    else if (w3 == w2)
		    {
			lab[j] = lab[v3];
			lab[v3] = lj;
			++v3;
		    }
		    else if (w3 < w1)
		    {
			lab[j] = lab[v2];
			lab[v2] = lab[v1];
			lab[v1] = lj;
			v3 = v2 + 1;
			v2 = v1 + 1;
			w2 = w1;
			w1 = w3;
		    }
		    else if (w3 < w2)
		    {
			lab[j] = lab[v2];
			lab[v2] = lj;
			v3 = v2 + 1;
			w2 = w3;
		    }
		} while (ptn[j++] > level);
    
		longcode = MASH(longcode,w2);
		longcode = MASH(longcode,v2);
		if (j != v2)   /* At least two fragments
				    * v1..v2-1 = w1; v2..v3-1 = w2  */
		{
		    if (v2 == v1+1)
			CELLSTART[lab[v1]] = n;
    
		    if (v3 == v2+1)
			CELLSTART[lab[v2]] = n;
		    else
		        for (k = v2; k < v3; ++k)
			    CELLSTART[lab[k]] = v2;
		    ++*numcells;
		    ptn[v2-1] = level;
    
		    if (j == v3)
		    {
		     /* Two fragments only */
			if (v2-v1 <= v3-v2 && !ISELEMENT(active,v1))
			{
			    ADDELEMENT(active,v1);
			    ACTIVE[nactive++] = v1;
		        }
			else
			{
			    ADDELEMENT(active,v2);
			    ACTIVE[nactive++] = v2;
			}
		    }
		    else 
		    {
		     /* Extra fragments: v3..j-1 > w2 */
		        sortindirect(lab+v3,j-v3,HITS);
		        ACTIVE[nactive++] = v2;
			ADDELEMENT(active,v2);
		        if (v2-v1 >= v3-v2)
		        {
		            bigpos = -1;
			    bigsize = v2-v1;
		        }
		        else
		        {
			    bigpos = nactive-1;
			    bigsize = v3-v2;
		        }
			for (k = v3-1; k < j-1;)
			{
			    ptn[k] = level;
			    longcode = MASH(longcode,k);
			    ++*numcells;
			    l = k+1;
			    ADDELEMENT(active,l);
			    ACTIVE[nactive++] = l;
			    w3 = HITS[lab[l]];
			    for (k = l; k < j-1
                                        && HITS[lab[k+1]] == w3; ++k)
				CELLSTART[lab[k+1]] = l;
			    size = k-l+1;
			    if (size == 1)
				CELLSTART[lab[l]] = n;
			    else
			    {
				CELLSTART[lab[l]] = l;
				if (size > bigsize)
				{
				    bigsize = size;
				    bigpos = nactive-1;
				}
			    }
			}
    
		        if (bigpos >= 0 && !ISELEMENT(active,v1))
		        {
			    longcode = MASH(longcode,bigpos);
			    DELELEMENT(active,ACTIVE[bigpos]);
			    ADDELEMENT(active,v1);
			    ACTIVE[bigpos] = v1;
		        }
		    }
		}
	        v1 = j;
	    }
	}

     /* Iterate until complete */
	while (nactive > 0 && *numcells < n)
	{
	    for (i = 0; i < nactive && i < 10; ++i)
		if (ptn[ACTIVE[i]] <= level) break;

	    if (i < nactive && i < 10)
	    {
		trivsplit = TRUE;
		isplit = ACTIVE[i];
		ACTIVE[i] = ACTIVE[--nactive];
	    }
	    else
	    {
		isplit = ACTIVE[--nactive];
		trivsplit = ptn[isplit] <= level;
	    }

	    DELELEMENT(active,isplit);
	    longcode = MASH(longcode,isplit);
    
	    if (trivsplit)
	    {
		RESETMARKS1;
		RESETMARKS2;
		hitcells = 0;
		splitv = lab[isplit];
		vi = v[splitv];
		di = d[splitv];
		for (i = 0; i < di; ++i)
		{
		    j = e[vi+i];
		    MARK2(j);
		    k = CELLSTART[j];
		    if (k != n && ISNOTMARKED1(k))
		    {
			MARK1(k);
			HITCELL[hitcells++] = k;
		    }
		}

		if (hitcells > 1) sortshortish(HITCELL,hitcells);

	     /* divide cells according to which vertices are hit */

		for (i = 0; i < hitcells; ++i)
		{
		    j = v1 = v2 = HITCELL[i];
		    k = 0;
		    do
		    {
			lj = lab[j];
			if (ISMARKED2(lj))
			    HITS[k++] = lj;
			else
			    lab[v2++] = lj;
		    } while (ptn[j++] > level);

	            longcode = MASH(longcode,k);
		    v3 = v2;
		    while (--k >= 0)
		    {
			j = HITS[k];
			CELLSTART[j] = v2;
			lab[v3++] = j;
		    }

		    if (v2 != v3 && v2 != v1)
		    {
			++*numcells;
			if (v2 == v1+1) CELLSTART[lab[v1]] = n;
			if (v3 == v2+1) CELLSTART[lab[v2]] = n;
			ptn[v2-1] = level;
	                longcode = MASH(longcode,v2);
			if (v2-v1 <= v3-v2 && !ISELEMENT(active,v1))
			{
			    ADDELEMENT(active,v1);
			    ACTIVE[nactive++] = v1;
		        }
			else
			{
			    ADDELEMENT(active,v2);
			    ACTIVE[nactive++] = v2;
			}
		    }
		}
	    }
	    else  /* non-trivial splitting */
	    {
	     /* isplit is the start of the splitting cell.
	        Set HITS[i] = hits of i for i in non-trivial cells,
	        HITCELL[0..hitcells-1] = starts of hit non-trivial cells */

	        RESETMARKS1;
	        hitcells = 0;
	        do
	        {
		    vi = v[lab[isplit]];
		    di = d[lab[isplit]];
		    for (i = 0; i < di; ++i)
		    {
		        j = e[vi+i];
		        k = CELLSTART[j];
		        if (k != n)
		        {
			    if (ISNOTMARKED1(k))
		            {
			        MARK1(k);
			        HITCELL[hitcells++] = k;
			        do
			        {
			            HITS[lab[k]] = 0;
		 	        } while (ptn[k++] > level);
		            }
		            ++HITS[j];
		        }
		    }
	        } while (ptn[isplit++] > level);
    
	        if (hitcells > 1) sortshortish(HITCELL,hitcells);
    
	     /* divide cells according to hit counts */
    
	        longcode = MASH(longcode,hitcells);
	        for (i = 0; i < hitcells; ++i)
	        {
		    v1 = HITCELL[i];
		    w1 = HITS[lab[v1]];

		    v2 = v1+1;
		    while (ptn[v2-1] > level && HITS[lab[v2]] == w1) ++v2;

		    if (ptn[v2-1] <= level) continue;
		    w2 = NAUTY_INFINITY;
		    v3 = j = v2;
    
		    do
		    {
		        lj = lab[j];
		        w3 = HITS[lj];
		        if (w3 == w1)
		        {
			    lab[j] = lab[v3];
			    lab[v3] = lab[v2];
			    lab[v2] = lj;
			    ++v2;
			    ++v3;
		        }
		        else if (w3 == w2)
		        {
			    lab[j] = lab[v3];
			    lab[v3] = lj;
			    ++v3;
		        }
		        else if (w3 < w1)
		        {
			    lab[j] = lab[v2];
			    lab[v2] = lab[v1];
			    lab[v1] = lj;
			    v3 = v2 + 1;
			    v2 = v1 + 1;
			    w2 = w1;
			    w1 = w3;
		        }
		        else if (w3 < w2)
		        {
			    lab[j] = lab[v2];
			    lab[v2] = lj;
			    v3 = v2 + 1;
			    w2 = w3;
		        }
		    } while (ptn[j++] > level);
    
	            longcode = MASH(longcode,w1);
	            longcode = MASH(longcode,v2);
		    if (j != v2)   /* At least two fragments
				    * v1..v2-1 = w1; v2..v3-1 = w2  */
		    {
		        if (v2 == v1+1)
			    CELLSTART[lab[v1]] = n;
    
		        if (v3 == v2+1)
			    CELLSTART[lab[v2]] = n;
		        else
		            for (k = v2; k < v3; ++k)
			        CELLSTART[lab[k]] = v2;
		        ++*numcells;
		        ptn[v2-1] = level;
    
		        if (j == v3)
		        {
		         /* Two fragments only */
			    if (v2-v1 <= v3-v2 && !ISELEMENT(active,v1))
			    {
			        ADDELEMENT(active,v1);
			        ACTIVE[nactive++] = v1;
		            }
			    else
			    {
			        ADDELEMENT(active,v2);
			        ACTIVE[nactive++] = v2;
			    }
		        }
		        else 
		        {
		         /* Extra fragments: v3..j-1 > w2 */
	            	    longcode = MASH(longcode,v3);
		            sortindirect(lab+v3,j-v3,HITS);
		            ACTIVE[nactive++] = v2;
			    ADDELEMENT(active,v2);
		            if (v2-v1 >= v3-v2)
		            {
		                bigpos = -1;
			        bigsize = v2-v1;
		            }
		            else
		            {
			        bigpos = nactive-1;
			        bigsize = v3-v2;
	            		longcode = MASH(longcode,bigsize);
		            }
			    for (k = v3-1; k < j-1;)
			    {
			        ptn[k] = level;
			        ++*numcells;
			        l = k+1;
			        ADDELEMENT(active,l);
			        ACTIVE[nactive++] = l;
			        w3 = HITS[lab[l]];
	            		longcode = MASH(longcode,w3);
			        for (k = l; k < j-1
                                            && HITS[lab[k+1]] == w3; ++k)
				    CELLSTART[lab[k+1]] = l;
			        size = k-l+1;
			        if (size == 1)
				    CELLSTART[lab[l]] = n;
			        else
			        {
				    CELLSTART[lab[l]] = l;
				    if (size > bigsize)
				    {
				        bigsize = size;
				        bigpos = nactive-1;
				    }
			        }
			    }
    
		            if (bigpos >= 0 && !ISELEMENT(active,v1))
		            {
			        DELELEMENT(active,ACTIVE[bigpos]);
			        ADDELEMENT(active,v1);
			        ACTIVE[bigpos] = v1;
		            }
		        }
		    }
		}
	    }
	}

	longcode = MASH(longcode,*numcells);
	*code = CLEANUP(longcode);
}

/*****************************************************************************
*                                                                            *
*  cheapautom_sg(ptn,level,digraph,n) returns TRUE if the partition at the   *
*  specified level in the partition nest (lab,ptn) {lab is not needed here}  *
*  satisfies a simple sufficient condition for its cells to be the orbits of *
*  some subgroup of the automorphism group.  Otherwise it returns FALSE.     *
*  It always returns FALSE if digraph!=FALSE.                                *
*                                                                            *
*  nauty assumes that this function will always return TRUE for any          *
*  partition finer than one for which it returns TRUE.                       *
*                                                                            *
*****************************************************************************/

boolean
cheapautom_sg(int *ptn, int level, boolean digraph, int n)
{
	int i,k,nnt;

	if (digraph) return FALSE;

	k = n;
	nnt = 0;
	for (i = 0; i < n; ++i)
	{
	    --k;
	    if (ptn[i] > level)
	    {
	        ++nnt;
	        while (ptn[++i] > level) {}
	    }
	}

	return (k <= nnt + 1 || k <= 4);
}

/*****************************************************************************
*                                                                            *
*  bestcell_sg(g,lab,ptn,level,tc_level,m,n) returns the index in lab of     *
*  the start of the "best non-singleton cell" for fixing.  If there is no    *
*  non-singleton cell it returns n.                                          *
*  This implementation finds the first cell which is non-trivially joined    *
*  to the greatest number of other cells, assuming equitability.             *
*  This is not good for digraphs!                                            *
*                                                                            *
*****************************************************************************/

static int
bestcell_sg(graph *g, int *lab, int *ptn, int level,
                                              int tc_level, int m, int n)
{
	int nnt;
	int *v,*d,*e;
	int i,j,k,vi,di;
	shortish *work1b;
	int maxcnt;

	SG_VDE(g,v,d,e);

#if !MAXN 
	DYNALLOC1(shortish,work1,work1_sz,n,"bestcell_sg"); 
	DYNALLOC1(shortish,work2,work2_sz,n,"bestcell_sg"); 
	DYNALLOC1(shortish,work3,work3_sz,n,"bestcell_sg"); 
	DYNALLOC1(shortish,work4,work4_sz,n,"bestcell_sg"); 
#endif
	work1b = work1 + (n/2);
#define START    work1
#define SIZE     work1b
#define NNTCELL  work2
#define HITS     work3
#define COUNT    work4

   /* find non-singleton cells: put starts in START[0..nnt-1],
      sizes in SIZE[0..nnt-1].
      Also NNTCELL[i] = n if {i} is a singelton, else index of
      nontriv cell containing i. */

	i = nnt = 0;

	while (i < n)
	{
	    if (ptn[i] > level)
	    {
	        START[nnt] = i;
		j = i;
		do
		    NNTCELL[lab[j]] = nnt;
		while (ptn[j++] > level);
		SIZE[nnt] = j-i;
		++nnt;
	        i = j;
	    }
	    else
	    {
		NNTCELL[lab[i]] = n;
		++i;
	    }
	}

	if (nnt == 0) return n;

     /* set COUNT[i] to # non-trivial neighbours of n.s. cell i */

	for (i = 0; i < nnt; ++i) HITS[i] = COUNT[i] = 0;

	for (i = 0; i < nnt; ++i)
	{
	    vi = v[lab[START[i]]];
	    di = d[lab[START[i]]];

	    for (j = 0; j < di; ++j)
	    {
		k = NNTCELL[e[vi+j]];
		if (k != n) ++HITS[k];
	    }
	    for (j = 0; j < di; ++j)
	    {
		k = NNTCELL[e[vi+j]];
		if (k != n)
		{
		    if (HITS[k] > 0 && HITS[k] < SIZE[k]) ++COUNT[i];
		    HITS[k] = 0;
		}
	    }
	}

     /* find first greatest bucket value */

	j = 0;
	maxcnt = COUNT[0];
	for (i = 1; i < nnt; ++i)
	    if (COUNT[i] > maxcnt)
	    {
	        j = i;
	        maxcnt = COUNT[i];
	    }

	return (int)START[j];
}
/*****************************************************************************
*                                                                            *
*  targetcell_sg(g,lab,ptn,level,tc_level,digraph,hint,m,n) returns the      *
*  index in lab of the next cell to split.                                   *
*  hint is a suggestion for the answer, which is obeyed if it is valid.      *
*  Otherwise we use bestcell() up to tc_level and the first non-trivial      *
*  cell after that.                                                          *
*                                                                            *
*****************************************************************************/

int
targetcell_sg(graph *g, int *lab, int *ptn, int level, int tc_level,
           boolean digraph, int hint, int m, int n)
{
        int i;

        if (hint >= 0 && ptn[hint] > level &&
                         (hint == 0 || ptn[hint-1] <= level))
            return hint;
        else if (level <= tc_level)
            return bestcell_sg(g,lab,ptn,level,tc_level,m,n);
        else
        {
            for (i = 0; i < n && ptn[i] <= level; ++i) {}
            return (i == n ? 0 : i);
        }
}

/*****************************************************************************
*                                                                            *
*  sortlists_sg(g) sorts the adjacency lists into numerical order            *
*                                                                            *
*****************************************************************************/

void
sortlists_sg(sparsegraph *g)
{
	int *v,*d,*e;
	int n,i;

	SG_VDE(g,v,d,e);
	n = g->nv;

	for (i = 0; i < n; ++i)
	    if (d[i] > 1) sortints(e+v[i],d[i]);
}

/*****************************************************************************
*                                                                            *
*  put_sg(f,sg,digraph,linelength) writes the sparse graph to file f using   *
*  at most linelength characters per line.  If digraph then all directed     *
*  edges are written; else one v-w for w>=v is written.                      *
*                                                                            *
*****************************************************************************/

void
put_sg(FILE *f, sparsegraph *sg, boolean digraph, int linelength)
{
    	int *v,*d,*e;
	int n,vi,di;
    	int i,j,curlen,slen;
	char s[12];

	SG_VDE(sg,v,d,e);
	n = sg->nv;

	for (i = 0; i < n; ++i)
	{
	    vi = v[i];
	    di = d[i];
	    if (di == 0) continue;
	    slen = itos(i+labelorg,s);
	    putstring(f,s);
	    putstring(f," :");
	    curlen = slen + 2;

	    for (j = 0; j < di; ++j)
	    {
		if (!digraph && e[vi+j] < i) continue;
		slen = itos(e[vi+j]+labelorg,s);
		if (linelength && curlen + slen + 1 >= linelength)
		{
		    putstring(f,"\n ");
		    curlen = 2;
		}
		PUTC(' ',f);
		putstring(f,s);
		curlen += slen + 1;
	    }
	    PUTC('\n',f);
	}
}

/*****************************************************************************
*                                                                            *
*  sg_to_nauty(sg,g,reqm,&m) creates a nauty-format graph from a sparse      *
*  graph.  reqm is the required m value (computed from n if reqm=0), and     *
*  m is the actual value used.  g is dynamically generated if NULL is given. *
*  A pointer to g is returned.                                               *
*                                                                            *
*****************************************************************************/

graph*
sg_to_nauty(sparsegraph *sg, graph *g, int reqm, int *pm)
{
	int *v,*d,*e;
	int m,n,i,j,di;
	int vi;
	set *gi;

	SG_VDE(sg,v,d,e);
	n = sg->nv;
	if (reqm != 0 && reqm*WORDSIZE < n)
	{
	    fprintf(ERRFILE,"sg_to_nauty: reqm is impossible\n");
	    exit(1);
	}

	if (reqm != 0) m = reqm;
	else           m = (n+WORDSIZE-1)/WORDSIZE;

	*pm = m;

	if (g == NULL)
	{
	    if ((g = (graph*)ALLOCS(n,m*sizeof(graph))) == NULL)
	    {
                fprintf(ERRFILE,"sg_to_nauty: malloc failed\n");
                exit(1);
            }
	}

	for (i = 0, gi = g; i < n; ++i, gi += m)
	{
	    vi = v[i];
	    di = d[i];
	    EMPTYSET(gi,m);
	    for (j = 0; j < di; ++j) ADDELEMENT(gi,e[vi+j]);
	}

	return g;
}

/*****************************************************************************
*                                                                            *
*  nauty_to_sg(g,m,n) creates a sparse graph from a nauty format graph       *
*  If sg is not NULL, it is assumed that the vlen,dlen,elen fields are       *
*  correct and v,d,e are dynamically allocated (or NULL); they are           *
*  reallocated if necessary.  If sg==NULL, a new structure is allocated.     *
*  A pointer to the sparse graph is returned.                                *
*                                                                            *
*****************************************************************************/

sparsegraph*
nauty_to_sg(graph *g, sparsegraph *sg, int m, int n)
{
	int *v,*d,*e;
	int i,j,k;
	int di,nde;
	long l;
	set *gi;

	if (!sg)
	{
	    if ((sg = (sparsegraph*)ALLOCS(1,sizeof(sparsegraph))) == NULL)
	    {
		fprintf(ERRFILE,"nauty_to_sg: malloc failed\n");
		exit(1);
	    }
	    SG_INIT(*sg);
	}

	nde = 0;
	for (l = m*1L*n; --l >= 0; )
	    if (g[l] != 0) nde += POPCOUNT(g[l]);

	sg->nv = n;
	sg->nde = nde;

	SG_ALLOC(*sg,n,nde,"nauty_to_sg");

	SG_VDE(sg,v,d,e);

	j = 0;
	for (i = 0, gi = g; i < n; ++i, gi += m)
	{
	    v[i] = j;
	    di = 0;
	    for (k = -1; (k = nextelement(gi,m,k)) >= 0; )
		e[j++] = k;
	    d[i] = j - v[i];
	}

	return sg;
}

/*****************************************************************************
*                                                                            *
*  distances_sg() assigns to each vertex v a value depending on the number   *
*  of vertices at each distance from v, and what cells they lie in.          *
*  If we find any cell which is split in this manner, we don't try any       *
*  further cells.                                                            *
*                                                                            *
*****************************************************************************/

void
distances_sg(graph *g, int *lab, int *ptn, int level, int numcells, int tvpos,
	     permutation *invar, int invararg, boolean digraph, int m, int n)
{
        int *v,*d,*e;
	int i,j,k,dlim,wt;
	int vi,di;
	int cell1,cell2,iv,liv,kcode;
	int head,tail;
	long longcode;
	boolean success;

	SG_VDE(g,v,d,e);

#if !MAXN
	DYNALLOC1(shortish,work1,work1_sz,n,"distances_sg");
	DYNALLOC1(shortish,work4,work4_sz,n,"distances_sg");
	DYNALLOC1(shortish,work3,work3_sz,n,"distances_sg");
#endif
#define CELLCODE work1
#define QUEUE work4
#define DIST work3

        for (i = n; --i >= 0;) invar[i] = 0;

        wt = 1;
        for (i = 0; i < n; ++i)
        {
	    CELLCODE[lab[i]] = FUZZ1(wt);
	    if (ptn[i] <= level) ++wt;
        }

        if (invararg > n || invararg == 0) dlim = n;
        else                               dlim = invararg+1;

        success = FALSE;
        for (cell1 = 0; cell1 < n; cell1 = cell2 + 1)
        {
	    for (cell2 = cell1; ptn[cell2] > level; ++cell2) {}
	    if (cell2 == cell1) continue;

	    for (iv = cell1; iv <= cell2; ++iv)
	    {
		liv = lab[iv];
	        QUEUE[0] = liv;
		DIST[liv] = 0;
		RESETMARKS1;
		MARK1(liv);
		longcode = 0;
		head = 0;
		tail = 1;
	        
	        while (tail < n && head < tail)
	        {
		    i = QUEUE[head++];
		    if (DIST[i] >= dlim) break;
		    vi = v[i];
		    di = d[i];

		    for (j = 0; j < di; ++j)
		    {
			k = e[vi+j];
			if (ISNOTMARKED1(k))
			{
			    MARK1(k);
			    DIST[k] = DIST[i] + 1;
			    kcode = DIST[k]+CELLCODE[k];
			    ACCUM(longcode,FUZZ1(kcode));
			    QUEUE[tail++] = k;
			}
		    }
	        }
		invar[liv] = CLEANUP(longcode);
	        if (invar[liv] != invar[lab[cell1]]) success = TRUE;
	    }
	    if (success) break;
        }
}

/*****************************************************************************
*                                                                            *
*  adjacencies_sg() assigns to each vertex v a code depending on which cells *
*  it is joined to and from, and how many times.  It is intended to provide  *
*  better partitioning that the normal refinement routine for digraphs.      *
*  It will not help with undirected graphs in nauty at all.                  *
*                                                                            *
*****************************************************************************/

void
adjacencies_sg(graph *g, int *lab, int *ptn, int level, int numcells,
               int tvpos, permutation *invar, int invararg, boolean digraph,
               int m, int n)
{
        int *v,*d,*e;
        shortish vwt,wwt;
	int *ei,di,i,j;

	SG_VDE(g,v,d,e);

#if !MAXN
	DYNALLOC1(shortish,work2,work2_sz,n,"adjacencies_sg");
#endif

	vwt = 1;
        for (i = 0; i < n; ++i)
        {
            work2[lab[i]] = vwt;
            if (ptn[i] <= level) ++vwt;
            invar[i] = 0;
        }

	for (i = 0; i < n; ++i)
	{
            vwt = FUZZ1(work2[i]);
            wwt = 0;
	    di = d[i];
	    ei = e + v[i];
	    for (j = 0; j < di; ++j)
	    {
                ACCUM(wwt,FUZZ2(work2[ei[j]]));
                ACCUM(invar[ei[j]],vwt);
            }
            ACCUM(invar[i],wwt);
        }
}

/*****************************************************************************
*                                                                            *
*  nausparse_check() checks that this file is compiled compatibly with the   *
*  given parameters.   If not, call exit(1).                                 *
*                                                                            *
*****************************************************************************/

void
nausparse_check(int wordsize, int m, int n, int version)
{
	if (wordsize != WORDSIZE)
	{
	    fprintf(ERRFILE,"Error: WORDSIZE mismatch in nausparse.c\n");
	    exit(1);
	}

#if MAXN
	if (m > MAXM)
	{
	    fprintf(ERRFILE,"Error: MAXM inadequate in nausparse.c\n");
	    exit(1);
	}

	if (n > MAXN)
	{
	    fprintf(ERRFILE,"Error: MAXN inadequate in nausparse.c\n");
	    exit(1);
	}
#endif

        if (version < NAUTYREQUIRED)
        {
            fprintf(ERRFILE,"Error: nausparse.c version mismatch\n");
            exit(1);
        }
}

/*****************************************************************************
*                                                                            *
*  nausparse_freedyn() - free the dynamic memory in this module              *
*                                                                            *
*****************************************************************************/

void
nausparse_freedyn(void)
{
#if !MAXN
	DYNFREE(vmark1,vmark1_sz);
	DYNFREE(vmark2,vmark2_sz);
        DYNFREE(work1,work1_sz);
        DYNFREE(work2,work2_sz);
        DYNFREE(work3,work3_sz);
        DYNFREE(work4,work4_sz);
#endif
}
