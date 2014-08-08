Discussion
===========
+ Other graph databases exist with better "mathematical" abilities than ours 
   1. GraPHedron - makes sense of invariant constraints better
   2. Others 
	   + [http://cs.anu.edu.au/~bdm/data/](http://cs.anu.edu.au/~bdm/data/)  `*`
	   + [http://staffhome.ecm.uwa.edu.au/~00013890/remote/graphs/](http://staffhome.ecm.uwa.edu.au/~00013890/remote/graphs/)  `*`
	   + [http://www.mathe2.uni-bayreuth.de/markus/reggraphs.html](http://www.mathe2.uni-bayreuth.de/markus/reggraphs.html)   `*`
	   + [http://mathematica.stackexchange.com/questions/17775/how-to-view-all-graphs-available-in-graphdata](http://mathematica.stackexchange.com/questions/17775/how-to-view-all-graphs-available-in-graphdata)
	   + [http://cs.anu.edu.au/~bdm/data/graphs.html](http://cs.anu.edu.au/~bdm/data/graphs.html)
	   + [https://snap.stanford.edu/data/](https://snap.stanford.edu/data/) (too large for our current setup)
	
		These projects have computed all graphs (typically for larger n) with certain interesting properties 
+ Therefore our naive way of computing everything does not compete with existing databases in terms of mathematical usefulness. 
+ However, our novel contribution is putting them in a query-able database alongside their invariants. We should incorporate other project's graphs into our database. See `**` for the standard for storing large adjacency matrices, called "graph6" 
+ Add graph names when exist `***` 
+ We should make the database public and have users be able to submit graphs and perform queries online and download the results as text, images. eg, query by an invariant value, search by graph name, etc. 
+ We could expand the number of invariants used in the GraPHedron project. (I think they just have 3). Or let them do it using our data 
+ Users should be able to submit new graphs --> our db computes invariants (should have some sort of trigger event in the db to call python scripts) --> more data available to users! 
+ Have an indicator for which n are "completed" (contains all`****` graphs) 
+ This project lists a ton of graph invariants. We could add as many as we can
[http://www.emn.fr/z-info/sdemasse/gccat/sec4.3.4.html](http://www.emn.fr/z-info/sdemasse/gccat/sec4.3.4.html)
This catalog seems to give all/lots of the "forcing relations"!
http://www.emn.fr/z-info/sdemasse/gccat/sec4.3.4.2.html
+ can maybe use maple to compute some invariants, see "gpval module" and "cce module"
http://www.msci.memphis.edu/~speeds/idxcasgp.html


`*` cited by [house of graphs](http://www.sciencedirect.com.proxy-um.researchport.umd.edu/science/article/pii/S0166218X12002831#)

`**` Look into adopting [this](http://cs.anu.edu.au/~bdm/data/formats.html) [format](http://cs.anu.edu.au/~bdm/data/formats.txt) for representing graphs.  Allows for accommodation of large graphs, and seems to be more commonly used, so would be easier to accept submissions. 

`***` Add their names (if any) e.g. 

+ [http://www.graphclasses.org/smallgraphs.html](http://www.graphclasses.org/smallgraphs.html)
+ [http://en.wikipedia.org/wiki/Gallery_of_named_graphs](http://en.wikipedia.org/wiki/Gallery_of_named_graphs)
+ [http://www.sagemath.org/doc/reference/graphs/sage/graphs/graph_generators.html](http://www.sagemath.org/doc/reference/graphs/sage/graphs/graph_generators.html)


`****` Of course, need to define "all." ie n=1..10 for simple connected graphs is completed, so users know if they are getting everything or just what is available 







