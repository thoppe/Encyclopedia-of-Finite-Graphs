## Discussion


This is good, and says pretty much what I'd like to cover. Work it up into a few paragraphs and submit it. I've left my comments below.

+ Other graph databases exist with better "mathematical" abilities than ours 

+ GraPHedron - makes sense of invariant constraints better; 
+ We could expand the number of invariants used in the GraPHedron project. (I think they just have 3). Or let them do it using our data 

I don't want to the reader to be confused that the paper is all about GraPHedron, we mention it many times, but it is a small point that we can use it to extend their results. Since it has been mentioned before, we don't need to dwell on it.

+ [http://cs.anu.edu.au/~bdm/data/](http://cs.anu.edu.au/~bdm/data/) 

Good ref, add it part where refs 2,3 are.

+ [http://staffhome.ecm.uwa.edu.au/~00013890/remote/graphs/](http://staffhome.ecm.uwa.edu.au/~00013890/remote/graphs/)  `*`

This one doesn't load for me... *hmm, it loads for me..*

+ [http://www.mathe2.uni-bayreuth.de/markus/reggraphs.html](http://www.mathe2.uni-bayreuth.de/markus/reggraphs.html)   `*`

I think I ref. a paper that generates this, if not add it part where refs 2,3 are. *Yep, you're right, looks like it's brinkmann1996fast*

+ [http://mathematica.stackexchange.com/questions/17775/how-to-view-all-graphs-available-in-graphdata](http://mathematica.stackexchange.com/questions/17775/how-to-view-all-graphs-available-in-graphdata)

You want to add mathematica as a public database? It is commercial software so I'm not inclined to use it. *My point with these references is to show that if one wanted a list of graphs, there are better options than our encyclopedia*

+ [http://cs.anu.edu.au/~bdm/data/graphs.html](http://cs.anu.edu.au/~bdm/data/graphs.html)

Good ref, add it part where refs 2,3 are.

+ [https://snap.stanford.edu/data/](https://snap.stanford.edu/data/) (too large for our current setup)

Yes, see if you can work this ref. into the intro paragraph.

+ We should make the database public and have users be able to submit graphs and perform queries online and download the results as text, images. eg, query by an invariant value, search by graph name, etc. 

Database _is_ public, there will be a DOI for the code and a DOI for the database. This is one of our key features! *Oops, by "public" I meant to say online/live, going along with my next comment*

+ Users should be able to submit new graphs --> our db computes invariants (should have some sort of trigger event in the db to call python scripts)

For now, the DB is static and hosted on Zenodo. A non-static DB would be nice for the future (worth mentioning) but a static DB can be referenced. What _is_ mallable is the code - users can add new invariant code!

+ Therefore our naive way of computing everything does not compete with existing databases in terms of mathematical usefulness. 

Don't call it naive, call it exhasutive. Nor should we use "mathematical usefulness", try something along the lines of specificity - ours is general, theirs is specific. 

+ However, our novel contribution is putting them in a query-able database alongside their invariants. We should incorporate other project's graphs into our database. 

Yes, that is a future goal.

+ Add graph names when exist ; Add their names (if any) e.g. 
+ [http://www.graphclasses.org/smallgraphs.html](http://www.graphclasses.org/smallgraphs.html)
+ [http://en.wikipedia.org/wiki/Gallery_of_named_graphs](http://en.wikipedia.org/wiki/Gallery_of_named_graphs)
+ [http://www.sagemath.org/doc/reference/graphs/sage/graphs/graph_generators.html](http://www.sagemath.org/doc/reference/graphs/sage/graphs/graph_generators.html)

Maybe, that isn't a bad idea for named graphs. But this is a future project. Good idea!

+ Have an indicator for which n are "completed" (contains all`****` graphs) 

That could be handled in the graph "class" designation. For example, we could make a new class that only includes trees, or forests, or regular graphs, etc... The DB would contain "all" graphs of that class.

+ This project lists a ton of graph invariants. We could add as many as we can [http://www.emn.fr/z-info/sdemasse/gccat/sec4.3.4.html](http://www.emn.fr/z-info/sdemasse/gccat/sec4.3.4.html), This catalog seems to give all/lots of the "forcing relations"! http://www.emn.fr/z-info/sdemasse/gccat/sec4.3.4.2.html

Yes, this is good. When we mention GraPHedron we can also mention this. There should be a paper ref. this project too.

+ can maybe use maple to compute some invariants, see "gpval module" and "cce module" [http://www.msci.memphis.edu/~speeds/idxcasgp.html](http://www.msci.memphis.edu/~speeds/idxcasgp.html)

I'm still against using closed source software, of which MAPLE is. SAGE however could be mentioned.

+ `*` cited by [house of graphs](http://arxiv.org/abs/1204.3549)



+ `**` Look into adopting [this](http://cs.anu.edu.au/~bdm/data/formats.html) [format](http://cs.anu.edu.au/~bdm/data/formats.txt) for representing graphs.  Allows for accommodation of large graphs, and seems to be more commonly used, so would be easier to accept submissions. 

This is similar to what we do, however if we restrict to order n=11 or less we can store the adj as a 64-bit integer.








