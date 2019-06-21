# HypoDD
Relocate the hypocenters using double difference algorithm

Each subdirectory of this directory/Repo contains the source code for hypoDD
or one of the associated commands.

MAKING EXECUTABLE FILES
Each subdirectory contains a simple Makefile.  To compile and load a
program, just go to the appropriate directory and type

	make

It may be necessary to modify the Makefile slightly for different
compilers.  The versions given here support the GNU g77 compiler and
SUN's f77 compiler; comments indicate the changes needed for these.

The Makefiles can also be used to remove all files that can easily be
re-generated.  Type

	make clean

SYMBOLIC LINKS
Some sub-programs are used by more than one command.  In these cases,
only one file is provided and the other directories contain symbolic
links to it.
