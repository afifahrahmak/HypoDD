#ifndef lint
static char rcsid[]="$Header: /home1/crhet/Afifah/HYPODD/ph2dt/RCS/atoangle.c,v 1.1 2017/07/13 21:03:41 Afifah Exp $";
#endif /* lint */

#include <stdio.h>
#include "compat.h"
#include "f77types.h"

/*
 * f77-callable interface to sscanf() function
 * Klewdgy version that allows three pointer arguments
 */
F77INT
sscanf3_(s, fmt, p1, p2, p3)
const	char	*s;
const	char	*fmt;
	GENPTR	p1, p2, p3;
{

	return sscanf(s, fmt, p1, p2, p3);
}
